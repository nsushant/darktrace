# Contributing to Darktrace

Thank you for your interest in contributing to the Darktrace package! This document provides guidelines for contributors to ensure a smooth and collaborative development process.

## Getting Started

### Prerequisites

- Python 3.x
- Familiarity with astrophysical simulations and particle tagging concepts
- Experience with scientific Python packages (numpy, pandas, matplotlib)

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/darktrace.git
   cd darktrace
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install numpy pandas matplotlib seaborn
   pip install pynbody tangos darklight  # Optional astrophysics packages
   ```

4. **Install in development mode**
   ```bash
   pip install -e .
   ```

## Code Style and Standards

### Python Style Guidelines

- Follow PEP 8 style guidelines
- Use 4 spaces for indentation (not tabs)
- Keep lines under 100 characters when possible
- Use descriptive variable and function names

### Documentation Standards

- All public functions must have docstrings
- Use Google-style or NumPy-style docstring format
- Include parameter types, descriptions, and return values
- Add usage examples for complex functions

Example:
```python
def example_function(param1: str, param2: int, param3: float = 0.1) -> pd.DataFrame:
    """
    Brief description of the function's purpose.
    
    Args:
        param1: Description of the first parameter
        param2: Description of the second parameter  
        param3: Description of the third parameter with default value
        
    Returns:
        DataFrame containing the results
        
    Raises:
        ValueError: If input parameters are invalid
        FileNotFoundError: If required files are missing
        
    Example:
        >>> result = example_function("test", 42, param3=0.5)
        >>> print(result.head())
    """
    pass
```

### Configuration System

- Always use the centralized configuration system (`config.py`)
- Never hardcode paths in functions
- Use `config.get_path()` for all file paths
- Add new configuration parameters to `config.json`

Good practice:
```python
from config import config

def my_function():
    pynbody_path = config.get_path('pynbody_path')
    # Use path safely
```

Bad practice:
```python
def my_function():
    pynbody_path = "/hardcoded/path/to/data"  # NEVER do this
```

## Testing

### Running Tests

Before submitting a pull request, run all tests:

```bash
python test.py
```

### Writing Tests

- Add tests for new functionality
- Test both success and failure cases
- Include edge cases and boundary conditions
- Use meaningful test names

### Test Data

- Use small, manageable test datasets
- Don't commit large simulation files
- Use mock data when appropriate
- Document test data requirements

## Pull Request Process

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Your Changes

- Write clean, well-documented code
- Follow the style guidelines
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run the test suite
python test.py

# Run linting if available
# flake8 .  # or your preferred linter
```

### 4. Submit Your Pull Request

- Push your branch to your fork
- Create a pull request with a clear title and description
- Link to any relevant issues
- Describe your changes and their purpose

### 5. Code Review

- Respond to review comments promptly
- Make requested changes
- Keep the conversation focused and professional
- Ensure all tests pass before merge

## Types of Contributions

### Bug Fixes

- Clearly describe the bug and its impact
- Include steps to reproduce the issue
- Provide a minimal example if possible
- Explain how your fix resolves the issue

### New Features

- Open an issue first to discuss the feature
- Clearly describe the feature's purpose and use case
- Consider backwards compatibility
- Include comprehensive documentation

### Documentation Improvements

- Fix typos and grammatical errors
- Improve clarity and readability
- Add missing examples
- Update outdated information

### Performance Improvements

- Benchmark before and after changes
- Measure performance gains
- Consider memory usage impact
- Document trade-offs

## Release Process

### Version Numbers

- Follow semantic versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking changes
- MINOR: New features (backwards compatible)
- PATCH: Bug fixes (backwards compatible)

### Release Notes

- Document all changes since last release
- Categorize changes (Added, Fixed, Changed, Deprecated)
- Include migration instructions for breaking changes

## Community Guidelines

### Communication

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

### Code of Conduct

- Be inclusive and welcoming
- Respect different viewpoints and experiences
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Help

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and general discussion
- **Documentation**: Check existing documentation and examples
- **Examples**: Look at existing code for patterns and best practices

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT license as the project itself.

---

Thank you for contributing to Darktrace! Your contributions help make this package better for the entire astrophysics community.