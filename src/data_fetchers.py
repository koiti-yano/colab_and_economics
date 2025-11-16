"""
Module for accessing economic data from various APIs.

This module provides utilities to fetch economic data from:
- FRED (Federal Reserve Economic Data)
- World Bank
- Other public economic data sources
"""

import pandas as pd
import numpy as np
from typing import Optional, List, Dict
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


class FREDDataFetcher:
    """
    Fetcher for FRED (Federal Reserve Economic Data) API.
    
    Note: Requires FRED API key. Get one at: https://fred.stlouisfed.org/docs/api/api_key.html
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize FRED data fetcher.
        
        Args:
            api_key: FRED API key (optional, can be set via environment variable)
        """
        self.api_key = api_key
        
    def get_series(self, series_id: str, start_date: Optional[str] = None, 
                   end_date: Optional[str] = None) -> pd.Series:
        """
        Fetch a FRED data series.
        
        Args:
            series_id: FRED series ID (e.g., 'GDP', 'UNRATE')
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            
        Returns:
            Pandas Series with the data
        """
        try:
            from fredapi import Fred
            
            if not self.api_key:
                raise ValueError("FRED API key is required. Get one at https://fred.stlouisfed.org/docs/api/api_key.html")
            
            fred = Fred(api_key=self.api_key)
            data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
            return data
            
        except ImportError:
            print("fredapi package not found. Install with: pip install fredapi")
            return pd.Series()
        except Exception as e:
            print(f"Error fetching FRED data: {e}")
            return pd.Series()


class WorldBankDataFetcher:
    """
    Fetcher for World Bank data.
    """
    
    def __init__(self):
        """Initialize World Bank data fetcher."""
        pass
        
    def get_indicator(self, indicator: str, countries: List[str], 
                     start_year: Optional[int] = None, 
                     end_year: Optional[int] = None) -> pd.DataFrame:
        """
        Fetch World Bank indicator data.
        
        Args:
            indicator: World Bank indicator code (e.g., 'NY.GDP.MKTP.CD' for GDP)
            countries: List of country ISO codes (e.g., ['USA', 'JPN', 'GBR'])
            start_year: Start year
            end_year: End year
            
        Returns:
            Pandas DataFrame with the data
        """
        try:
            import wbdata
            
            # Convert years to datetime if provided
            date_range = None
            if start_year and end_year:
                import datetime
                date_range = (datetime.datetime(start_year, 1, 1), 
                            datetime.datetime(end_year, 12, 31))
            
            data = wbdata.get_dataframe({indicator: indicator}, 
                                       country=countries,
                                       date=date_range,
                                       convert_date=True)
            return data
            
        except ImportError:
            print("wbdata package not found. Install with: pip install wbdata")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error fetching World Bank data: {e}")
            return pd.DataFrame()


class PandasDataReaderFetcher:
    """
    Fetcher using pandas-datareader for various data sources.
    """
    
    def __init__(self):
        """Initialize pandas-datareader fetcher."""
        pass
        
    def get_data(self, symbols: List[str], source: str = 'yahoo',
                start: Optional[str] = None, end: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch data using pandas-datareader.
        
        Args:
            symbols: List of ticker symbols or economic indicators
            source: Data source ('yahoo', 'fred', 'wb', etc.)
            start: Start date in 'YYYY-MM-DD' format
            end: End date in 'YYYY-MM-DD' format
            
        Returns:
            Pandas DataFrame with the data
        """
        try:
            import pandas_datareader as pdr
            
            data = pdr.DataReader(symbols, source, start=start, end=end)
            return data
            
        except ImportError:
            print("pandas_datareader package not found. Install with: pip install pandas-datareader")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()


def create_sample_data(n_periods: int = 100, start_date: str = '2015-01-01') -> pd.DataFrame:
    """
    Create sample economic data for demonstration purposes.
    
    Args:
        n_periods: Number of time periods
        start_date: Start date for the time series
        
    Returns:
        DataFrame with sample economic indicators
    """
    np.random.seed(42)
    
    # Create date range
    dates = pd.date_range(start=start_date, periods=n_periods, freq='M')
    
    # Generate synthetic economic data
    gdp_base = 20000
    gdp_growth = np.cumsum(np.random.normal(0.02, 0.01, n_periods))
    gdp = gdp_base * np.exp(gdp_growth)
    
    unemployment = 5 + np.random.normal(0, 0.5, n_periods).cumsum() * 0.1
    unemployment = np.clip(unemployment, 2, 15)
    
    inflation = 2 + np.random.normal(0, 0.3, n_periods)
    
    interest_rate = np.maximum(0, 2 + np.random.normal(0, 0.5, n_periods))
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'gdp': gdp,
        'unemployment_rate': unemployment,
        'inflation_rate': inflation,
        'interest_rate': interest_rate
    })
    
    df.set_index('date', inplace=True)
    
    return df


# Example usage
if __name__ == "__main__":
    # Create sample data
    sample_data = create_sample_data()
    print("Sample Economic Data:")
    print(sample_data.head())
    print(f"\nShape: {sample_data.shape}")
    print(f"\nColumns: {sample_data.columns.tolist()}")
