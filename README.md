# Thư Viện Numerology (Thần Số Học)

Thư viện Python tính toán các chỉ số Numerology kèm luận giải chi tiết.

## Tính Năng

✅ **Tính toán các chỉ số chính:**
- Life Path Number (Chỉ Số Đường Đời)
- Expression Number (Chỉ Số Biểu Đạt)
- Soul Urge Number (Chỉ Số Linh Hồn)
- Personality Number (Chỉ Số Nhân Cách)
- Birthday Number (Chỉ Số Ngày Sinh)

✅ **Các chỉ số phụ:**
- Maturity Number (Số Trưởng Thành)
- Balance Number (Số Cân Bằng)
- Hidden Passion Number (Đam Mê Ẩn)
- Subconscious Self (Tiềm Thức)
- Karmic Lesson Numbers (Bài Học Nghiệp)

✅ **Chu kỳ cuộc đời:**
- 4 Pinnacle Numbers (Đỉnh Cao)
- 4 Challenge Numbers (Thử Thách)

✅ **Luận giải chi tiết:**
- Mô tả đầy đủ cho từng số (1-9, 11, 22, 33)
- Điểm mạnh và thách thức
- Nghề nghiệp phù hợp
- Từ khóa đặc trưng

✅ **Hỗ trợ đa ngôn ngữ:**
- Tiếng Việt (tự động bỏ dấu)
- Các ngôn ngữ khác qua Google Translate API

## Cài Đặt

```bash
# Clone hoặc tải về thư mục
cd numberology-ar

# (Tùy chọn) Cài đặt Google Translate nếu cần dịch tên
pip install googletrans==4.0.0rc1
```

## Sử Dụng Cơ Bản

### 1. Tính toán các chỉ số

```python
from numerology import Numerology

# Khởi tạo
person = Numerology("JOHN SMITH", "15/06/1990", use_translation=False)

# Lấy các chỉ số riêng lẻ
life_path = person.life_path_number()
expression = person.expression_number()
soul_urge = person.soul_urge_number()

print(f"Life Path: {life_path}")
print(f"Expression: {expression}")
print(f"Soul Urge: {soul_urge}")
```

### 2. Lấy tất cả chỉ số (không có luận giải)

```python
data = person.get_all_numbers()
print(data['core_numbers'])
# {'life_path': 4, 'expression': 8, 'soul_urge': 6, ...}
```

### 3. Lấy tất cả chỉ số KÈM luận giải

```python
data = person.get_all_numbers_with_interpretations()

# Truy cập luận giải
lp = data['core_numbers']['life_path']
print(f"Số: {lp['number']}")
print(f"Tiêu đề: {lp['interpretation']['title']}")
print(f"Mô tả: {lp['interpretation']['description']}")
print(f"Điểm mạnh: {lp['interpretation']['strengths']}")
print(f"Nghề nghiệp: {lp['interpretation']['career']}")
```

### 4. Lấy luận giải cho một số cụ thể

```python
# Lấy luận giải Life Path số 1
interp = person.get_interpretation('life_path', 1)
print(interp['title'])        # "Người Lãnh Đạo - The Leader"
print(interp['keywords'])     # ['Độc lập', 'Tiên phong', ...]
print(interp['description'])  # Mô tả chi tiết
```

## Các Loại Luận Giải

Hệ thống hỗ trợ luận giải cho 5 loại chỉ số:

1. **`life_path`** - Chỉ Số Đường Đời
   - Tiêu đề, từ khóa, mô tả
   - Điểm mạnh, thách thức
   - Nghề nghiệp phù hợp

2. **`expression`** - Chỉ Số Biểu Đạt
   - Tiêu đề, mô tả
   - Tài năng đặc trưng

3. **`soul_urge`** - Chỉ Số Linh Hồn
   - Tiêu đề, mô tả
   - Khao khát nội tâm

4. **`personality`** - Chỉ Số Nhân Cách
   - Tiêu đề, mô tả
   - Ấn tượng ban đầu

5. **`birthday`** - Chỉ Số Ngày Sinh
   - Tài năng đặc biệt

## Demo

Chạy demo để xem luận giải chi tiết:

