# Installation Guide - Numerology Library

## Quick Installation

### Option 1: Install from source (Development)

```bash
# Clone or download the repository
cd numberology-ar

# Install in development mode
pip install -e .

# Or install with optional translation support
pip install -e ".[translate]"

# Or install with dev dependencies
pip install -e ".[dev]"
```

### Option 2: Install from wheel (Production)

```bash
# Build the package first
python -m build

# Install the built wheel
pip install dist/numerology_ar-1.0.0-py3-none-any.whl
```

### Option 3: Install from PyPI (When published)

```bash
# Once published to PyPI
pip install numerology-ar

# With optional translation support
pip install numerology-ar[translate]
```

---

## Building the Package

### Prerequisites

```bash
# Install build tools
pip install build twine
```

### Build wheel and source distribution

```bash
# Clean old builds (if any)
rm -rf build/ dist/ *.egg-info

# Build the package
python -m build

# This creates:
# - dist/numerology_ar-1.0.0-py3-none-any.whl (wheel)
# - dist/numerology-ar-1.0.0.tar.gz (source)
```

### Verify the build

```bash
# Check the package contents
unzip -l dist/numerology_ar-1.0.0-py3-none-any.whl

# Or check with twine
twine check dist/*
```

---

## Running Tests

### Install test dependencies

```bash
pip install -e ".[dev]"
```

### Run tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=numerology --cov-report=html

# Run specific test file
pytest tests/test_core.py

# Run with verbose output
pytest -v
```

---

## Development Setup

### 1. Clone and setup virtual environment

```bash
# Clone repository
cd numberology-ar

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev]"
```

### 2. Run code quality checks

```bash
# Format code with black
black numerology/ tests/

# Check with flake8
flake8 numerology/ tests/

# Type checking with mypy
mypy numerology/
```

### 3. Run tests

```bash
pytest -v --cov=numerology
```

---

## Usage After Installation

### Basic usage

```python
from numerology import Numerology

# Create instance
calc = Numerology("Nguyễn Văn A", "15/07/1990", language='vi')

# Get numbers
life_path = calc.life_path_number()
expression = calc.expression_number()
soul_urge = calc.soul_urge_number()

print(f"Life Path: {life_path}")
print(f"Expression: {expression}")
print(f"Soul Urge: {soul_urge}")
```

### With interpretations

```python
# Get all numbers with interpretations
data = calc.get_all_numbers_with_interpretations()

# Access specific interpretation
lp = data['core_numbers']['life_path']
print(f"Number: {lp['number']}")
print(f"Title: {lp['interpretation']['title']}")
print(f"Description: {lp['interpretation']['description']}")
```

---

## Troubleshooting

### Import error after installation

```python
# Make sure you're importing from the package
from numerology import Numerology  # ✅ Correct

# Not from the old files
from numerology import Numerology  # ❌ If you have old numerology.py file
```

### Clean installation

```bash
# Uninstall old version
pip uninstall numerology-ar

# Clean build artifacts
rm -rf build/ dist/ *.egg-info numerology.egg-info/

# Reinstall
pip install -e .
```

### Test import

```bash
# Test if package is properly installed
python -c "from numerology import Numerology; print(Numerology.__name__)"
# Should print: Numerology
```

---

## Publishing to PyPI (For maintainers)

### Test PyPI (first time)

```bash
# Build the package
python -m build

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ numerology-ar
```

### Production PyPI

```bash
# Build the package
python -m build

# Upload to PyPI
twine upload dist/*

# Install from PyPI
pip install numerology-ar
```

---

## System Requirements

- Python 3.7 or higher
- No required dependencies (googletrans is optional)
- Works on Windows, macOS, and Linux

---

## Support

For issues and questions:
- GitHub Issues: https://github.com/yourusername/numerology-ar/issues
- Documentation: README.md and docs/ folder
