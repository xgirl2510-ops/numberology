# INPUT & OUTPUT Documentation - Numerology System

## 📥 INPUT (Dữ liệu đầu vào)

### Thông tin cần thiết:

```python
from numerology import Numerology

# INPUT: 3 thông tin bắt buộc
calc = Numerology(
    full_name="Nguyễn Thị Uyên Yên",    # 1. Họ tên đầy đủ
    birth_date="15/07/1990",             # 2. Ngày sinh (DD/MM/YYYY)
    language='vi'                        # 3. Ngôn ngữ
)
```

### Chi tiết INPUT:

| Tham số | Kiểu | Ví dụ | Bắt buộc | Mô tả |
|---------|------|-------|----------|-------|
| `full_name` | `str` | "Nguyễn Thị Uyên Yên" | ✅ | Họ tên đầy đủ |
| `birth_date` | `str` | "15/07/1990" | ✅ | Ngày/Tháng/Năm sinh |
| `language` | `str` | 'vi' | ⚠️ | Ngôn ngữ (30+ languages) |

---

## 📤 OUTPUT (Kết quả đầu ra)

Hệ thống có **3 mức độ OUTPUT:**

---

## 1️⃣ OUTPUT CƠ BẢN - Chỉ Số Đơn Lẻ

### Code:
```python
life_path = calc.life_path_number()
expression = calc.expression_number()
soul_urge = calc.soul_urge_number()
personality = calc.personality_number()
birthday = calc.birthday_number()
```

### OUTPUT:
```python
life_path:    5   # int - Life Path Number
expression:   7   # int - Expression Number
soul_urge:    3   # int - Soul Urge Number
personality:  22  # int - Personality Number (Master Number)
birthday:     6   # int - Birthday Number
```

**OUTPUT Type:** `int`

**Range:** 1-9 hoặc Master Numbers (11, 22, 33)

---

## 2️⃣ OUTPUT TRUNG BÌNH - Tất Cả Chỉ Số

### Code:
```python
data = calc.get_all_numbers()
```

### OUTPUT Structure:
```python
{
    'personal_info': {
        'original_name': 'Nguyễn Thị Uyên Yên',
        'full_name': 'NGUYEN THI UYEN YEN',
        'birth_date': '15/07/1990'
    },

    'core_numbers': {
        'life_path': 5,
        'expression': 7,
        'soul_urge': 3,
        'personality': 22,
        'birthday': 6
    },

    'secondary_numbers': {
        'maturity': 3,
        'balance': 5,
        'hidden_passion': 5,
        'subconscious_self': 9,
        'karmic_lessons': [2, 4, 7, 8]
    },

    'name_analysis': {
        'letter_frequency': {
            1: 2, 2: 1, 3: 2, 4: 0, 5: 5,
            6: 0, 7: 2, 8: 1, 9: 1
        },
        'missing_numbers': [4, 6],
        'has_karmic_debt': False,
        'karmic_debt_numbers': []
    },

    'life_cycles': {
        'pinnacles': {
            'first': {'number': 3, 'age_range': '0-31'},
            'second': {'number': 8, 'age_range': '31-40'},
            'third': {'number': 6, 'age_range': '40-49'},
            'fourth': {'number': 5, 'age_range': '49+'}
        },
        'challenges': {
            'first': {'number': 2, 'age_range': '0-31'},
            'second': {'number': 2, 'age_range': '31-40'},
            'third': {'number': 0, 'age_range': '40-49'},
            'fourth': {'number': 4, 'age_range': '49+'}
        }
    }
}
```

**OUTPUT Type:** `dict`

**Không có giải nghĩa** - chỉ có số

---

## 3️⃣ OUTPUT ĐẦY ĐỦ - Tất Cả Chỉ Số + Giải Nghĩa

### Code:
```python
data = calc.get_all_numbers_with_interpretations()
```

### OUTPUT Structure (with interpretations):

