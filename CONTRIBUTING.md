# Contributing to Economic Analysis Repository

Thank you for your interest in contributing to this project! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (Python version, OS, etc.)
- Any relevant error messages

### Suggesting Enhancements

We welcome suggestions for new features or improvements! Please open an issue with:
- A clear description of the enhancement
- Use cases and benefits
- Any implementation ideas you have

### Contributing Code

1. **Fork the repository** and create a new branch for your feature or bugfix
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear, readable code
   - Follow PEP 8 style guidelines for Python code
   - Add docstrings to functions and classes
   - Include type hints where appropriate

3. **Test your changes**
   - Ensure your code works as expected
   - Check that existing functionality still works
   - Add examples or documentation if needed

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

5. **Push to your fork** and submit a pull request
   ```bash
   git push origin feature/your-feature-name
   ```

### Adding New Data Sources

If you'd like to add support for a new economic data API:

1. Add the new fetcher class to `src/api_utils.py`
2. Follow the existing pattern (similar to `FREDDataFetcher` or `WorldBankDataFetcher`)
3. Include comprehensive docstrings with examples
4. Update the README with information about the new source
5. Consider adding a notebook example

### Improving Notebooks

Contributions to the example notebooks are welcome:
- Fix errors or improve explanations
- Add new analysis examples
- Improve visualizations
- Add new notebooks for different use cases

### Documentation

Help us improve documentation:
- Fix typos or clarify explanations
- Add more usage examples
- Improve docstrings in the code
- Update the README with new information

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions, classes, and modules
- Include type hints for function parameters and return values
- Keep functions focused and not too long

## Testing

While we don't currently have automated tests, please:
- Test your code manually before submitting
- Ensure notebooks run without errors
- Verify that API calls work correctly
- Check that visualizations display properly

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Ask in your pull request
- Reach out to the maintainers

Thank you for contributing to make this project better!
