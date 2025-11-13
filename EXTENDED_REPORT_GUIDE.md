# Extended Report Guide - AI-Friendly JSON Output

## 🎯 MỤC ĐÍCH

Method `get_extended_report()` tạo ra JSON output đầy đủ giống `example_full_report.json` để AI có thể luận giải dễ dàng.

---

## 📥 SỬ DỤNG

### Basic Usage:

```python
from numerology import Numerology

# Create instance
calc = Numerology("Nguyen Van A", "15/08/1990", language='vi')

# Get extended report
extended_report = calc.get_extended_report()

# Save to JSON
import json
with open('report.json', 'w', encoding='utf-8') as f:
    json.dump(extended_report, f, indent=2, ensure_ascii=False)
```

---

## 📤 OUTPUT STRUCTURE

### Top-level Keys:

```python
{
    'metadata': {...},              # Thông tin báo cáo
    'personal_information': {...},  # Thông tin cá nhân
    'core_numbers': {...},          # 5 chỉ số chính
    'secondary_numbers': {...},     # Các chỉ số phụ
    'name_analysis': {...},         # Phân tích tên
    'life_cycles': {...},           # Chu kỳ cuộc đời
    'summary': {...}                # Tổng kết
}
```

---

## 📊 CHI TIẾT CÁC SECTION

### 1. **metadata** (Thông tin báo cáo)

```json
{
    "metadata": {
        "report_type": "Numerology Complete Analysis",
        "generated_at": "2025-01-13T10:30:00.123456",
        "version": "1.0",
        "language": "Vietnamese"
    }
}
```

**Fields:**
- `report_type`: Loại báo cáo
- `generated_at`: Thời gian tạo (ISO format)
- `version`: Phiên bản
- `language`: Ngôn ngữ (Vietnamese/English)

---

### 2. **personal_information** (Thông tin cá nhân)

```json
{
    "personal_information": {
        "original_name": "Nguyen Van A",
        "normalized_name": "NGUYEN VAN A",
        "birth_date": "15/08/1990",
        "age": "35"
    }
}
```

**Fields:**
- `original_name`: Tên gốc
- `normalized_name`: Tên chuẩn hóa (uppercase, no diacritics)
- `birth_date`: Ngày sinh (DD/MM/YYYY)
- `age`: Tuổi (calculated)

---

### 3. **core_numbers** (5 Chỉ Số Chính)

```json
{
    "core_numbers": {
        "life_path": {
            "number": 6,
            "name": "Chỉ Số Đường Đời (Life Path Number)",
            "importance": "⭐⭐⭐⭐⭐ Quan trọng nhất",
            "meaning": "Mục đích và hướng đi của cuộc đời",
            "interpretation": {
                "title": "Người Nuôi Dưỡng - The Nurturer",
                "keywords": ["Trách nhiệm", "Chăm sóc", ...],
                "description": "...",
                "strengths": ["Có trách nhiệm", ...],
                "challenges": ["Kiểm soát quá mức", ...],
                "career": ["Giáo viên", "Y tế", ...]
            },
            "ai_context": "Đây là chỉ số quan trọng nhất..."
        },
        "expression": {...},
        "soul_urge": {...},
        "personality": {...},
        "birthday": {...}
    }
}
```

**Fields cho mỗi số:**
- `number`: Số (1-9 hoặc 11, 22, 33)
- `name`: Tên tiếng Việt và tiếng Anh
- `importance`: Mức độ quan trọng (⭐)
- `meaning`: Ý nghĩa tóm tắt
- `interpretation`: Giải nghĩa chi tiết từ interpretations.py
- `ai_context`: Hướng dẫn cho AI

---

### 4. **secondary_numbers** (Chỉ Số Phụ)

```json
{
    "secondary_numbers": {
        "maturity": {
            "number": 4,
            "name": "Số Trưởng Thành (Maturity Number)",
            "importance": "⭐⭐⭐ Khá quan trọng",
            "meaning": "Mục tiêu khi trưởng thành",
            "interpretation": {},
            "ai_context": "..."
        },
        "balance": {...},
        "hidden_passion": {...},
        "subconscious_self": {...}
    }
}
```

**Tương tự core_numbers nhưng ít quan trọng hơn**

---

### 5. **name_analysis** (Phân tích tên)

