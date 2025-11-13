"""
Numerology Library - Advanced Numerology calculations with 30+ language support

This library provides comprehensive numerology calculations including:
- Life Path Number
- Expression Number
- Soul Urge Number
- Personality Number
- Birthday Number
- And many more secondary numbers

Features:
- Support for 30+ languages with dynamic Y vowel/consonant detection
- Master Numbers (11, 22, 33) support
- Name Component Reduction Method
- Comprehensive interpretations for all numbers
"""

__version__ = "1.0.0"
__author__ = "Claude Code"
__license__ = "MIT"

from .core import Numerology
from .interpretations import get_interpretation

__all__ = [
    'Numerology',
    'get_interpretation',
]
