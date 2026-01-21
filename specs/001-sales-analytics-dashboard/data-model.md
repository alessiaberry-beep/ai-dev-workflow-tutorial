# Data Model: Sales Analytics Dashboard

**Feature**: 001-sales-analytics-dashboard
**Date**: 2026-01-19
**Source**: CSV file (`data/sales-data.csv`)

## Overview

This document defines the data structures used in the Sales Analytics Dashboard. The primary data source is a CSV file containing sales transaction records. No database is used in Phase 1.

## Entities

### Transaction (Primary Entity)

A single sales record representing one order transaction.

| Field | Type | Description | Example | Validation |
|-------|------|-------------|---------|------------|
| `date` | Date | Transaction date | 2024-01-15 | Must be valid ISO date format |
| `order_id` | String | Unique order identifier | ORD-001234 | Non-empty, unique |
| `product` | String | Product name | Wireless Headphones | Non-empty |
| `category` | String | Product category | Electronics | Must be one of: Electronics, Accessories, Audio, Wearables, Smart Home |
| `region` | String | Geographic region | North | Must be one of: North, South, East, West |
| `quantity` | Integer | Units sold | 2 | Positive integer |
| `unit_price` | Decimal | Price per unit | 49.99 | Non-negative |
| `total_amount` | Decimal | Total transaction value | 99.98 | Non-negative, equals quantity × unit_price |

**Source**: `data/sales-data.csv`
**Volume**: ~1,000 records
**Date Range**: 12 months of historical data

### Category (Reference Entity)

Product classification groupings for segment analysis.

| Value | Description |
|-------|-------------|
| Electronics | Consumer electronic devices |
| Accessories | Product accessories and add-ons |
| Audio | Audio equipment and accessories |
| Wearables | Wearable technology devices |
| Smart Home | Smart home devices and systems |

**Usage**: Used for grouping transactions in the category breakdown chart (FR-004).

### Region (Reference Entity)

Geographic territories for regional performance tracking.

| Value | Description |
|-------|-------------|
| North | Northern geographic region |
| South | Southern geographic region |
| East | Eastern geographic region |
| West | Western geographic region |

**Usage**: Used for grouping transactions in the regional breakdown chart (FR-005).

## Derived Data (Calculated at Runtime)

### KPIs

| Metric | Calculation | Format |
|--------|-------------|--------|
| Total Sales | `SUM(total_amount)` | US Currency ($X,XXX.XX) |
| Total Orders | `COUNT(*)` | Integer with thousands separator |

### Aggregations

| Aggregation | Calculation | Used For |
|-------------|-------------|----------|
| Monthly Sales | `GROUP BY date.month, SUM(total_amount)` | Sales trend line chart |
| Category Sales | `GROUP BY category, SUM(total_amount), ORDER BY SUM DESC` | Category bar chart |
| Region Sales | `GROUP BY region, SUM(total_amount), ORDER BY SUM DESC` | Region bar chart |

## Data Flow

```text
┌─────────────────────────────────────────────────────────────┐
│                    data/sales-data.csv                       │
│                    (Source of Truth)                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    src/data_loader.py                        │
│                                                              │
│  • load_sales_data() → DataFrame                            │
│  • Parses dates, validates types                            │
│  • Handles missing file / empty data errors                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Pandas DataFrame                          │
│                    (In-Memory)                               │
│                                                              │
│  Columns: date, order_id, product, category, region,        │
│           quantity, unit_price, total_amount                 │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   KPI Calcs     │ │  Trend Agg      │ │  Breakdown Agg  │
│                 │ │                 │ │                 │
│ • Total Sales   │ │ • Monthly sum   │ │ • By category   │
│ • Total Orders  │ │                 │ │ • By region     │
└─────────────────┘ └─────────────────┘ └─────────────────┘
              │               │               │
              └───────────────┼───────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    src/charts.py                             │
│                                                              │
│  • create_trend_chart() → Plotly Figure                     │
│  • create_category_chart() → Plotly Figure                  │
│  • create_region_chart() → Plotly Figure                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    app.py (Streamlit)                        │
│                                                              │
│  • Displays KPI metrics                                     │
│  • Renders Plotly charts                                    │
│  • Handles errors with user-friendly messages               │
└─────────────────────────────────────────────────────────────┘
```

## Error Handling

| Error Condition | Handling | User Message |
|-----------------|----------|--------------|
| CSV file missing | Catch `FileNotFoundError` | "Data file not found. Please ensure sales-data.csv exists in the data/ directory." |
| CSV file empty | Check row count after load | "No data available. The data file appears to be empty." |
| Missing values in numeric columns | Use `fillna(0)` or `dropna()` | N/A (handled silently) |
| Malformed dates | `errors='coerce'` in `pd.to_datetime()` | N/A (invalid dates become NaT and are excluded) |
| Invalid category/region values | Display as-is | N/A (no strict validation in Phase 1) |

## Relationships

```text
Transaction ──────> Category (many-to-one via category field)
Transaction ──────> Region (many-to-one via region field)
```

- Each Transaction belongs to exactly one Category
- Each Transaction belongs to exactly one Region
- Categories and Regions are fixed reference values (not stored separately)

## Constraints

1. **Data Immutability**: Dashboard is read-only; no data modification capabilities
2. **Single Source**: All data comes from one CSV file
3. **In-Memory Processing**: Entire dataset loaded into memory (acceptable for ~1000 records)
4. **No Persistence**: No application state is saved between sessions
5. **No Real-Time Updates**: Data reflects CSV contents at load time only

## Sample Data Structure

```csv
date,order_id,product,category,region,quantity,unit_price,total_amount
2024-01-15,ORD-001234,Wireless Headphones,Audio,North,2,49.99,99.98
2024-01-15,ORD-001235,Smart Watch,Wearables,South,1,199.99,199.99
2024-01-16,ORD-001236,Phone Case,Accessories,East,3,19.99,59.97
```
