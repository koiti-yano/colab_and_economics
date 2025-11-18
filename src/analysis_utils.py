"""
Utilities for economic data analysis.

This module provides functions for common economic analysis tasks:
- Time series analysis
- Statistical tests
- Data visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple, List

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def calculate_growth_rate(series: pd.Series, periods: int = 1) -> pd.Series:
    """
    Calculate period-over-period growth rate.
    
    Args:
        series: Time series data
        periods: Number of periods for growth calculation
        
    Returns:
        Series with growth rates
    """
    return series.pct_change(periods=periods) * 100


def calculate_moving_average(series: pd.Series, window: int = 12) -> pd.Series:
    """
    Calculate moving average.
    
    Args:
        series: Time series data
        window: Window size for moving average
        
    Returns:
        Series with moving averages
    """
    return series.rolling(window=window).mean()


def detect_trend(series: pd.Series) -> Tuple[float, float, float]:
    """
    Detect trend in time series using linear regression.
    
    Args:
        series: Time series data
        
    Returns:
        Tuple of (slope, intercept, r_squared)
    """
    from scipy import stats
    
    # Remove NaN values
    clean_series = series.dropna()
    
    if len(clean_series) < 2:
        return (np.nan, np.nan, np.nan)
    
    x = np.arange(len(clean_series))
    y = clean_series.values
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    r_squared = r_value ** 2
    
    return slope, intercept, r_squared


def calculate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate correlation matrix for DataFrame.
    
    Args:
        df: DataFrame with numeric columns
        
    Returns:
        Correlation matrix
    """
    return df.corr()


def plot_time_series(series: pd.Series, title: str = "Time Series", 
                     ylabel: str = "Value", show_trend: bool = False) -> None:
    """
    Plot time series data.
    
    Args:
        series: Time series data
        title: Plot title
        ylabel: Y-axis label
        show_trend: Whether to show trend line
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(series.index, series.values, linewidth=2, label='Data')
    
    if show_trend:
        slope, intercept, r_squared = detect_trend(series)
        x_numeric = np.arange(len(series))
        trend_line = slope * x_numeric + intercept
        ax.plot(series.index, trend_line, 'r--', linewidth=2, 
               label=f'Trend (R² = {r_squared:.3f})')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def plot_multiple_series(df: pd.DataFrame, title: str = "Multiple Time Series",
                        normalize: bool = False) -> None:
    """
    Plot multiple time series on the same chart.
    
    Args:
        df: DataFrame with multiple columns
        title: Plot title
        normalize: Whether to normalize series to 100 at start
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    plot_df = df.copy()
    
    if normalize:
        # Normalize to 100 at first valid value
        for col in plot_df.columns:
            first_valid = plot_df[col].first_valid_index()
            if first_valid is not None:
                plot_df[col] = (plot_df[col] / plot_df.loc[first_valid, col]) * 100
    
    for col in plot_df.columns:
        ax.plot(plot_df.index, plot_df[col], linewidth=2, label=col)
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Normalized Value (Base = 100)' if normalize else 'Value', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame, title: str = "Correlation Matrix") -> None:
    """
    Plot correlation heatmap.
    
    Args:
        df: DataFrame with numeric columns
        title: Plot title
    """
    corr_matrix = calculate_correlation_matrix(df)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
               center=0, square=True, linewidths=1, ax=ax,
               cbar_kws={"shrink": 0.8})
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def perform_stationarity_test(series: pd.Series) -> dict:
    """
    Perform Augmented Dickey-Fuller test for stationarity.
    
    Args:
        series: Time series data
        
    Returns:
        Dictionary with test results
    """
    try:
        from statsmodels.tsa.stattools import adfuller
        
        # Remove NaN values
        clean_series = series.dropna()
        
        if len(clean_series) < 3:
            return {'error': 'Not enough data points'}
        
        result = adfuller(clean_series)
        
        return {
            'test_statistic': result[0],
            'p_value': result[1],
            'n_lags': result[2],
            'n_obs': result[3],
            'critical_values': result[4],
            'is_stationary': result[1] < 0.05  # 5% significance level
        }
        
    except ImportError:
        return {'error': 'statsmodels package not found'}
    except Exception as e:
        return {'error': str(e)}


def calculate_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate comprehensive summary statistics.
    
    Args:
        df: DataFrame with numeric columns
        
    Returns:
        DataFrame with summary statistics
    """
    summary = df.describe().T
    summary['median'] = df.median()
    summary['skewness'] = df.skew()
    summary['kurtosis'] = df.kurtosis()
    
    return summary


# Example usage
if __name__ == "__main__":
    # Create sample data
    dates = pd.date_range(start='2020-01-01', periods=50, freq='M')
    data = pd.DataFrame({
        'gdp': np.random.randn(50).cumsum() + 100,
        'inflation': np.random.randn(50) * 2 + 2,
    }, index=dates)
    
    print("Summary Statistics:")
    print(calculate_summary_statistics(data))
    
    print("\nCorrelation Matrix:")
    print(calculate_correlation_matrix(data))
    
    print("\nGrowth Rate (GDP):")
    print(calculate_growth_rate(data['gdp']).tail())
