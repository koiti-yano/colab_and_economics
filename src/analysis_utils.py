"""
Analysis utilities for economic data.

This module provides common functions for analyzing and visualizing economic data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple, List


def calculate_growth_rate(data: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate period-over-period growth rate.
    
    Args:
        data: Time series data
        periods: Number of periods for growth calculation (default: 1)
        
    Returns:
        Growth rate as percentage
        
    Example:
        >>> gdp_growth = calculate_growth_rate(gdp_data, periods=4)  # Year-over-year for quarterly data
    """
    return data.pct_change(periods=periods) * 100


def calculate_log_returns(data: pd.Series) -> pd.Series:
    """
    Calculate logarithmic returns.
    
    Args:
        data: Time series data
        
    Returns:
        Log returns
    """
    return np.log(data / data.shift(1))


def calculate_moving_average(data: pd.Series, window: int) -> pd.Series:
    """
    Calculate moving average.
    
    Args:
        data: Time series data
        window: Window size for moving average
        
    Returns:
        Moving average series
    """
    return data.rolling(window=window).mean()


def detrend_series(data: pd.Series, method: str = 'linear') -> pd.Series:
    """
    Detrend a time series.
    
    Args:
        data: Time series data
        method: Detrending method ('linear', 'log')
        
    Returns:
        Detrended series
    """
    from scipy import signal
    
    if method == 'linear':
        return pd.Series(signal.detrend(data.values), index=data.index)
    elif method == 'log':
        log_data = np.log(data)
        return pd.Series(signal.detrend(log_data.values), index=data.index)
    else:
        raise ValueError("Method must be 'linear' or 'log'")


def calculate_correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate correlation matrix for multiple time series.
    
    Args:
        data: DataFrame with multiple time series
        
    Returns:
        Correlation matrix
    """
    return data.corr()


def plot_time_series(data: pd.Series, title: str = "Time Series Plot",
                     ylabel: str = "Value", figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot a time series.
    
    Args:
        data: Time series data
        title: Plot title
        ylabel: Y-axis label
        figsize: Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    plt.plot(data.index, data.values, linewidth=2)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_multiple_series(data: pd.DataFrame, title: str = "Multiple Time Series",
                        ylabel: str = "Value", figsize: Tuple[int, int] = (12, 6),
                        normalize: bool = False) -> None:
    """
    Plot multiple time series on the same chart.
    
    Args:
        data: DataFrame with multiple time series
        title: Plot title
        ylabel: Y-axis label
        figsize: Figure size (width, height)
        normalize: Whether to normalize series to start at 100
    """
    plt.figure(figsize=figsize)
    
    if normalize:
        data_plot = data.div(data.iloc[0]) * 100
        ylabel = "Index (Base = 100)"
    else:
        data_plot = data
    
    for column in data_plot.columns:
        plt.plot(data_plot.index, data_plot[column], label=column, linewidth=2)
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(data: pd.DataFrame, title: str = "Correlation Matrix",
                            figsize: Tuple[int, int] = (10, 8)) -> None:
    """
    Plot correlation heatmap for multiple time series.
    
    Args:
        data: DataFrame with multiple time series
        title: Plot title
        figsize: Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    corr = calculate_correlation_matrix(data)
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def descriptive_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate descriptive statistics for time series data.
    
    Args:
        data: DataFrame with time series data
        
    Returns:
        DataFrame with descriptive statistics
    """
    stats = pd.DataFrame({
        'Mean': data.mean(),
        'Median': data.median(),
        'Std Dev': data.std(),
        'Min': data.min(),
        'Max': data.max(),
        'Skewness': data.skew(),
        'Kurtosis': data.kurtosis()
    })
    return stats


def seasonal_decomposition(data: pd.Series, model: str = 'additive', 
                          period: Optional[int] = None) -> Tuple:
    """
    Perform seasonal decomposition of time series.
    
    Args:
        data: Time series data
        model: 'additive' or 'multiplicative'
        period: Period for seasonal component (auto-detected if None)
        
    Returns:
        Tuple of (trend, seasonal, residual)
    """
    from statsmodels.tsa.seasonal import seasonal_decompose
    
    result = seasonal_decompose(data, model=model, period=period)
    
    return result.trend, result.seasonal, result.resid


def plot_seasonal_decomposition(data: pd.Series, model: str = 'additive',
                                period: Optional[int] = None, 
                                figsize: Tuple[int, int] = (12, 10)) -> None:
    """
    Plot seasonal decomposition of time series.
    
    Args:
        data: Time series data
        model: 'additive' or 'multiplicative'
        period: Period for seasonal component
        figsize: Figure size (width, height)
    """
    from statsmodels.tsa.seasonal import seasonal_decompose
    
    result = seasonal_decompose(data, model=model, period=period)
    
    fig, axes = plt.subplots(4, 1, figsize=figsize)
    
    result.observed.plot(ax=axes[0], title='Observed')
    axes[0].set_ylabel('Observed')
    
    result.trend.plot(ax=axes[1], title='Trend')
    axes[1].set_ylabel('Trend')
    
    result.seasonal.plot(ax=axes[2], title='Seasonal')
    axes[2].set_ylabel('Seasonal')
    
    result.resid.plot(ax=axes[3], title='Residual')
    axes[3].set_ylabel('Residual')
    
    plt.tight_layout()
    plt.show()


def test_stationarity(data: pd.Series, verbose: bool = True) -> dict:
    """
    Test for stationarity using Augmented Dickey-Fuller test.
    
    Args:
        data: Time series data
        verbose: Whether to print results
        
    Returns:
        Dictionary with test results
    """
    from statsmodels.tsa.stattools import adfuller
    
    result = adfuller(data.dropna())
    
    output = {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Used Lag': result[2],
        'Number of Observations': result[3],
        'Critical Values': result[4],
        'Is Stationary': result[1] < 0.05
    }
    
    if verbose:
        print('Augmented Dickey-Fuller Test:')
        print(f'ADF Statistic: {output["ADF Statistic"]:.6f}')
        print(f'p-value: {output["p-value"]:.6f}')
        print(f'Number of Lags Used: {output["Used Lag"]}')
        print(f'Number of Observations: {output["Number of Observations"]}')
        print('Critical Values:')
        for key, value in output['Critical Values'].items():
            print(f'   {key}: {value:.3f}')
        print(f'\nConclusion: The series is {"stationary" if output["Is Stationary"] else "non-stationary"} at 5% significance level.')
    
    return output
