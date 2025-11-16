#!/usr/bin/env python3
"""
Simple example script demonstrating the colab_and_economics toolkit.

This script shows how to:
1. Create sample economic data
2. Perform basic analysis
3. Create visualizations
4. Calculate statistics

Run this script to verify your installation is working correctly.
"""

import sys
import os

# Add src to path if running from root directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data_fetchers import create_sample_data
from analysis_utils import (
    calculate_growth_rate,
    calculate_moving_average,
    calculate_summary_statistics,
    calculate_correlation_matrix
)

def main():
    print("=" * 60)
    print("Colab and Economics - Example Script")
    print("=" * 60)
    
    # Step 1: Create sample data
    print("\n1. Creating sample economic data...")
    df = create_sample_data(n_periods=100, start_date='2015-01-01')
    print(f"   ✓ Created dataset with {len(df)} observations")
    print(f"   ✓ Variables: {', '.join(df.columns)}")
    
    # Step 2: Display basic info
    print("\n2. Data overview:")
    print(f"   Date range: {df.index.min().date()} to {df.index.max().date()}")
    print(f"   Shape: {df.shape}")
    
    # Step 3: Calculate summary statistics
    print("\n3. Summary statistics:")
    stats = calculate_summary_statistics(df)
    print(stats[['mean', 'std', 'min', 'max']].round(2))
    
    # Step 4: Calculate growth rates
    print("\n4. Growth rates (year-over-year):")
    gdp_growth = calculate_growth_rate(df['gdp'], periods=12)
    print(f"   Mean GDP growth: {gdp_growth.mean():.2f}%")
    print(f"   Std GDP growth: {gdp_growth.std():.2f}%")
    
    # Step 5: Calculate moving averages
    print("\n5. Moving averages:")
    ma_6 = calculate_moving_average(df['unemployment_rate'], window=6)
    ma_12 = calculate_moving_average(df['unemployment_rate'], window=12)
    print(f"   6-month MA (unemployment): {ma_6.iloc[-1]:.2f}%")
    print(f"   12-month MA (unemployment): {ma_12.iloc[-1]:.2f}%")
    
    # Step 6: Correlation analysis
    print("\n6. Correlation matrix:")
    corr = calculate_correlation_matrix(df)
    print(corr.round(3))
    
    # Step 7: Recommendations
    print("\n" + "=" * 60)
    print("✅ Installation verified successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Open notebooks/01_introduction_to_economic_analysis.ipynb")
    print("2. Try the Jupyter notebooks in Google Colab")
    print("3. Get a FRED API key for real economic data")
    print("4. Explore the analysis_utils and data_fetchers modules")
    print("\nHappy analyzing! 📈")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have installed all dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
