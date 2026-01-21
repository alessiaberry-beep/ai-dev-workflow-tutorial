"""Data loading and processing functions for the Sales Analytics Dashboard."""

import pandas as pd
from pathlib import Path


def load_sales_data(filepath: str = "data/sales-data.csv") -> pd.DataFrame:
    """Load sales data from CSV file with date parsing and type validation.

    Args:
        filepath: Path to the CSV file

    Returns:
        DataFrame with sales data

    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        ValueError: If the data is empty or invalid
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Sales data file not found: {filepath}")

    df = pd.read_csv(filepath, parse_dates=["date"])

    if df.empty:
        raise ValueError("Sales data file is empty")

    # Validate required columns
    required_columns = ["date", "order_id", "product", "category", "region",
                       "quantity", "unit_price", "total_amount"]
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df


def calculate_total_sales(df: pd.DataFrame) -> float:
    """Calculate total sales from the data.

    Args:
        df: Sales DataFrame

    Returns:
        Sum of total_amount column
    """
    return df["total_amount"].sum()


def calculate_total_orders(df: pd.DataFrame) -> int:
    """Calculate total number of orders.

    Args:
        df: Sales DataFrame

    Returns:
        Count of rows (orders)
    """
    return len(df)


def format_currency(value: float) -> str:
    """Format a number as US currency.

    Args:
        value: Numeric value to format

    Returns:
        Formatted string like "$687,432"
    """
    return f"${value:,.0f}"


def format_number(value: int) -> str:
    """Format a number with thousands separators.

    Args:
        value: Integer value to format

    Returns:
        Formatted string like "1,234"
    """
    return f"{value:,}"


def aggregate_monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by month.

    Args:
        df: Sales DataFrame

    Returns:
        DataFrame with month and total_amount columns
    """
    monthly = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum().reset_index()
    monthly["date"] = monthly["date"].dt.to_timestamp()
    monthly.columns = ["month", "total_amount"]
    return monthly


def aggregate_category_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by category, sorted descending.

    Args:
        df: Sales DataFrame

    Returns:
        DataFrame with category and total_amount columns, sorted by total descending
    """
    category_sales = df.groupby("category")["total_amount"].sum().reset_index()
    category_sales = category_sales.sort_values("total_amount", ascending=False)
    return category_sales


def aggregate_region_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by region, sorted descending.

    Args:
        df: Sales DataFrame

    Returns:
        DataFrame with region and total_amount columns, sorted by total descending
    """
    region_sales = df.groupby("region")["total_amount"].sum().reset_index()
    region_sales = region_sales.sort_values("total_amount", ascending=False)
    return region_sales
