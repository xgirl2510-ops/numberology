#!/usr/bin/env python3
"""
Demo: INPUT & OUTPUT của Numerology System
Ví dụ cụ thể: Phân tích "Nguyễn Thị Uyên Yên"
"""

from numerology import Numerology
import json

print("=" * 70)
print("DEMO: INPUT & OUTPUT CỦA HỆ THỐNG NUMEROLOGY")
print("=" * 70)

# ============================================================================
# INPUT - DỮ LIỆU ĐẦU VÀO
# ============================================================================

print("\n" + "=" * 70)
print("📥 INPUT (Dữ liệu đầu vào)")
print("=" * 70)

full_name = "Nguyễn Thị Uyên Yên"
birth_date = "15/07/1990"
language = 'vi'

print(f"""
INPUT cần thiết (3 thông tin):
  1. Họ tên đầy đủ: "{full_name}"
  2. Ngày sinh:      "{birth_date}"
  3. Ngôn ngữ:       '{language}'
""")

print("Tạo instance:")
print(f'  calc = Numerology("{full_name}", "{birth_date}", language="{language}")')

# Tạo instance
calc = Numerology(full_name, birth_date, language=language)

print("  ✅ Instance created successfully!")

# ============================================================================
# OUTPUT LEVEL 1 - CƠ BẢN: CHỈ SỐ ĐƠN LẺ
# ============================================================================

print("\n" + "=" * 70)
print("📤 OUTPUT LEVEL 1: CƠ BẢN - Chỉ Số Đơn Lẻ")
print("=" * 70)

print("""
Code:
  life_path = calc.life_path_number()
  expression = calc.expression_number()
  soul_urge = calc.soul_urge_number()
  personality = calc.personality_number()
  birthday = calc.birthday_number()
""")

life_path = calc.life_path_number()
expression = calc.expression_number()
soul_urge = calc.soul_urge_number()
personality = calc.personality_number()
birthday = calc.birthday_number()

print("OUTPUT:")
print(f"  life_path:    {life_path}   (int)")
print(f"  expression:   {expression}   (int)")
print(f"  soul_urge:    {soul_urge}   (int)")
print(f"  personality:  {personality}  (int) ← Master Number!")
print(f"  birthday:     {birthday}   (int)")

print("\n📊 OUTPUT Type: int")
print("📊 Range: 1-9 hoặc Master Numbers (11, 22, 33)")

# ============================================================================
# OUTPUT LEVEL 2 - TRUNG BÌNH: TẤT CẢ CHỈ SỐ
# ============================================================================

print("\n" + "=" * 70)
print("📤 OUTPUT LEVEL 2: TRUNG BÌNH - Tất Cả Chỉ Số (Không giải nghĩa)")
print("=" * 70)

print("""
Code:
  data = calc.get_all_numbers()
""")

data = calc.get_all_numbers()

print("OUTPUT Structure:")
print(f"  - personal_info:      {list(data['personal_info'].keys())}")
print(f"  - core_numbers:       {list(data['core_numbers'].keys())}")
print(f"  - secondary_numbers:  {list(data['secondary_numbers'].keys())}")
print(f"  - name_analysis:      {list(data['name_analysis'].keys())}")
print(f"  - life_cycles:        {list(data['life_cycles'].keys())}")

print("\n📊 Core Numbers:")
for key, value in data['core_numbers'].items():
    print(f"    {key:15s} = {value}")

print("\n📊 Secondary Numbers:")
for key, value in data['secondary_numbers'].items():
    print(f"    {key:20s} = {value}")

print("\n📊 OUTPUT Type: dict")
print("📊 Không có giải nghĩa - chỉ có số")

# ============================================================================
# OUTPUT LEVEL 3 - ĐẦY ĐỦ: TẤT CẢ CHỈ SỐ + GIẢI NGHĨA
# ============================================================================

print("\n" + "=" * 70)
print("📤 OUTPUT LEVEL 3: ĐẦY ĐỦ - Tất Cả + Giải Nghĩa")
print("=" * 70)

print("""
Code:
  data_full = calc.get_all_numbers_with_interpretations()
""")

data_full = calc.get_all_numbers_with_interpretations()

print("OUTPUT Structure:")
print("  ├─ personal_info")
print("  ├─ core_numbers")
print("  │   ├─ life_path")
print("  │   │   ├─ number: int")
print("  │   │   └─ interpretation: dict")
print("  │   │       ├─ title")
print("  │   │       ├─ keywords")
print("  │   │       ├─ description")
print("  │   │       ├─ strengths")
print("  │   │       ├─ challenges")
print("  │   │       └─ career")
print("  │   ├─ expression (same structure)")
print("  │   ├─ soul_urge (same structure)")
print("  │   ├─ personality (same structure)")
print("  │   └─ birthday (same structure)")
print("  ├─ secondary_numbers")
print("  ├─ name_analysis")
print("  └─ life_cycles")

# ============================================================================
# CHI TIẾT GIẢI NGHĨA
# ============================================================================

print("\n" + "=" * 70)
print("📖 CHI TIẾT GIẢI NGHĨA - VÍ DỤ: LIFE PATH NUMBER")
print("=" * 70)

lp = data_full['core_numbers']['life_path']

print(f"""
Life Path Number: {lp['number']}

Title:
  {lp['interpretation']['title']}

Keywords:
  {', '.join(lp['interpretation']['keywords'])}

Description:
  {lp['interpretation']['description'][:200]}...

Strengths:
""")
for strength in lp['interpretation']['strengths']:
    print(f"  • {strength}")

print("\nChallenges:")
for challenge in lp['interpretation']['challenges']:
    print(f"  • {challenge}")

