# Quick Start Guide - Numerology Library

## 🚀 Installation

### Development Installation (Recommended for now)

```bash
cd numberology-ar

# Install in editable/development mode
pip install -e .
```

### Verify Installation

```bash
# Test import
python3 -c "from numerology import Numerology; print('✅ Installation successful!')"
```

---

## 📖 Basic Usage

### Example 1: Calculate Core Numbers

```python
from numerology import Numerology

# Create instance with Vietnamese name
calc = Numerology(
    full_name="Nguyễn Thị Uyên Yên",
    birth_date="15/07/1990",
    language='vi'
)

# Get core numbers
print(f"Life Path: {calc.life_path_number()}")        # 5
print(f"Expression: {calc.expression_number()}")      # 7
print(f"Soul Urge: {calc.soul_urge_number()}")        # 3
print(f"Personality: {calc.personality_number()}")    # 22 (Master Number)
print(f"Birthday: {calc.birthday_number()}")          # 6
```

### Example 2: English Name

```python
calc = Numerology("MARY JOHNSON", "02/09/1990", language='en')

print(f"Life Path: {calc.life_path_number()}")
print(f"Soul Urge: {calc.soul_urge_number()}")        # 11 (Master Number)
print(f"Personality: {calc.personality_number()}")
```

### Example 3: Get All Numbers (No Interpretations)

```python
calc = Numerology("John Doe", "15/06/1990", language='en')
data = calc.get_all_numbers()

print(data['core_numbers'])
# {
#   'life_path': 4,
#   'expression': 8,
#   'soul_urge': 6,
#   'personality': 2,
#   'birthday': 6
# }

print(data['secondary_numbers'])
# {
#   'maturity': 3,
#   'balance': 1,
#   'hidden_passion': 5,
#   'subconscious_self': 9
# }
```

### Example 4: Get All Numbers WITH Interpretations

```python
calc = Numerology("John Doe", "15/06/1990", language='en')
data = calc.get_all_numbers_with_interpretations()

# Access Life Path interpretation
lp = data['core_numbers']['life_path']
print(f"Number: {lp['number']}")
print(f"Title: {lp['interpretation']['title']}")
print(f"Description: {lp['interpretation']['description']}")
print(f"Strengths: {lp['interpretation']['strengths']}")
print(f"Challenges: {lp['interpretation']['challenges']}")
print(f"Career: {lp['interpretation']['career']}")
```

---

## 🌍 Supported Languages

The library supports 30+ languages with intelligent Y vowel/consonant detection:

```python
# Vietnamese
calc = Numerology("Nguyễn Văn A", "15/07/1990", language='vi')

# English
calc = Numerology("John Smith", "15/07/1990", language='en')

# French
calc = Numerology("Jean Dupont", "15/07/1990", language='fr')

# Spanish
calc = Numerology("Juan García", "15/07/1990", language='es')

# And 26 more languages...
```

**Supported languages:**
vi, en, fr, es, de, it, pt, ru, uk, pl, el, tr, ar, hi, ja, ko, zh, th, tl, id, ms, sw, zu, yo, wo, ha, ig, so, am, and more.

---

## 📊 Available Numbers

### Core Numbers (Most Important)
- **Life Path Number**: Your life's purpose and direction
- **Expression Number**: Your natural talents and abilities
- **Soul Urge Number**: Your inner desires and motivations
- **Personality Number**: How others perceive you
- **Birthday Number**: Special talents from birth day

### Secondary Numbers
- **Maturity Number**: What you're moving toward
- **Balance Number**: How you handle challenges
- **Hidden Passion Number**: Your strongest desire
- **Subconscious Self**: How you react to situations
- **Karmic Lesson Numbers**: Areas to develop

### Life Cycles
- **Pinnacle Numbers**: 4 major life cycles
- **Challenge Numbers**: 4 major challenges

---

## 🔢 Master Numbers

The library properly handles Master Numbers (11, 22, 33):

```python
calc = Numerology("Test Name", "08/06/1988", language='en')
life_path = calc.life_path_number()
# Returns: 22 (Master Number preserved)
```

Master Numbers are NOT reduced to single digits and have special meanings:
- **11**: Master Intuitive - Spiritual messenger
- **22**: Master Builder - Turning dreams into reality
- **33**: Master Teacher - Teaching with compassion

---

## 🎯 Key Features

### 1. Name Component Reduction Method
```python
# Each name component is reduced separately
# "NGUYEN THI UYEN YEN"
# → NGUYEN: 26 → 8
# → THI: 19 → 1
# → UYEN: 14 → 5
# → YEN: 11 (Master Number)
# → Total: 8+1+5+11 = 25 → 7
```

### 2. Dynamic Y Processing
```python
# Y can be vowel or consonant depending on position and language

# English: MARY
# Y at end after R → VOWEL (Y=7)
# Soul Urge counts: A(1) + Y(7) = 8

# Vietnamese: YEN
# Y at start before E → CONSONANT (Y=1)
# Personality counts: Y(1) + N(5) = 6
```

### 3. Vietnamese Diacritics Auto-removal
```python
# Automatic handling of Vietnamese diacritics
calc = Numerology("Nguyễn Văn Á", "01/01/1990", language='vi')
# Automatically converts to: NGUYEN VAN A
```

---

## 📚 Documentation Files

- **README.md**: Complete library documentation
- **INSTALLATION.md**: Detailed installation guide
- **CHANGELOG.md**: Version history
- **QUICK_START.md**: This file
- **CACH_TINH_LIFE_PATH.md**: Life Path calculation method (Vietnamese)
- **CACH_TINH_EXPRESSION_NUMBER.md**: Expression Number calculation
- **CACH_TINH_SOUL_URGE_PERSONALITY.md**: Soul Urge & Personality calculation
- **QUY_TAC_Y_TAT_CA_NGON_NGU.md**: Y rules for all 30 languages
- **FLOW_XU_LY_Y.md**: Y processing flow documentation

---

## 🧪 Testing

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=numerology --cov-report=html

# Run specific test
pytest tests/test_core.py -v
```

---

## 💡 Tips

1. **Always specify language** for accurate Y processing:
   ```python
   calc = Numerology("Name", "DD/MM/YYYY", language='vi')  # ✅ Good
   ```

2. **Master Numbers are special**:
   - If you get 11, 22, or 33, they won't be reduced
   - These have powerful meanings

3. **Name format**:
   - Use full name: "FIRST MIDDLE LAST"
   - System automatically splits by spaces
   - Each component is reduced separately

4. **Date format**:
   - Use "DD/MM/YYYY" format
   - Example: "15/07/1990"

---

## 🆘 Troubleshooting

### Import Error
```python
# ❌ Wrong - trying to import from old file
from numerology import Numerology  # If you have old numerology.py

# ✅ Correct - import from package
from numerology import Numerology
```

### Reinstall if needed
```bash
pip uninstall numerology-ar
pip install -e .
```

### Test installation
```bash
python3 -c "from numerology import Numerology; print(Numerology.__name__)"
# Should print: Numerology
```

---

## 📞 Support

- **Documentation**: See README.md
- **Issues**: GitHub Issues (when repository is set up)
- **Examples**: See tests/test_core.py for more examples

---

Happy numerology calculations! 🎉