```json
{
    "name_analysis": {
        "cornerstone": {
            "letter": "N",
            "number": 5,
            "name": "Đá Góc (Cornerstone)",
            "importance": "⭐⭐ Tham khảo",
            "meaning": "Cách tiếp cận cơ hội",
            "interpretation": {...},
            "ai_context": "Chữ cái đầu tiên 'N'..."
        },
        "capstone": {...},
        "karmic_lessons": {
            "missing_numbers": [2, 6, 8, 9],
            "name": "Bài Học Nghiệp",
            "importance": "⭐⭐⭐ Khá quan trọng",
            "meaning": "Các bài học cần học",
            "interpretations": [
                {
                    "number": 2,
                    "interpretation": {
                        "title": "Bài Học Về Hợp Tác",
                        "description": "...",
                        "lesson": "..."
                    }
                }
            ],
            "ai_context": "..."
        }
    }
}
```

---

### 6. **life_cycles** (Chu kỳ cuộc đời)

```json
{
    "life_cycles": {
        "current_age": 35,
        "pinnacles": {
            "name": "4 Đỉnh Cao (Pinnacle Numbers)",
            "importance": "⭐⭐⭐⭐ Rất quan trọng",
            "meaning": "4 giai đoạn chính trong cuộc đời",
            "data": [
                {
                    "stage": "1",
                    "number": 5,
                    "age_range": "0 - 30",
                    "start_age": 0,
                    "end_age": 30,
                    "interpretation": {},
                    "is_current": false
                },
                {
                    "stage": "2",
                    "number": 7,
                    "age_range": "31 - 39",
                    "start_age": 31,
                    "end_age": 39,
                    "interpretation": {},
                    "is_current": true
                }
            ],
            "current_pinnacle": {
                "stage": "2",
                "number": 7,
                "age_range": "31 - 39",
                ...
            },
            "ai_context": "Hiện tại đang ở giai đoạn Pinnacle 2 (số 7)."
        },
        "challenges": {
            // Tương tự pinnacles
        }
    }
}
```

**Key features:**
- `current_age`: Tuổi hiện tại
- `is_current`: Flag để highlight giai đoạn hiện tại
- `current_pinnacle` / `current_challenge`: Giai đoạn hiện tại được extract ra
- `ai_context`: Hướng dẫn cho AI về giai đoạn hiện tại

---

### 7. **summary** (Tổng kết)

```json
{
    "summary": {
        "overview": "Nguyen Van A có Life Path Number là 6...",
        "key_characteristics": {
            "life_purpose": "...",
            "natural_talents": ["Phân tích", "Nghiên cứu", ...],
            "inner_desires": ["Tự chủ", "Lãnh đạo", ...],
            "strengths": ["Có trách nhiệm", ...],
            "challenges": ["Kiểm soát quá mức", ...]
        },
        "ai_interpretation_guide": {
            "instruction": "Khi phân tích báo cáo này, hãy chú ý đến:",
            "priorities": [
                "1. Life Path Number - Mục đích cuộc đời",
                "2. Expression Number - Tài năng",
                "3. Soul Urge Number - Động lực nội tâm",
                "4. Pinnacle hiện tại - Giai đoạn hiện tại",
                "5. Challenge hiện tại - Thử thách hiện tại",
                "6. Karmic Lessons - Bài học cần học"
            ],
            "interpretation_approach": "Hãy kết hợp tất cả các chỉ số..."
        }
    }
}
```

**Key features:**
- `overview`: Tóm tắt ngắn gọn
- `key_characteristics`: Đặc điểm chính
- `ai_interpretation_guide`: Hướng dẫn cho AI cách phân tích

---

## 🆚 SO SÁNH VỚI STANDARD OUTPUT

| Feature | get_all_numbers_with_interpretations() | get_extended_report() |
|---------|----------------------------------------|----------------------|
| **metadata** | ❌ | ✅ (timestamp, version, language) |
| **age** | ❌ | ✅ (calculated) |
| **name** | ❌ | ✅ (Vietnamese name) |
| **importance** | ❌ | ✅ (⭐⭐⭐⭐⭐) |
| **meaning** | ❌ | ✅ (Short description) |
| **ai_context** | ❌ | ✅ (AI guidance) |
| **current_pinnacle** | ❌ | ✅ (Highlighted) |
| **current_challenge** | ❌ | ✅ (Highlighted) |
| **summary** | ❌ | ✅ (Overview + guide) |

---

## 💡 USE CASES

