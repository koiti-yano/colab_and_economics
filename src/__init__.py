"""
Economic Analysis Utilities

This package provides tools for fetching and analyzing economic data.
"""

from .api_utils import (
    FREDDataFetcher,
    WorldBankDataFetcher,
    PandasDataReaderFetcher,
    get_sample_economic_indicators
)

from .analysis_utils import (
    calculate_growth_rate,
    calculate_log_returns,
    calculate_moving_average,
    calculate_correlation_matrix,
    plot_time_series,
    plot_multiple_series,
    plot_correlation_heatmap,
    descriptive_statistics,
    seasonal_decomposition,
    test_stationarity
)

__version__ = '0.1.0'
__all__ = [
    'FREDDataFetcher',
    'WorldBankDataFetcher',
    'PandasDataReaderFetcher',
    'get_sample_economic_indicators',
    'calculate_growth_rate',
    'calculate_log_returns',
    'calculate_moving_average',
    'calculate_correlation_matrix',
    'plot_time_series',
    'plot_multiple_series',
    'plot_correlation_heatmap',
    'descriptive_statistics',
    'seasonal_decomposition',
    'test_stationarity'
]
