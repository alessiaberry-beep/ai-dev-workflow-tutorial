"""Chart generation functions for the Sales Analytics Dashboard."""

import plotly.express as px
import pandas as pd

# Consistent color scheme - Purple brand theme
COLORS = {
    "primary": "#7B1FA2",
    "secondary": "#AB47BC",
    "category_palette": ["#7B1FA2", "#9C27B0", "#AB47BC", "#BA68C8", "#CE93D8"],
    "region_palette": ["#6A1B9A", "#8E24AA", "#AB47BC", "#CE93D8"],
}


def create_trend_chart(monthly_data: pd.DataFrame) -> px.line:
    """Create a line chart showing monthly sales trends.

    Args:
        monthly_data: DataFrame with month and total_amount columns

    Returns:
        Plotly Express line chart figure
    """
    fig = px.line(
        monthly_data,
        x="month",
        y="total_amount",
        title="Sales Trend Over Time",
        labels={"month": "Month", "total_amount": "Sales Amount ($)"},
    )

    fig.update_traces(
        line_color=COLORS["primary"],
        hovertemplate="<b>%{x|%B %Y}</b><br>Sales: $%{y:,.0f}<extra></extra>",
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales Amount ($)",
        hovermode="x unified",
    )

    return fig


def create_category_chart(category_data: pd.DataFrame) -> px.bar:
    """Create a bar chart showing sales by category.

    Args:
        category_data: DataFrame with category and total_amount columns

    Returns:
        Plotly Express bar chart figure
    """
    fig = px.bar(
        category_data,
        x="category",
        y="total_amount",
        title="Sales by Category",
        labels={"category": "Category", "total_amount": "Sales Amount ($)"},
        color="category",
        color_discrete_sequence=COLORS["category_palette"],
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>",
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales Amount ($)",
        showlegend=False,
    )

    return fig


def create_region_chart(region_data: pd.DataFrame) -> px.bar:
    """Create a bar chart showing sales by region.

    Args:
        region_data: DataFrame with region and total_amount columns

    Returns:
        Plotly Express bar chart figure
    """
    fig = px.bar(
        region_data,
        x="region",
        y="total_amount",
        title="Sales by Region",
        labels={"region": "Region", "total_amount": "Sales Amount ($)"},
        color="region",
        color_discrete_sequence=COLORS["region_palette"],
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>",
    )

    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales Amount ($)",
        showlegend=False,
    )

    return fig
