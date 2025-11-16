# Colab and Economics

A comprehensive toolkit for empirical economic analysis using Google Colaboratory and public APIs. This repository provides Python code, Jupyter notebooks, and sample data for analyzing economic indicators, time series, and conducting econometric research.

## 🎯 Features

- **Data Access**: Easy-to-use functions for fetching data from major economic APIs (FRED, World Bank, etc.)
- **Analysis Tools**: Pre-built functions for common economic analysis tasks
- **Interactive Notebooks**: Ready-to-run Jupyter notebooks for Google Colab
- **Sample Data**: Realistic economic datasets for learning and experimentation
- **Visualization**: Professional charts and plots for economic data

## 📁 Repository Structure

```
colab_and_economics/
├── notebooks/               # Jupyter notebooks for Colab
│   ├── 01_introduction_to_economic_analysis.ipynb
│   ├── 02_accessing_economic_apis.ipynb
│   └── 03_time_series_econometrics.ipynb
├── src/                    # Python modules
│   ├── data_fetchers.py   # Functions to fetch data from APIs
│   └── analysis_utils.py  # Utility functions for analysis
├── data/                   # Sample economic data
│   └── sample_economic_data.csv
├── example.py              # Example script to test installation
├── QUICKSTART.md           # Quick start guide
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Quick Start

### Using Google Colab (Recommended)

1. Open any notebook from the `notebooks/` directory in Google Colab
2. Click the "Open in Colab" badge (or manually upload to Colab)
3. Run the first cell to install dependencies
4. Follow along with the examples!

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

### Local Installation

```bash
# Clone the repository
git clone https://github.com/koiti-yano/colab_and_economics.git
cd colab_and_economics

# Install dependencies
pip install -r requirements.txt

# Test the installation
python example.py

# Launch Jupyter
jupyter notebook
```

## 📚 Notebooks

### 1. Introduction to Economic Analysis
**File**: `notebooks/01_introduction_to_economic_analysis.ipynb`

Learn the basics of economic data analysis:
- Loading and exploring economic data
- Time series visualization
- Computing growth rates and moving averages
- Correlation analysis

### 2. Accessing Economic APIs
**File**: `notebooks/02_accessing_economic_apis.ipynb`

Connect to real-world data sources:
- **FRED API**: Federal Reserve Economic Data
- **World Bank API**: Global development indicators
- **pandas-datareader**: Multiple data sources
- Best practices for API usage

### 3. Time Series Econometrics
**File**: `notebooks/03_time_series_econometrics.ipynb`

Advanced econometric techniques:
- Stationarity testing (ADF test)
- Autocorrelation analysis (ACF/PACF)
- ARIMA modeling and forecasting
- Granger causality tests

## 📊 Available Data

### Sample Economic Data
The repository includes sample monthly economic indicators (2010-2023):
- GDP (billions USD)
- Unemployment rate (%)
- Inflation rate (%)
- Interest rate (%)
- Consumer confidence index

Load the data:
```python
import pandas as pd

df = pd.read_csv('data/sample_economic_data.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
```

## 🔧 Python Modules

### Data Fetchers (`src/data_fetchers.py`)

```python
from src.data_fetchers import FREDDataFetcher, WorldBankDataFetcher, create_sample_data

# Create sample data
sample_df = create_sample_data(n_periods=100)

# Fetch FRED data (requires API key)
fred = FREDDataFetcher(api_key='your_key')
gdp_data = fred.get_series('GDP', start_date='2010-01-01')

# Fetch World Bank data
wb = WorldBankDataFetcher()
wb_data = wb.get_indicator('NY.GDP.MKTP.CD', ['USA', 'JPN'])
```

### Analysis Utilities (`src/analysis_utils.py`)

```python
from src.analysis_utils import (
    calculate_growth_rate,
    calculate_moving_average,
    plot_time_series,
    plot_correlation_heatmap
)

# Calculate growth rates
growth_rate = calculate_growth_rate(df['gdp_billions'], periods=12)

# Plot time series
plot_time_series(df['unemployment_rate'], 
                title='Unemployment Rate', 
                show_trend=True)

# Correlation heatmap
plot_correlation_heatmap(df)
```

## 🔑 Getting API Keys

### FRED (Federal Reserve Economic Data)
1. Visit https://fred.stlouisfed.org/
2. Create a free account
3. Request an API key at https://fred.stlouisfed.org/docs/api/api_key.html

### World Bank
No API key required! The World Bank API is free and open.

## 📦 Dependencies

Main packages used:
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **matplotlib**: Plotting
- **seaborn**: Statistical visualization
- **scipy**: Scientific computing
- **statsmodels**: Statistical models and econometrics
- **fredapi**: FRED API client
- **wbdata**: World Bank API client
- **pandas-datareader**: Access to multiple data sources

See `requirements.txt` for complete list with versions.

## 💡 Example Use Cases

### 1. GDP Growth Analysis
```python
import pandas as pd
from src.data_fetchers import create_sample_data
from src.analysis_utils import calculate_growth_rate, plot_time_series

# Load data
df = create_sample_data()

# Calculate growth rate
growth = calculate_growth_rate(df['gdp'], periods=12)

# Visualize
plot_time_series(growth, title='Annual GDP Growth Rate', ylabel='Growth Rate (%)')
```

### 2. Unemployment-Inflation Relationship
```python
import matplotlib.pyplot as plt

# Create scatter plot (Phillips Curve)
plt.figure(figsize=(10, 6))
plt.scatter(df['inflation_rate'], df['unemployment_rate'], alpha=0.6)
plt.xlabel('Inflation Rate (%)')
plt.ylabel('Unemployment Rate (%)')
plt.title('Phillips Curve: Inflation vs Unemployment')
plt.grid(True, alpha=0.3)
plt.show()
```

### 3. Economic Indicators Dashboard
```python
from src.analysis_utils import plot_multiple_series

# Plot multiple indicators
indicators = df[['gdp', 'unemployment_rate', 'consumer_confidence']]
plot_multiple_series(indicators, 
                    title='Economic Indicators Dashboard',
                    normalize=True)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Useful Links

- [FRED API Documentation](https://fred.stlouisfed.org/docs/api/)
- [World Bank API Documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- [Statsmodels Documentation](https://www.statsmodels.org/stable/index.html)
- [Google Colab](https://colab.research.google.com/)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Economic Analysis! 📈**
