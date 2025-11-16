"""
API utilities for fetching economic data from various sources.

This module provides convenient functions to fetch economic data from:
- FRED (Federal Reserve Economic Data)
- World Bank
- Other economic data sources
"""

import pandas as pd
from typing import Optional, List, Union
from datetime import datetime


class FREDDataFetcher:
    """
    Fetches data from the Federal Reserve Economic Data (FRED) API.
    
    Usage:
        fetcher = FREDDataFetcher(api_key='your_api_key')
        data = fetcher.get_series('GDP')
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize FRED data fetcher.
        
        Args:
            api_key: FRED API key. If None, will try to fetch without authentication
                    (limited access). Get your key at: https://fred.stlouisfed.org/docs/api/api_key.html
        """
        self.api_key = api_key
        
    def get_series(self, series_id: str, start_date: Optional[str] = None, 
                   end_date: Optional[str] = None) -> pd.Series:
        """
        Fetch a single series from FRED.
        
        Args:
            series_id: FRED series ID (e.g., 'GDP', 'UNRATE', 'CPIAUCSL')
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            
        Returns:
            pandas Series with the data
            
        Example:
            >>> fetcher = FREDDataFetcher(api_key='your_key')
            >>> gdp = fetcher.get_series('GDP', start_date='2010-01-01')
        """
        try:
            from fredapi import Fred
            
            if not self.api_key:
                raise ValueError("FRED API key is required. Get one at https://fred.stlouisfed.org/docs/api/api_key.html")
            
            fred = Fred(api_key=self.api_key)
            data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
            return data
            
        except ImportError:
            raise ImportError("fredapi package is required. Install with: pip install fredapi")
    
    def get_multiple_series(self, series_ids: List[str], start_date: Optional[str] = None,
                           end_date: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch multiple series from FRED.
        
        Args:
            series_ids: List of FRED series IDs
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            
        Returns:
            pandas DataFrame with multiple series
            
        Example:
            >>> fetcher = FREDDataFetcher(api_key='your_key')
            >>> data = fetcher.get_multiple_series(['GDP', 'UNRATE'], start_date='2010-01-01')
        """
        series_dict = {}
        for series_id in series_ids:
            series_dict[series_id] = self.get_series(series_id, start_date, end_date)
        
        return pd.DataFrame(series_dict)


class WorldBankDataFetcher:
    """
    Fetches data from the World Bank API.
    
    Usage:
        fetcher = WorldBankDataFetcher()
        data = fetcher.get_indicator('NY.GDP.MKTP.CD', countries=['USA', 'CHN'])
    """
    
    def get_indicator(self, indicator: str, countries: Union[str, List[str]] = 'all',
                     start_year: Optional[int] = None, end_year: Optional[int] = None) -> pd.DataFrame:
        """
        Fetch World Bank indicator data.
        
        Args:
            indicator: World Bank indicator code (e.g., 'NY.GDP.MKTP.CD' for GDP)
            countries: Country code(s) - 'all', single code like 'USA', or list like ['USA', 'CHN']
            start_year: Start year
            end_year: End year
            
        Returns:
            pandas DataFrame with the data
            
        Example:
            >>> fetcher = WorldBankDataFetcher()
            >>> gdp = fetcher.get_indicator('NY.GDP.MKTP.CD', countries=['USA', 'CHN'], 
            ...                              start_year=2000, end_year=2020)
        """
        try:
            import wbdata
            
            # Convert single country to list
            if isinstance(countries, str) and countries != 'all':
                countries = [countries]
            
            # Prepare date range
            date_range = None
            if start_year and end_year:
                date_range = (datetime(start_year, 1, 1), datetime(end_year, 12, 31))
            
            # Fetch data
            if countries == 'all':
                data = wbdata.get_dataframe({indicator: 'value'}, date=date_range)
            else:
                data = wbdata.get_dataframe({indicator: 'value'}, country=countries, date=date_range)
            
            return data
            
        except ImportError:
            raise ImportError("wbdata package is required. Install with: pip install wbdata")


class PandasDataReaderFetcher:
    """
    Fetches data using pandas-datareader for various sources.
    
    Supports: Yahoo Finance, FRED, World Bank, OECD, Eurostat, and more.
    """
    
    def get_data(self, symbols: Union[str, List[str]], source: str = 'yahoo',
                start: Optional[str] = None, end: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch data from various sources using pandas-datareader.
        
        Args:
            symbols: Ticker symbol(s) or data identifier(s)
            source: Data source ('yahoo', 'fred', 'wb', 'oecd', etc.)
            start: Start date in 'YYYY-MM-DD' format
            end: End date in 'YYYY-MM-DD' format
            
        Returns:
            pandas DataFrame with the data
            
        Example:
            >>> fetcher = PandasDataReaderFetcher()
            >>> stock_data = fetcher.get_data('AAPL', source='yahoo', start='2020-01-01')
            >>> fred_data = fetcher.get_data('GDP', source='fred', start='2010-01-01')
        """
        try:
            import pandas_datareader.data as web
            
            data = web.DataReader(symbols, source, start=start, end=end)
            return data
            
        except ImportError:
            raise ImportError("pandas-datareader package is required. Install with: pip install pandas-datareader")


def get_sample_economic_indicators() -> dict:
    """
    Returns a dictionary of commonly used economic indicators and their IDs.
    
    Returns:
        Dictionary mapping indicator names to their codes
    """
    return {
        'FRED': {
            'GDP': 'GDP',  # Gross Domestic Product
            'UNRATE': 'UNRATE',  # Unemployment Rate
            'CPIAUCSL': 'CPIAUCSL',  # Consumer Price Index
            'FEDFUNDS': 'FEDFUNDS',  # Federal Funds Rate
            'DGS10': 'DGS10',  # 10-Year Treasury Constant Maturity Rate
            'DEXUSEU': 'DEXUSEU',  # US/Euro Foreign Exchange Rate
            'PCE': 'PCE',  # Personal Consumption Expenditures
            'PAYEMS': 'PAYEMS',  # All Employees, Total Nonfarm
        },
        'World Bank': {
            'GDP': 'NY.GDP.MKTP.CD',  # GDP (current US$)
            'GDP_per_capita': 'NY.GDP.PCAP.CD',  # GDP per capita (current US$)
            'Population': 'SP.POP.TOTL',  # Population, total
            'Inflation': 'FP.CPI.TOTL.ZG',  # Inflation, consumer prices (annual %)
            'Unemployment': 'SL.UEM.TOTL.ZS',  # Unemployment, total (% of total labor force)
            'Trade': 'NE.TRD.GNFS.ZS',  # Trade (% of GDP)
        }
    }
