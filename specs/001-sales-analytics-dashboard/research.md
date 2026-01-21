# Research: Sales Analytics Dashboard

**Feature**: 001-sales-analytics-dashboard
**Date**: 2026-01-19
**Status**: Complete

## Overview

This document captures technology decisions and best practices research for implementing the Sales Analytics Dashboard. All technical choices were pre-determined by the project constitution and user requirements, so this research focuses on implementation patterns and Streamlit/Plotly best practices.

## Technology Decisions

### 1. Dashboard Framework: Streamlit

**Decision**: Use Streamlit as the dashboard framework

**Rationale**:
- Mandated by project constitution (Technology Standards)
- Python-native, reducing learning curve for Python developers
- Built-in support for interactive widgets and data visualization
- Simple deployment to Streamlit Community Cloud
- Automatic reactive updates when data changes

**Alternatives Considered**:
- Dash (Plotly): More complex, better for production apps but overkill for this use case
- Flask + templates: Requires more boilerplate, manual JavaScript for interactivity
- Jupyter notebooks: Not suitable for sharing with non-technical stakeholders

**Best Practices for Streamlit**:
- Use `@st.cache_data` decorator to cache data loading (prevents re-reading CSV on every interaction)
- Organize layout with `st.columns()` for side-by-side content
- Use `st.metric()` for KPI display with built-in formatting
- Set page config at the top of the app for title and layout

### 2. Data Processing: Pandas

**Decision**: Use Pandas for all data manipulation

**Rationale**:
- Mandated by project constitution (Technology Standards)
- Industry standard for tabular data processing in Python
- Excellent CSV reading capabilities with `pd.read_csv()`
- Efficient aggregation operations (groupby, sum, count)
- Seamless integration with Plotly

**Alternatives Considered**:
- Polars: Faster but less familiar, smaller ecosystem
- Pure Python: Too slow for data processing, no vectorization
- SQL/SQLite: Unnecessary complexity for read-only CSV data

**Best Practices for Pandas**:
- Parse dates during CSV read: `pd.read_csv(..., parse_dates=['date'])`
- Use vectorized operations instead of row iteration
- Handle missing values explicitly with `fillna()` or `dropna()`
- Use `groupby().agg()` for multiple aggregations in one pass

### 3. Visualization: Plotly

**Decision**: Use Plotly Express for all charts

**Rationale**:
- Mandated by project constitution (Technology Standards)
- Built-in interactivity (tooltips, zoom, pan) without extra code
- Professional appearance suitable for executive presentations
- Native Streamlit integration via `st.plotly_chart()`
- Consistent styling across chart types

**Alternatives Considered**:
- Matplotlib: Static images, requires more code for formatting
- Altair: Good declarative API but less feature-rich tooltips
- Streamlit native charts: Limited customization options

**Best Practices for Plotly**:
- Use Plotly Express (`px`) for simple charts (line, bar)
- Configure hover templates for clear tooltip formatting
- Set consistent color schemes across all charts
- Use `update_layout()` for titles, axis labels, and formatting

### 4. Package Management: uv

**Decision**: Use uv for package management and virtual environments

**Rationale**:
- Mandated by project constitution (Technology Standards)
- Faster than pip for dependency resolution
- Built-in virtual environment management
- Compatible with standard `pyproject.toml` format

**Setup Commands**:
```bash
# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -e .
```

### 5. Deployment: Streamlit Community Cloud

**Decision**: Deploy to Streamlit Community Cloud for public access

**Rationale**:
- Free hosting for public Streamlit apps
- Direct GitHub integration for automatic deployments
- No server configuration required
- Meets requirement for publicly accessible URL (SC-008)

**Deployment Requirements**:
- `requirements.txt` file listing all dependencies
- Main app file at repository root (or configured path)
- Public GitHub repository

## Data Handling Patterns

### CSV Loading with Error Handling

```python
def load_sales_data(file_path: str) -> pd.DataFrame:
    """Load sales data from CSV with error handling."""
    try:
        df = pd.read_csv(
            file_path,
            parse_dates=['date'],
            dtype={
                'order_id': str,
                'product': str,
                'category': str,
                'region': str,
                'quantity': int,
                'unit_price': float,
                'total_amount': float
            }
        )
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("Data file is empty")
```

### KPI Calculations

```python
def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calculate key performance indicators from sales data."""
    return {
        'total_sales': df['total_amount'].sum(),
        'total_orders': len(df)
    }
```

### Aggregation Patterns

```python
# Monthly sales trend
monthly_sales = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum()

# Sales by category
category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)

# Sales by region
region_sales = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
```

## Chart Patterns

### Line Chart for Trends

```python
import plotly.express as px

fig = px.line(
    monthly_sales_df,
    x='month',
    y='sales',
    title='Sales Trend Over Time',
    labels={'month': 'Month', 'sales': 'Sales ($)'}
)
fig.update_traces(hovertemplate='%{x}<br>Sales: $%{y:,.2f}')
```

### Bar Chart for Categories/Regions

```python
fig = px.bar(
    category_sales_df,
    x='category',
    y='sales',
    title='Sales by Category',
    labels={'category': 'Category', 'sales': 'Sales ($)'}
)
fig.update_traces(hovertemplate='%{x}<br>Sales: $%{y:,.2f}')
```

## Currency Formatting

```python
def format_currency(value: float) -> str:
    """Format a number as US currency."""
    return f"${value:,.2f}"

def format_number(value: int) -> str:
    """Format a number with thousands separators."""
    return f"{value:,}"
```

## Accessibility Considerations

- Use colorblind-friendly palettes (Plotly's default is acceptable)
- Ensure sufficient contrast for text labels
- Include clear axis labels and chart titles
- Provide tooltips with exact values for all data points

## Performance Considerations

- Cache data loading with `@st.cache_data` to avoid repeated CSV reads
- Data volume (~1000 records) is small enough for in-memory processing
- No pagination or lazy loading needed at this scale
- Expected load time: <2 seconds for all operations

## Resolved Items

| Item | Resolution | Source |
|------|------------|--------|
| Dashboard framework | Streamlit | Constitution mandate |
| Data processing | Pandas | Constitution mandate |
| Visualization library | Plotly | Constitution mandate |
| Package manager | uv | Constitution mandate |
| Deployment target | Streamlit Community Cloud | PRD requirement |
| Authentication | None required | Spec: Out of Scope |
| Data source | CSV file | PRD requirement |

## Open Items

None. All technical decisions resolved.