```python
{
    'personal_info': {
        'original_name': 'Nguyễn Thị Uyên Yên',
        'full_name': 'NGUYEN THI UYEN YEN',
        'birth_date': '15/07/1990'
    },

    'core_numbers': {
        'life_path': {
            'number': 5,
            'interpretation': {
                'title': 'Người Tìm Kiếm Tự Do - The Freedom Seeker',
                'keywords': ['Tự do', 'Phiêu lưu', 'Thay đổi', 'Linh hoạt'],
                'description': 'Bạn là người yêu thích tự do, thích khám phá và trải nghiệm những điều mới mẻ...',
                'strengths': [
                    'Thích ứng nhanh',
                    'Đa năng',
                    'Giao tiếp tốt',
                    'Năng động'
                ],
                'challenges': [
                    'Thiếu kiên nhẫn',
                    'Không kiên định',
                    'Dễ phân tâm'
                ],
                'career': [
                    'Du lịch',
                    'Truyền thông',
                    'Bán hàng',
                    'Marketing',
                    'Nhà báo'
                ]
            }
        },

        'expression': {
            'number': 7,
            'interpretation': {
                'title': 'Người Tìm Kiếm Chân Lý - The Seeker',
                'keywords': ['Trí tuệ', 'Tâm linh', 'Phân tích', 'Sâu sắc'],
                'description': 'Bạn có tài năng phân tích, nghiên cứu sâu...',
                'strengths': [
                    'Trí tuệ cao',
                    'Phân tích sắc bén',
                    'Tư duy logic',
                    'Trực giác mạnh'
                ],
                'challenges': [
                    'Quá kín đáo',
                    'Khó tiếp cận',
                    'Có xu hướng cô lập'
                ],
                'career': [
                    'Nghiên cứu',
                    'Giáo dục',
                    'Tâm linh',
                    'Khoa học',
                    'Phân tích dữ liệu'
                ]
            }
        },

        'soul_urge': {
            'number': 3,
            'interpretation': {
                'title': 'Người Giao Tiếp - The Communicator',
                'keywords': ['Sáng tạo', 'Biểu đạt', 'Giao tiếp', 'Vui vẻ'],
                'description': 'Bên trong, bạn khao khát sáng tạo và biểu đạt bản thân...',
                'strengths': [
                    'Sáng tạo',
                    'Giao tiếp tốt',
                    'Lạc quan',
                    'Truyền cảm hứng'
                ],
                'challenges': [
                    'Dễ phân tâm',
                    'Thiếu tập trung',
                    'Quá nhạy cảm'
                ],
                'career': [
                    'Nghệ thuật',
                    'Viết lách',
                    'Diễn xuất',
                    'Thiết kế'
                ]
            }
        },

        'personality': {
            'number': 22,
            'interpretation': {
                'title': 'Người Xây Dựng Vĩ Đại - Master Builder',
                'keywords': ['Xây dựng', 'Tầm nhìn', 'Thực tế', 'Quyền lực'],
                'description': 'Người khác nhìn bạn như một người có tầm ảnh hưởng lớn, khả năng biến ước mơ thành hiện thực...',
                'strengths': [
                    'Tầm nhìn xa',
                    'Thực tế',
                    'Xây dựng hệ thống',
                    'Lãnh đạo mạnh mẽ'
                ],
                'challenges': [
                    'Áp lực cao',
                    'Mất cân bằng',
                    'Quá tham vọng'
                ],
                'career': [
                    'Doanh nhân',
                    'Kiến trúc sư',
                    'Quản lý dự án lớn',
                    'Chính trị'
                ]
            }
        },

        'birthday': {
            'number': 6,
            'interpretation': {
                'title': 'Người Chăm Sóc - The Nurturer',
                'description': 'Tài năng đặc biệt về chăm sóc, hỗ trợ người khác...'
            }
        }
    },

    'secondary_numbers': {
        'maturity': 3,
        'balance': 5,
        'hidden_passion': 5,
        'subconscious_self': 9,
        'karmic_lessons': [2, 4, 7, 8]
    },

    'name_analysis': { ... },
    'life_cycles': { ... }
}
```

**OUTPUT Type:** `dict`

**Có đầy đủ giải nghĩa** cho mỗi số

---

## 📊 SO SÁNH 3 MỨC OUTPUT

| Mức độ | Method | Có số? | Có giải nghĩa? | Use case |
|--------|--------|--------|----------------|----------|
| **Cơ bản** | `calc.life_path_number()` | ✅ | ❌ | Lấy 1 số cụ thể |
| **Trung bình** | `calc.get_all_numbers()` | ✅ | ❌ | Lấy tất cả số |
| **Đầy đủ** | `calc.get_all_numbers_with_interpretations()` | ✅ | ✅ | Báo cáo đầy đủ |

---

## 🔍 CHI TIẾT QUY TRÌNH XỬ LÝ

### INPUT → PROCESSING → OUTPUT

