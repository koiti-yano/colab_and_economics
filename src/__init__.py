"""
Colab and Economics - Tools for empirical economic analysis.

This package provides utilities for:
- Fetching economic data from various APIs
- Analyzing economic time series
- Visualizing economic data
"""

from .data_fetchers import (
    FREDDataFetcher,
    WorldBankDataFetcher,
    PandasDataReaderFetcher,
    create_sample_data
)

from .analysis_utils import (
    calculate_growth_rate,
    calculate_moving_average,
    detect_trend,
    calculate_correlation_matrix,
    plot_time_series,
    plot_multiple_series,
    plot_correlation_heatmap,
    perform_stationarity_test,
    calculate_summary_statistics
)

__all__ = [
    'FREDDataFetcher',
    'WorldBankDataFetcher',
    'PandasDataReaderFetcher',
    'create_sample_data',
    'calculate_growth_rate',
    'calculate_moving_average',
    'detect_trend',
    'calculate_correlation_matrix',
    'plot_time_series',
    'plot_multiple_series',
    'plot_correlation_heatmap',
    'perform_stationarity_test',
    'calculate_summary_statistics',
]

__version__ = '0.1.0'