```bash
python3 demo_interpretations.py
```

Output mẫu:
```
======================================================================
                 CHỈ SỐ ĐƯỜNG ĐỜI (LIFE PATH NUMBER)
======================================================================

  🔢 Chỉ Số: 4
  📌 Người Xây Dựng - The Builder
  🏷️  Từ khóa: Thực tế, Kỷ luật, Tổ chức, Chăm chỉ, Ổn định
  📖 Mô tả: Bạn là người thực tế, có tổ chức và đáng tin cậy...
  💪 Điểm mạnh: Có tổ chức, Đáng tin cậy, Thực tế, Kiên trì
  ⚠️  Thách thức: Cứng nhắc, Thiếu linh hoạt, Quá nghiêm túc
  💼 Nghề nghiệp phù hợp: Kế toán, Kỹ sư, Kiến trúc sư, Quản lý dự án
```

## Test

Chạy test để kiểm tra:

```bash
# Test tính toán các chỉ số
python3 test_numerology.py

# Test hệ thống luận giải
python3 test_interpretations.py
```

## Cấu Trúc Dữ Liệu

### Output của `get_all_numbers_with_interpretations()`:

```python
{
    'personal_info': {
        'original_name': 'JOHN SMITH',
        'full_name': 'JOHN SMITH',
        'birth_date': '15/06/1990'
    },
    'core_numbers': {
        'life_path': {
            'number': 4,
            'interpretation': {
                'title': 'Người Xây Dựng - The Builder',
                'keywords': ['Thực tế', 'Kỷ luật', ...],
                'description': '...',
                'strengths': ['Có tổ chức', ...],
                'challenges': ['Cứng nhắc', ...],
                'career': ['Kế toán', 'Kỹ sư', ...]
            }
        },
        'expression': { ... },
        'soul_urge': { ... },
        'personality': { ... },
        'birthday': { ... }
    },
    'secondary_numbers': { ... },
    'name_analysis': { ... },
    'life_cycles': { ... }
}
```

## Master Numbers

Hệ thống hỗ trợ đầy đủ Master Numbers:
- **11** - Người Truyền Cảm Hứng
- **22** - Người Xây Dựng Vĩ Đại
- **33** - Người Thầy Tối Cao

## Files

- `numerology.py` - Thư viện chính, tính toán các chỉ số
- `interpretations.py` - Module chứa luận giải chi tiết
- `demo_interpretations.py` - Demo hiển thị luận giải
- `test_numerology.py` - Test cases cho tính toán
- `test_interpretations.py` - Test cases cho luận giải
- `requirements.txt` - Dependencies (optional)

## API Reference

### Class `Numerology`

```python
Numerology(full_name: str, birth_date: str, use_translation: bool = True)
```

**Các phương thức chính:**

- `life_path_number()` → int
- `expression_number()` → int
- `soul_urge_number()` → int
- `personality_number()` → int
- `birthday_number()` → int
- `maturity_number()` → int
- `balance_number()` → int
- `hidden_passion_number()` → int
- `subconscious_self()` → int
- `karmic_lesson_numbers()` → List[int]
- `pinnacle_numbers()` → Dict
- `challenge_numbers()` → Dict
- `get_all_numbers()` → Dict
- `get_all_numbers_with_interpretations()` → Dict
- `get_interpretation(category, number)` → Dict

## Ví Dụ Nâng Cao

### Phân tích profile đầy đủ

```python
from numerology import Numerology
import json

# Tạo profile
person = Numerology("Nguyễn Văn A", "15/06/1990", use_translation=False)

# Lấy dữ liệu đầy đủ
data = person.get_all_numbers_with_interpretations()

# In ra JSON đẹp
print(json.dumps(data, indent=2, ensure_ascii=False))

# Hoặc truy cập từng phần
lp = data['core_numbers']['life_path']
print(f"\nĐường đời của bạn: {lp['number']}")
print(f"Bạn là: {lp['interpretation']['title']}")
print(f"\nĐiểm mạnh:")
for strength in lp['interpretation']['strengths']:
    print(f"  • {strength}")
```

## License

MIT License

## Tác Giả

Phát triển bởi Claude Code