```
INPUT:
  full_name: "Nguyễn Thị Uyên Yên"
  birth_date: "15/07/1990"
  language: 'vi'
       ↓

PROCESSING:
  1. Normalize name
     → "NGUYEN THI UYEN YEN"

  2. Split components
     → ["NGUYEN", "THI", "UYEN", "YEN"]

  3. Process each component with Y detection

     NGUYEN:
     - N(5) + G(7) + U(3-vowel) + Y(1-consonant) + E(5-vowel) + N(5)
     - Vowels only:     U(3) + E(5) = 8
     - Consonants only: N(5) + G(7) + Y(1) + N(5) = 18 → 9
     - All letters:     5+7+3+1+5+5 = 26 → 8

     THI:
     - T(2) + H(8) + I(9-vowel)
     - Vowels only:     I(9) = 9
     - Consonants only: T(2) + H(8) = 10 → 1
     - All letters:     2+8+9 = 19 → 1

     UYEN:
     - U(3-vowel) + Y(1-consonant) + E(5-vowel) + N(5)
     - Vowels only:     U(3) + E(5) = 8
     - Consonants only: Y(1) + N(5) = 6
     - All letters:     3+1+5+5 = 14 → 5

     YEN:
     - Y(1-consonant) + E(5-vowel) + N(5)
     - Vowels only:     E(5) = 5
     - Consonants only: Y(1) + N(5) = 6
     - All letters:     1+5+5 = 11 (Master Number)

  4. Sum and reduce
     Expression:  8 + 1 + 5 + 11 = 25 → 7
     Soul Urge:   8 + 9 + 8 + 5 = 30 → 3
     Personality: 9 + 1 + 6 + 6 = 22 (Master Number)

  5. Calculate Life Path from birth_date
     15/07/1990
     → Day:   15 → 6
     → Month: 7
     → Year:  1990 → 1
     → Total: 6+7+1 = 14 → 5
       ↓

OUTPUT (Level 1 - Basic):
  life_path: 5
  expression: 7
  soul_urge: 3
  personality: 22
  birthday: 6

OUTPUT (Level 2 - All numbers):
  { core_numbers: {...}, secondary_numbers: {...}, ... }

OUTPUT (Level 3 - With interpretations):
  {
    core_numbers: {
      life_path: {
        number: 5,
        interpretation: {...}
      },
      ...
    }
  }
```

---

## 💡 VÍ DỤ SỬ DỤNG THỰC TẾ

### Ví dụ 1: Lấy chỉ số cơ bản
```python
from numerology import Numerology

calc = Numerology("Nguyễn Văn A", "01/01/1990", language='vi')

print(f"Life Path: {calc.life_path_number()}")
print(f"Expression: {calc.expression_number()}")
```

**OUTPUT:**
```
Life Path: 3
Expression: 9
```

---

### Ví dụ 2: Lấy tất cả số (không giải nghĩa)
```python
calc = Numerology("MARY JOHNSON", "15/06/1990", language='en')
data = calc.get_all_numbers()

# Truy cập core numbers
print(data['core_numbers'])
```

**OUTPUT:**
```python
{
    'life_path': 4,
    'expression': 6,
    'soul_urge': 11,  # Master Number
    'personality': 4,
    'birthday': 6
}
```

---

### Ví dụ 3: Lấy đầy đủ với giải nghĩa
```python
calc = Numerology("John Doe", "10/05/1985", language='en')
data = calc.get_all_numbers_with_interpretations()

# Truy cập interpretation
lp = data['core_numbers']['life_path']
print(f"Number: {lp['number']}")
print(f"Title: {lp['interpretation']['title']}")
print(f"Description: {lp['interpretation']['description'][:100]}...")
print(f"Strengths: {lp['interpretation']['strengths']}")
print(f"Career: {lp['interpretation']['career']}")
```

**OUTPUT:**
```
Number: 1
Title: Người Lãnh Đạo - The Leader
Description: Bạn sinh ra để lãnh đạo, tiên phong và độc lập. Bạn có khả năng tự tin, quyết đoán...
Strengths: ['Độc lập', 'Tự tin', 'Quyết đoán', 'Tiên phong', 'Sáng tạo']
Career: ['Doanh nhân', 'Quản lý', 'Lãnh đạo', 'Khởi nghiệp', 'Giám đốc']
```

---

## 📋 TÓM TẮT

### INPUT (3 thông tin):
1. ✅ Họ tên đầy đủ (`str`)
2. ✅ Ngày sinh DD/MM/YYYY (`str`)
3. ✅ Ngôn ngữ - language code (`str`)

### OUTPUT (3 levels):
1. 🔢 **Basic**: Single number (`int`) - Một số từ 1-9 hoặc 11, 22, 33
2. 📊 **Medium**: All numbers (`dict`) - Tất cả số, không giải nghĩa
3. 📖 **Full**: All numbers + interpretations (`dict`) - Đầy đủ số + giải nghĩa

### PROCESSING:
- Name normalization (bỏ dấu, uppercase)
- Component splitting (tách từng từ)
- Dynamic Y detection (Y động theo vị trí, ngôn ngữ)
- Number calculation (tính toán theo Pythagorean)
- Master Number preservation (giữ 11, 22, 33)
- Interpretation lookup (tra giải nghĩa)

---

## ✅ KẾT LUẬN

**INPUT:** 3 thông tin đơn giản (Tên, Ngày sinh, Ngôn ngữ)

**OUTPUT:** Từ đơn giản (1 số) đến phức tạp (toàn bộ profile + giải nghĩa)

**Linh hoạt:** 3 mức độ output cho 3 use case khác nhau!
