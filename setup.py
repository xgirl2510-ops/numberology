"""
Setup script for numerology library
"""
from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="numerology-ar",
    version="1.0.0",
    author="Claude Code",
    author_email="noreply@anthropic.com",
    description="Advanced Numerology library with 30+ language support and dynamic Y processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/numerology-ar",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Natural Language :: Vietnamese",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Core dependencies - empty for now, googletrans is optional
    ],
    extras_require={
        "translate": [
            "googletrans==4.0.0rc1",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
    },
    keywords=[
        "numerology",
        "pythagorean",
        "life path number",
        "expression number",
        "soul urge",
        "personality number",
        "vietnamese",
        "multilingual",
        "thần số học",
    ],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/numerology-ar/issues",
        "Source": "https://github.com/yourusername/numerology-ar",
        "Documentation": "https://github.com/yourusername/numerology-ar/blob/main/README.md",
    },
    include_package_data=True,
    zip_safe=False,
)
