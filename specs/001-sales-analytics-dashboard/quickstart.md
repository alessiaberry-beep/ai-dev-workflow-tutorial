# Quickstart: Sales Analytics Dashboard

**Feature**: 001-sales-analytics-dashboard
**Date**: 2026-01-19

This guide provides step-by-step instructions to set up and run the Sales Analytics Dashboard locally.

## Prerequisites

- Python 3.11 or higher
- uv package manager ([installation guide](https://github.com/astral-sh/uv))
- Git

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create Virtual Environment

```bash
# Create and activate virtual environment using uv
uv venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
# Install project dependencies
uv pip install -e .
```

Or if using `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### 4. Verify Data File

Ensure the sales data file exists:

```bash
ls data/sales-data.csv
```

The file should contain ~1,000 transaction records with the following columns:
- date, order_id, product, category, region, quantity, unit_price, total_amount

## Running the Dashboard

### Start Streamlit

```bash
streamlit run app.py
```

The dashboard will open automatically in your default browser at `http://localhost:8501`.

### Expected Output

When the dashboard loads successfully, you should see:

1. **Header**: "ShopSmart Sales Dashboard" (or similar title)
2. **KPI Cards**: Total Sales (~$650,000-$700,000) and Total Orders (482)
3. **Trend Chart**: Line chart showing monthly sales over 12 months
4. **Category Chart**: Bar chart with 5 categories sorted by value
5. **Region Chart**: Bar chart with 4 regions sorted by value

## Verification Checklist

| Check | Expected Result |
|-------|-----------------|
| Dashboard loads | Page appears within 5 seconds |
| KPIs display | Currency and number formatting correct |
| Trend chart renders | Line chart shows 12 months of data |
| Category chart renders | 5 bars sorted highest to lowest |
| Region chart renders | 4 bars sorted highest to lowest |
| Tooltips work | Hover shows exact values |
| No errors | No error messages or warnings |

## Common Issues

### "Data file not found"

**Cause**: The CSV file is missing or in the wrong location.

**Solution**: Ensure `data/sales-data.csv` exists relative to the project root.

### "Module not found" errors

**Cause**: Dependencies not installed or virtual environment not activated.

**Solution**:
```bash
source .venv/bin/activate
uv pip install -e .
```

### Streamlit not found

**Cause**: Streamlit not installed in the active environment.

**Solution**:
```bash
uv pip install streamlit
```

### Charts not rendering

**Cause**: Plotly not installed.

**Solution**:
```bash
uv pip install plotly
```

## Development Workflow

### Making Changes

1. Edit files in `app.py` or `src/` directory
2. Streamlit automatically reloads on file save
3. Check browser for updates

### File Structure

```text
project-root/
├── app.py              # Main Streamlit app (edit this for layout changes)
├── src/
│   ├── data_loader.py  # Data loading functions (edit for data handling)
│   └── charts.py       # Chart functions (edit for visualization changes)
├── data/
│   └── sales-data.csv  # Source data (do not modify)
└── pyproject.toml      # Dependencies
```

## Deployment to Streamlit Community Cloud

### Prerequisites

1. Push code to a public GitHub repository
2. Create account at [share.streamlit.io](https://share.streamlit.io)

### Steps

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Set main file path to `app.py`
5. Click "Deploy"

### Requirements for Deployment

Ensure your repository contains a `requirements.txt`:

```text
streamlit
pandas
plotly
```

The deployed app will be accessible at a URL like:
`https://<your-app-name>.streamlit.app`

## Testing

### Manual Testing Checklist

Run through these checks after making changes:

- [ ] Dashboard loads without errors
- [ ] Total Sales matches sum of CSV `total_amount` column
- [ ] Total Orders matches row count in CSV
- [ ] Trend chart shows correct monthly totals
- [ ] Category chart shows all 5 categories
- [ ] Region chart shows all 4 regions
- [ ] All tooltips display correct values
- [ ] Layout looks professional

### Data Validation

To manually verify KPI calculations:

```python
import pandas as pd

df = pd.read_csv('data/sales-data.csv')
print(f"Total Sales: ${df['total_amount'].sum():,.2f}")
print(f"Total Orders: {len(df):,}")
```

## Next Steps

After completing the quickstart:

1. Review the full [Implementation Plan](./plan.md)
2. Check the [Feature Specification](./spec.md) for acceptance criteria
3. Run `/speckit.tasks` to generate the task list for implementation
