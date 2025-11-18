# Data Directory

This directory contains sample economic data files for demonstration purposes.

## Files

### sample_economic_data.csv
Sample monthly economic indicators from 2010-2023:
- **date**: Monthly date
- **gdp_billions**: Gross Domestic Product in billions of USD
- **unemployment_rate**: Unemployment rate as percentage
- **inflation_rate**: Inflation rate as percentage
- **interest_rate**: Interest rate as percentage
- **consumer_confidence**: Consumer confidence index (base = 100)

## Usage

You can load the data in your notebooks:

```python
import pandas as pd

# Load sample data
df = pd.read_csv('data/sample_economic_data.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

print(df.head())
```

## Adding Your Own Data

Place your economic data files in this directory. Supported formats:
- CSV (.csv)
- Excel (.xlsx)
- JSON (.json)
- Parquet (.parquet)
