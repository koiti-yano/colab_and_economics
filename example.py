"""
Example script demonstrating how to use the economic analysis utilities.

This script shows basic usage of the API fetchers and analysis functions.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Main function to demonstrate usage."""
    
    print("=" * 60)
    print("Economic Analysis Utilities - Example Usage")
    print("=" * 60)
    
    # Try to import and display available indicators
    print("\n1. Available Economic Indicators:")
    print("-" * 60)
    
    try:
        from api_utils import get_sample_economic_indicators
        indicators = get_sample_economic_indicators()
        
        print("\nFRED Indicators:")
        for name, code in list(indicators['FRED'].items())[:5]:
            print(f"  - {name}: {code}")
        
        print("\nWorld Bank Indicators:")
        for name, code in list(indicators['World Bank'].items())[:5]:
            print(f"  - {name}: {code}")
    except ImportError as e:
        print(f"\nNote: Dependencies not installed. Run: pip install -r requirements.txt")
        print(f"Error: {e}")
        print("\nShowing example indicator codes instead:")
        print("\nFRED Indicators:")
        print("  - GDP: GDP")
        print("  - UNRATE: UNRATE")
        print("  - CPIAUCSL: CPIAUCSL")
        print("\nWorld Bank Indicators:")
        print("  - GDP: NY.GDP.MKTP.CD")
        print("  - GDP_per_capita: NY.GDP.PCAP.CD")
    
    print("\n" + "=" * 60)
    print("To use these utilities:")
    print("-" * 60)
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Get a FRED API key: https://fred.stlouisfed.org/docs/api/api_key.html")
    print("3. Check the notebooks/ directory for detailed examples")
    print("4. Import utilities in your code:")
    print("   from src.api_utils import FREDDataFetcher")
    print("   from src.analysis_utils import calculate_growth_rate")
    print("=" * 60)
    
    # Example usage (commented out as it requires API key and data)
    print("\nExample code (requires FRED API key):")
    print("-" * 60)
    example_code = '''
from src.api_utils import FREDDataFetcher
from src.analysis_utils import calculate_growth_rate, plot_time_series

# Fetch data
fetcher = FREDDataFetcher(api_key='your_api_key_here')
gdp = fetcher.get_series('GDP', start_date='2010-01-01')

# Analyze
gdp_growth = calculate_growth_rate(gdp, periods=4)

# Visualize
plot_time_series(gdp_growth, title='GDP Growth Rate', ylabel='% Change')
'''
    print(example_code)
    print("=" * 60)

if __name__ == '__main__':
    main()
