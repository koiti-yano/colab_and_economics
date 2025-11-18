# Quick Start Guide

## For Google Colab Users

### Option 1: Direct Upload
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click `File` → `Upload notebook`
3. Upload any notebook from the `notebooks/` directory
4. Run the first cell to install dependencies
5. Start analyzing!

### Option 2: From GitHub
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click `File` → `Open notebook` → `GitHub` tab
3. Enter: `koiti-yano/colab_and_economics`
4. Select a notebook to open
5. Run the first cell to install dependencies

## For Local Jupyter Users

```bash
# Clone the repository
git clone https://github.com/koiti-yano/colab_and_economics.git
cd colab_and_economics

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

Navigate to the `notebooks/` directory and open any notebook.

## First Steps

### 1. Start with the Introduction Notebook
Open `01_introduction_to_economic_analysis.ipynb` to learn:
- Loading and exploring economic data
- Basic time series visualization
- Computing growth rates and moving averages
- Correlation analysis

### 2. Learn API Access
Open `02_accessing_economic_apis.ipynb` to:
- Get data from FRED (Federal Reserve)
- Access World Bank indicators
- Use pandas-datareader
- **Note**: You'll need a free FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html

### 3. Advanced Econometrics
Open `03_time_series_econometrics.ipynb` for:
- Stationarity testing
- ARIMA modeling
- Forecasting
- Granger causality tests

## Using the Python Modules

You can also use the Python modules directly in your own scripts:

```python
# Import the modules
from src.data_fetchers import create_sample_data, FREDDataFetcher
from src.analysis_utils import plot_time_series, calculate_growth_rate

# Create sample data
df = create_sample_data(n_periods=100)

# Calculate growth rate
growth = calculate_growth_rate(df['gdp'], periods=12)

# Visualize
plot_time_series(df['gdp'], title='GDP Over Time', show_trend=True)
```

## Getting API Keys

### FRED (Required for US economic data)
1. Visit https://fred.stlouisfed.org/
2. Create a free account
3. Go to https://fred.stlouisfed.org/docs/api/api_key.html
4. Request an API key (instant approval)

### World Bank (No key needed!)
The World Bank API is completely free and doesn't require any authentication.

## Common Issues

### "Module not found" errors
**Solution**: Run the first cell in the notebook:
```python
!pip install pandas numpy matplotlib seaborn scipy statsmodels fredapi wbdata pandas-datareader -q
```

### "FRED API key required" error
**Solution**: Get a free API key from FRED (see above) and set it:
```python
FRED_API_KEY = 'your_key_here'
fred = FREDDataFetcher(api_key=FRED_API_KEY)
```

### Data file not found in Colab
**Solution**: The notebooks will automatically try to load from GitHub if local file is not found.

## Example Projects

### Project 1: GDP Growth Analysis
```python
import pandas as pd
from src.data_fetchers import create_sample_data
from src.analysis_utils import calculate_growth_rate, plot_time_series

df = create_sample_data()
growth = calculate_growth_rate(df['gdp'], periods=12)
plot_time_series(growth, title='Annual GDP Growth Rate')
```

### Project 2: Unemployment Forecasting
```python
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

df = pd.read_csv('data/sample_economic_data.csv', parse_dates=['date'])
df.set_index('date', inplace=True)

model = ARIMA(df['unemployment_rate'], order=(1,1,1))
results = model.fit()
forecast = results.forecast(steps=12)
print(forecast)
```

### Project 3: Multi-Country Comparison
```python
from src.data_fetchers import WorldBankDataFetcher

wb = WorldBankDataFetcher()
gdp_data = wb.get_indicator('NY.GDP.MKTP.CD', 
                            countries=['USA', 'JPN', 'GBR'],
                            start_year=2010, 
                            end_year=2023)
```

## Next Steps

1. ✅ Complete all three notebooks
2. 📚 Read the main README.md for detailed documentation
3. 🔑 Get your FRED API key to access real US economic data
4. 🌍 Explore World Bank data for international comparisons
5. 📊 Create your own analysis projects
6. 🚀 Share your findings!

## Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review the notebook examples
- Open an issue on GitHub
- Consult API documentation:
  - [FRED API Docs](https://fred.stlouisfed.org/docs/api/)
  - [World Bank API Docs](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392)

Happy analyzing! 📈
