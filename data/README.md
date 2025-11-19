# Data Directory

This directory is for storing sample or downloaded economic data files.

## Usage

You can use this directory to:
- Store CSV files downloaded from APIs
- Cache data for offline analysis
- Save processed datasets
- Store example data files for demonstration

## Example Data Files

You can download sample economic data from:
- [FRED Data Downloads](https://fred.stlouisfed.org/)
- [World Bank Data](https://data.worldbank.org/)
- [OECD Data](https://data.oecd.org/)
- [IMF Data](https://www.imf.org/en/Data)

## File Formats

Common formats for economic data:
- `.csv` - Comma-separated values (most common)
- `.xlsx` - Excel files
- `.json` - JSON format for API responses
- `.pkl` - Pickled pandas DataFrames

## Note

By default, data files are not tracked in git (see `.gitignore`). 
If you want to include specific data files in the repository, you can force add them:

```bash
git add -f data/your_file.csv
```