print("\nCareer:")
for career in lp['interpretation']['career']:
    print(f"  • {career}")

# ============================================================================
# SO SÁNH 3 CORE NUMBERS
# ============================================================================

print("\n" + "=" * 70)
print("🔍 SO SÁNH 3 CORE NUMBERS QUAN TRỌNG")
print("=" * 70)

exp = data_full['core_numbers']['expression']
su = data_full['core_numbers']['soul_urge']
per = data_full['core_numbers']['personality']

print(f"""
┌─────────────────┬────────┬─────────────────────────────────────┐
│ Chỉ Số          │ Số     │ Ý Nghĩa                             │
├─────────────────┼────────┼─────────────────────────────────────┤
│ Life Path       │ {life_path:2d}     │ {lp['interpretation']['title'][:35]:35s} │
│                 │        │ Mục đích cuộc đời                   │
├─────────────────┼────────┼─────────────────────────────────────┤
│ Expression      │ {expression:2d}     │ {exp['interpretation']['title'][:35]:35s} │
│                 │        │ Tài năng bẩm sinh                   │
├─────────────────┼────────┼─────────────────────────────────────┤
│ Soul Urge       │ {soul_urge:2d}     │ {su['interpretation']['title'][:35]:35s} │
│                 │        │ Mong muốn nội tâm                   │
├─────────────────┼────────┼─────────────────────────────────────┤
│ Personality     │ {personality:2d}     │ {per['interpretation']['title'][:35]:35s} │
│                 │        │ Ấn tượng bên ngoài                  │
└─────────────────┴────────┴─────────────────────────────────────┘
""")

# ============================================================================
# GIẢI THÍCH Y PROCESSING
# ============================================================================

print("=" * 70)
print("🔧 QUY TRÌNH XỬ LÝ - Y VOWEL/CONSONANT DETECTION")
print("=" * 70)

print(f"""
INPUT Name: "{full_name}"
  ↓ Normalize & Uppercase
"NGUYEN THI UYEN YEN"
  ↓ Split components
["NGUYEN", "THI", "UYEN", "YEN"]
  ↓ Process each component

Component 1: NGUYEN
  N(5) + G(7) + U(3-vowel) + Y(1-consonant) + E(5-vowel) + N(5)

  → Y ở vị trí 3: U-[Y]-E (giữa 2 nguyên âm)
  → Y = PHỤ ÂM (số 1)

  Vowels only:     U(3) + E(5) = 8
  Consonants only: N(5) + G(7) + Y(1) + N(5) = 18 → 9
  All letters:     5+7+3+1+5+5 = 26 → 8

Component 2: THI
  T(2) + H(8) + I(9-vowel)

  Vowels only:     I(9) = 9
  Consonants only: T(2) + H(8) = 10 → 1
  All letters:     2+8+9 = 19 → 1

Component 3: UYEN
  U(3-vowel) + Y(1-consonant) + E(5-vowel) + N(5)

  → Y ở vị trí 1: U-[Y]-E (giữa 2 nguyên âm)
  → Y = PHỤ ÂM (số 1)

  Vowels only:     U(3) + E(5) = 8
  Consonants only: Y(1) + N(5) = 6
  All letters:     3+1+5+5 = 14 → 5

Component 4: YEN
  Y(1-consonant) + E(5-vowel) + N(5)

  → Y ở vị trí 0: —-[Y]-E (đầu từ + nguyên âm)
  → Y = PHỤ ÂM (số 1)

  Vowels only:     E(5) = 5
  Consonants only: Y(1) + N(5) = 6
  All letters:     1+5+5 = 11 (Master Number!)

Final Calculation:
  Expression:  8 + 1 + 5 + 11 = 25 → 7 ✅
  Soul Urge:   8 + 9 + 8 + 5  = 30 → 3 ✅
  Personality: 9 + 1 + 6 + 6  = 22 (Master Number!) ✅
""")

# ============================================================================
# TÓM TẮT
# ============================================================================

print("=" * 70)
print("📋 TÓM TẮT")
print("=" * 70)

print(f"""
INPUT (3 thông tin):
  ✅ Họ tên:    "{full_name}"
  ✅ Ngày sinh: "{birth_date}"
  ✅ Ngôn ngữ:  '{language}'

OUTPUT Level 1 - Basic (int):
  ✅ life_path:    {life_path}
  ✅ expression:   {expression}
  ✅ soul_urge:    {soul_urge}
  ✅ personality:  {personality}
  ✅ birthday:     {birthday}

OUTPUT Level 2 - All Numbers (dict):
  ✅ personal_info + core_numbers + secondary_numbers
  ✅ name_analysis + life_cycles
  ❌ Không có giải nghĩa

OUTPUT Level 3 - Full (dict):
  ✅ Tất cả như Level 2
  ✅ + Giải nghĩa đầy đủ cho mỗi số
  ✅ + Title, keywords, description, strengths, challenges, career

PROCESSING:
  ✅ Name normalization (bỏ dấu, uppercase)
  ✅ Component splitting (tách từng từ)
  ✅ Dynamic Y detection (Y động theo vị trí + ngôn ngữ)
  ✅ Name Component Reduction Method
  ✅ Master Number preservation (11, 22, 33)
""")

print("=" * 70)
print("✅ DEMO COMPLETE!")
print("=" * 70)

print("""
Để xem chi tiết OUTPUT Level 3 đầy đủ, uncomment dòng sau:
# print(json.dumps(data_full, indent=2, ensure_ascii=False))
""")

# Uncomment để xem full JSON output
# print("\n" + "=" * 70)
# print("FULL JSON OUTPUT (Level 3)")
# print("=" * 70)
# print(json.dumps(data_full, indent=2, ensure_ascii=False))
