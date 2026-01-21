"""Sales Analytics Dashboard - Main Streamlit Application."""

import streamlit as st

from src.data_loader import (
    load_sales_data,
    calculate_total_sales,
    calculate_total_orders,
    format_currency,
    format_number,
    aggregate_monthly_sales,
    aggregate_category_sales,
    aggregate_region_sales,
)
from src.charts import (
    create_trend_chart,
    create_category_chart,
    create_region_chart,
)

# Page configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Sales Analytics Dashboard")


@st.cache_data
def load_data():
    """Load and cache sales data."""
    return load_sales_data()


# Load data with error handling
try:
    with st.spinner("Loading sales data..."):
        df = load_data()

    # KPI Section
    st.header("Key Performance Indicators")
    col1, col2 = st.columns(2)

    with col1:
        total_sales = calculate_total_sales(df)
        st.metric("Total Sales", format_currency(total_sales))

    with col2:
        total_orders = calculate_total_orders(df)
        st.metric("Total Orders", format_number(total_orders))

    # Trend Chart
    st.header("Sales Trend")
    monthly_data = aggregate_monthly_sales(df)
    trend_chart = create_trend_chart(monthly_data)
    st.plotly_chart(trend_chart, use_container_width=True)

    # Category and Region Charts side by side
    st.header("Sales Breakdown")
    col1, col2 = st.columns(2)

    with col1:
        category_data = aggregate_category_sales(df)
        category_chart = create_category_chart(category_data)
        st.plotly_chart(category_chart, use_container_width=True)

    with col2:
        region_data = aggregate_region_sales(df)
        region_chart = create_region_chart(region_data)
        st.plotly_chart(region_chart, use_container_width=True)

except FileNotFoundError as e:
    st.error("Data file not found. Please ensure sales-data.csv exists in the data/ directory.")
    st.exception(e)

except ValueError as e:
    st.error("No data available. The data file appears to be empty or invalid.")
    st.exception(e)

except Exception as e:
    st.error("An unexpected error occurred while loading the dashboard.")
    st.exception(e)
