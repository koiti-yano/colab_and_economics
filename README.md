# Economic Analysis with Colaboratory and APIs

This repository contains codes and data for empirical economic analysis using Google Colaboratory and various economic data APIs.

## Features

- **Easy Data Fetching**: Utilities to fetch economic data from multiple sources
  - Federal Reserve Economic Data (FRED)
  - World Bank Open Data
  - Yahoo Finance
  - And more via pandas-datareader

- **Analysis Tools**: Common economic analysis functions
  - Growth rate calculations
  - Correlation analysis
  - Time series decomposition
  - Stationarity tests
  - And more

- **Visualization**: Built-in plotting functions for economic data
  - Time series plots
  - Correlation heatmaps
  - Seasonal decomposition plots

- **Colab-Ready**: All notebooks are designed to run seamlessly on Google Colaboratory

## Quick Start

### Installation

1. Clone this repository:
```bash
git clone https://github.com/koiti-yano/colab_and_economics.git
cd colab_and_economics
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Using in Google Colaboratory

1. Open any notebook from the `notebooks/` directory in Google Colab
2. The notebooks will automatically install required dependencies
3. Follow the examples in each notebook

### Basic Usage

#### Fetching FRED Data

```python
from src.api_utils import FREDDataFetcher

# Initialize with your API key
fetcher = FREDDataFetcher(api_key='your_fred_api_key')

# Fetch GDP data
gdp = fetcher.get_series('GDP', start_date='2010-01-01')

# Fetch multiple series
data = fetcher.get_multiple_series(['GDP', 'UNRATE', 'CPIAUCSL'], 
                                   start_date='2010-01-01')
```

Get your free FRED API key at: https://fred.stlouisfed.org/docs/api/api_key.html

#### Fetching World Bank Data

```python
from src.api_utils import WorldBankDataFetcher

# Initialize fetcher
fetcher = WorldBankDataFetcher()

# Fetch GDP data for specific countries
gdp = fetcher.get_indicator('NY.GDP.MKTP.CD', 
                            countries=['USA', 'CHN', 'JPN'],
                            start_year=2000, end_year=2020)
```

#### Analysis Example

```python
from src.analysis_utils import calculate_growth_rate, plot_time_series

# Calculate GDP growth rate
gdp_growth = calculate_growth_rate(gdp, periods=4)  # Year-over-year

# Plot the results
plot_time_series(gdp_growth, title='GDP Growth Rate', ylabel='% Change')
```

## Repository Structure

```
colab_and_economics/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── notebooks/               # Jupyter notebooks for Colab
│   ├── 01_getting_started.ipynb
│   ├── 02_fred_data_analysis.ipynb
│   └── 03_world_bank_analysis.ipynb
├── src/                     # Source code
│   ├── api_utils.py        # API fetching utilities
│   └── analysis_utils.py   # Analysis and visualization functions
└── data/                    # Sample data files (if any)
```

## Available Data Sources

### FRED (Federal Reserve Economic Data)
- GDP, Unemployment Rate, Inflation
- Interest Rates, Exchange Rates
- And thousands of other economic indicators

### World Bank
- GDP, Population, Trade
- Development Indicators
- Country-level statistics

### Other Sources (via pandas-datareader)
- Yahoo Finance for stock market data
- OECD statistics
- Eurostat data

## Common Economic Indicators

### FRED Series IDs
- `GDP`: Gross Domestic Product
- `UNRATE`: Unemployment Rate
- `CPIAUCSL`: Consumer Price Index
- `FEDFUNDS`: Federal Funds Rate
- `DGS10`: 10-Year Treasury Rate
- `PAYEMS`: Total Nonfarm Payroll

### World Bank Indicators
- `NY.GDP.MKTP.CD`: GDP (current US$)
- `NY.GDP.PCAP.CD`: GDP per capita
- `SP.POP.TOTL`: Population
- `FP.CPI.TOTL.ZG`: Inflation rate
- `SL.UEM.TOTL.ZS`: Unemployment rate

## Examples

Check out the notebooks in the `notebooks/` directory for detailed examples:

1. **Getting Started**: Introduction to fetching and analyzing economic data
2. **FRED Data Analysis**: Deep dive into FRED data with examples
3. **World Bank Analysis**: International economic comparisons using World Bank data

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- statsmodels
- scikit-learn
- pandas-datareader
- fredapi
- wbdata
- jupyter

See `requirements.txt` for complete list with versions.

## Contributing

Contributions are welcome! Feel free to:
- Add new data sources
- Improve analysis functions
- Add new example notebooks
- Fix bugs or improve documentation

## License

This project is open source and available for educational and research purposes.

## Resources

- [FRED API Documentation](https://fred.stlouisfed.org/docs/api/fred/)
- [World Bank API Documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- [pandas-datareader Documentation](https://pandas-datareader.readthedocs.io/)
- [Google Colaboratory](https://colab.research.google.com/)

## Citation

If you use this repository in your research or projects, please cite:

```
@misc{colab_and_economics,
  author = {Koiti Yano},
  title = {Codes and Data for Empirical Economic Analysis with Colaboratory and APIs},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/koiti-yano/colab_and_economics}
}
```

## Contact

For questions or suggestions, please open an issue on GitHub.