### 1. **AI Chatbot Integration**
```python
report = calc.get_extended_report()

# AI có thể đọc ai_context để hiểu ý nghĩa
for key, data in report['core_numbers'].items():
    print(f"AI Context: {data['ai_context']}")
```

### 2. **JSON API Response**
```python
from flask import jsonify

@app.route('/api/numerology')
def get_numerology():
    calc = Numerology(name, birth_date, language='vi')
    return jsonify(calc.get_extended_report())
```

### 3. **Report Generation**
```python
report = calc.get_extended_report()

# Generate PDF/HTML report từ structured data
template.render(
    metadata=report['metadata'],
    personal_info=report['personal_information'],
    core_numbers=report['core_numbers'],
    summary=report['summary']
)
```

### 4. **AI Prompt Engineering**
```python
report = calc.get_extended_report()

prompt = f"""
Phân tích numerology cho {report['personal_information']['original_name']}:

{report['summary']['ai_interpretation_guide']['instruction']}

Life Path: {report['core_numbers']['life_path']['number']}
- {report['core_numbers']['life_path']['ai_context']}

Expression: {report['core_numbers']['expression']['number']}
- {report['core_numbers']['expression']['ai_context']}

...
"""
```

---

## 🎯 KEY DIFFERENCES

### **Standard Output** (get_all_numbers_with_interpretations)
- ✅ Minimal structure
- ✅ Chỉ có data cần thiết
- ✅ Dùng cho general purpose
- ❌ Thiếu metadata
- ❌ Thiếu AI guidance
- ❌ Không highlight current stage

### **Extended Report** (get_extended_report)
- ✅ Complete structure
- ✅ Metadata đầy đủ (timestamp, version, language)
- ✅ Age calculated
- ✅ Name, importance, meaning cho mỗi số
- ✅ AI context for each number
- ✅ Current pinnacle/challenge highlighted
- ✅ Summary với key characteristics
- ✅ AI interpretation guide
- ✅ **Ready for AI consumption**

---

## 📝 EXAMPLE SCRIPT

```python
#!/usr/bin/env python3
from numerology import Numerology
import json

# Input
calc = Numerology("Nguyen Van A", "15/08/1990", language='vi')

# Get extended report
report = calc.get_extended_report()

# Save to file
with open('ai_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

# Extract key info for AI
print(f"Name: {report['personal_information']['original_name']}")
print(f"Age: {report['personal_information']['age']}")
print(f"\nLife Path: {report['core_numbers']['life_path']['number']}")
print(f"AI Context: {report['core_numbers']['life_path']['ai_context']}")
print(f"\nCurrent Pinnacle: {report['life_cycles']['pinnacles']['current_pinnacle']['number']}")
print(f"Current Challenge: {report['life_cycles']['challenges']['current_challenge']['number']}")
```

---

## ✅ FEATURES

### Metadata
- ✅ Report type, timestamp, version, language

### Personal Info
- ✅ Original name, normalized name, birth date, **age**

### Every Number Has
- ✅ `number`: Value (1-9, 11, 22, 33)
- ✅ `name`: Vietnamese + English name
- ✅ `importance`: Stars rating
- ✅ `meaning`: Short description
- ✅ `interpretation`: Full interpretation from interpretations.py
- ✅ `ai_context`: Guidance for AI

### Life Cycles
- ✅ `current_age`: Calculated age
- ✅ `is_current`: Flag for current stage
- ✅ `current_pinnacle`: Extracted current pinnacle
- ✅ `current_challenge`: Extracted current challenge
- ✅ `ai_context`: AI guidance about current stage

### Summary
- ✅ `overview`: Short summary
- ✅ `key_characteristics`: Extracted key traits
- ✅ `ai_interpretation_guide`: How AI should analyze

---

## 🚀 TESTING

Run demo script:
```bash
python3 demo_extended_report.py
```

Output:
- Extended report structure
- Comparison with example_full_report.json
- Saved to `extended_report_output.json`

---

## 📞 SUPPORT

- **Standard output:** Use `get_all_numbers_with_interpretations()`
- **Extended report:** Use `get_extended_report()`
- **Documentation:** See EXAMPLE_INPUT_OUTPUT.md, JSON_OUTPUT_ANALYSIS.md

---

**Version:** 1.0.0
**Created:** 2025-01-13
**Purpose:** AI-friendly JSON output for numerology interpretation
