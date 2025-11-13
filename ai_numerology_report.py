"""
AI-Friendly Numerology Report Generator
Tạo báo cáo Thần Số Học dạng JSON cấu trúc rõ ràng cho AI Models
"""

import json
from datetime import datetime
from typing import Dict, Any, Optional
from numerology import Numerology
from interpretations import get_interpretation


class AINumerologyReport:
    """
    Tạo báo cáo Thần Số Học hoàn chỉnh với luận giải chi tiết
    dưới dạng JSON cấu trúc để AI models dễ dàng hiểu và phân tích
    """

    def __init__(self, full_name: str, birth_date: str, use_translation: bool = True):
        """
        Khởi tạo báo cáo Thần Số Học

        Args:
            full_name: Tên đầy đủ của người cần xem
            birth_date: Ngày sinh (DD/MM/YYYY hoặc DD-MM-YYYY)
            use_translation: Tự động dịch tên không phải Latin sang tiếng Anh
        """
        self.numerology = Numerology(full_name, birth_date, use_translation)

    def generate_complete_report(self) -> Dict[str, Any]:
        """
        Tạo báo cáo hoàn chỉnh với tất cả chỉ số và luận giải

        Returns:
            Dictionary cấu trúc JSON chứa toàn bộ thông tin và luận giải
        """
        report = {
            "metadata": {
                "report_type": "Numerology Complete Analysis",
                "generated_at": datetime.now().isoformat(),
                "version": "1.0",
                "language": "Vietnamese"
            },

            "personal_information": self._get_personal_info(),

            "core_numbers": self._get_core_numbers_with_interpretations(),

            "secondary_numbers": self._get_secondary_numbers_with_interpretations(),

            "name_analysis": self._get_name_analysis_with_interpretations(),

            "life_cycles": self._get_life_cycles_with_interpretations(),

            "summary": self._generate_summary()
        }

        return report

    def _get_personal_info(self) -> Dict[str, str]:
        """Lấy thông tin cá nhân"""
        return {
            "original_name": self.numerology.original_name,
            "normalized_name": self.numerology.full_name,
            "birth_date": self.numerology.birth_date.strftime('%d/%m/%Y'),
            "age": self._calculate_age()
        }

    def _calculate_age(self) -> str:
        """Tính tuổi hiện tại"""
        today = datetime.now()
        age = today.year - self.numerology.birth_date.year
        if today.month < self.numerology.birth_date.month or \
           (today.month == self.numerology.birth_date.month and today.day < self.numerology.birth_date.day):
            age -= 1
        return str(age)

    def _get_core_numbers_with_interpretations(self) -> Dict[str, Any]:
        """
        Lấy các chỉ số chính kèm luận giải chi tiết
        Đây là 5 chỉ số quan trọng nhất trong Thần Số Học
        """
        life_path = self.numerology.life_path_number()
        expression = self.numerology.expression_number()
        soul_urge = self.numerology.soul_urge_number()
        personality = self.numerology.personality_number()
        birthday = self.numerology.birthday_number()

        return {
            "life_path": {
                "number": life_path,
                "name": "Chỉ Số Đường Đời (Life Path Number)",
                "importance": "⭐⭐⭐⭐⭐ Quan trọng nhất",
                "meaning": "Mục đích và hướng đi của cuộc đời",
                "interpretation": get_interpretation('life_path', life_path),
                "ai_context": "Đây là chỉ số quan trọng nhất, thể hiện con đường và sứ mệnh cuộc đời của người này."
            },
            "expression": {
                "number": expression,
                "name": "Chỉ Số Biểu Đạt (Expression Number)",
                "importance": "⭐⭐⭐⭐⭐ Rất quan trọng",
                "meaning": "Tài năng, khả năng và số mệnh bẩm sinh",
                "interpretation": get_interpretation('expression', expression),
                "ai_context": "Chỉ số này cho biết tài năng tự nhiên và cách người này thể hiện bản thân với thế giới."
            },
            "soul_urge": {
                "number": soul_urge,
                "name": "Chỉ Số Linh Hồn (Soul Urge Number)",
                "importance": "⭐⭐⭐⭐⭐ Rất quan trọng",
                "meaning": "Mong muốn nội tâm và động lực sâu xa",
                "interpretation": get_interpretation('soul_urge', soul_urge),
                "ai_context": "Đây là động lực nội tâm sâu xa nhất, những gì linh hồn người này thực sự khao khát."
            },
            "personality": {
                "number": personality,
                "name": "Chỉ Số Nhân Cách (Personality Number)",
                "importance": "⭐⭐⭐⭐ Quan trọng",
                "meaning": "Ấn tượng ban đầu, cách người khác nhìn nhận",
                "interpretation": get_interpretation('personality', personality),
                "ai_context": "Chỉ số này thể hiện hình ảnh bên ngoài và ấn tượng đầu tiên mà người này tạo ra."
            },
            "birthday": {
                "number": birthday,
                "name": "Chỉ Số Ngày Sinh (Birthday Number)",
                "importance": "⭐⭐⭐ Khá quan trọng",
                "meaning": "Tài năng đặc biệt mang theo từ khi sinh ra",
                "interpretation": get_interpretation('birthday', birthday),
                "ai_context": "Một tài năng hoặc khả năng đặc biệt mà người này có từ khi sinh ra."
            }
        }

    def _get_secondary_numbers_with_interpretations(self) -> Dict[str, Any]:
        """
        Lấy các chỉ số phụ kèm luận giải
        Cung cấp thêm thông tin chi tiết về tính cách và khả năng
        """
        maturity = self.numerology.maturity_number()
        balance = self.numerology.balance_number()
        hidden_passion = self.numerology.hidden_passion_number()
        subconscious = self.numerology.subconscious_self()

        return {
            "maturity": {
                "number": maturity,
                "name": "Số Trưởng Thành (Maturity Number)",
                "importance": "⭐⭐⭐ Khá quan trọng",
                "meaning": "Mục tiêu và phẩm chất phát triển khi trưởng thành",
                "interpretation": get_interpretation('maturity', maturity),
                "ai_context": "Chỉ số này cho thấy người này sẽ phát triển và trưởng thành như thế nào theo thời gian."
            },
            "balance": {
                "number": balance,
                "name": "Số Cân Bằng (Balance Number)",
                "importance": "⭐⭐⭐ Khá quan trọng",
                "meaning": "Cách đối phó với khó khăn và thử thách",
                "interpretation": get_interpretation('balance', balance),
                "ai_context": "Cách tự nhiên mà người này phản ứng và giải quyết vấn đề khi gặp khó khăn."
            },
            "hidden_passion": {
                "number": hidden_passion,
                "name": "Đam Mê Ẩn (Hidden Passion Number)",
                "importance": "⭐⭐⭐ Khá quan trọng",
                "meaning": "Đam mê và điều bạn yêu thích nhất",
                "interpretation": get_interpretation('hidden_passion', hidden_passion),
                "ai_context": "Điều mà người này có đam mê mãnh liệt nhất, thường thể hiện qua hành động."
            },
            "subconscious_self": {
                "number": subconscious,
                "name": "Tiềm Thức (Subconscious Self)",
                "importance": "⭐⭐ Tham khảo",
                "meaning": "Tự tin và khả năng đối phó với tình huống khẩn cấp",
                "interpretation": get_interpretation('subconscious_self', subconscious),
                "ai_context": f"Người này có {subconscious} trên 9 số trong tên, cho thấy mức độ tự tin và nguồn lực nội tâm."
            }
        }

    def _get_name_analysis_with_interpretations(self) -> Dict[str, Any]:
        """
        Phân tích tên kèm luận giải
        Bao gồm Cornerstone, Capstone và Karmic Lessons
        """
        cornerstone_letter, cornerstone_value = self.numerology.cornerstone()
        capstone_letter, capstone_value = self.numerology.capstone()
        karmic_lessons = self.numerology.karmic_lesson_numbers()

        # Cornerstone
        cornerstone_data = {
            "letter": cornerstone_letter,
            "number": cornerstone_value,
            "name": "Đá Góc (Cornerstone)",
            "importance": "⭐⭐ Tham khảo",
            "meaning": "Cách tiếp cận cơ hội và thử thách",
            "interpretation": get_interpretation('cornerstone', cornerstone_value),
            "ai_context": f"Chữ cái đầu tiên '{cornerstone_letter}' cho thấy cách người này bắt đầu và tiếp cận mọi việc."
        }

        # Capstone
        capstone_data = {
            "letter": capstone_letter,
            "number": capstone_value,
            "name": "Đá Chóp (Capstone)",
            "importance": "⭐⭐ Tham khảo",
            "meaning": "Khả năng hoàn thành và kết thúc công việc",
            "interpretation": get_interpretation('capstone', capstone_value),
            "ai_context": f"Chữ cái cuối cùng '{capstone_letter}' cho thấy cách người này hoàn thành và kết thúc mọi việc."
        }

        # Karmic Lessons
        karmic_data = {
            "missing_numbers": karmic_lessons if karmic_lessons else [],
            "name": "Bài Học Nghiệp (Karmic Lessons)",
            "importance": "⭐⭐⭐ Khá quan trọng",
            "meaning": "Các bài học cần học, điểm yếu cần khắc phục",
            "interpretations": [
                {
                    "number": num,
                    "interpretation": get_interpretation('karmic_lesson', num)
                } for num in karmic_lessons
            ] if karmic_lessons else [],
            "ai_context": "Những số KHÔNG xuất hiện trong tên, thể hiện các bài học mà người này cần học trong đời." if karmic_lessons else "Người này có đầy đủ tất cả các số 1-9 trong tên - đây là điều hiếm gặp và tích cực!"
        }

        return {
            "cornerstone": cornerstone_data,
            "capstone": capstone_data,
            "karmic_lessons": karmic_data
        }

    def _get_life_cycles_with_interpretations(self) -> Dict[str, Any]:
        """
        Lấy chu kỳ cuộc đời kèm luận giải
        Bao gồm 4 Pinnacles và 4 Challenges
        """
        pinnacles = self.numerology.pinnacle_numbers()
        challenges = self.numerology.challenge_numbers()
        current_age = int(self._calculate_age())

        # Xử lý Pinnacles
        pinnacles_data = []
        current_pinnacle = None

        for key in ['pinnacle_1', 'pinnacle_2', 'pinnacle_3', 'pinnacle_4']:
            p = pinnacles[key]
            pinnacle_obj = {
                "stage": key.replace('pinnacle_', ''),
                "number": p['number'],
                "age_range": p['age_range'],
                "start_age": p['start_age'],
                "end_age": p['end_age'],
                "interpretation": get_interpretation('pinnacle', p['number']),
                "is_current": False
            }

            # Kiểm tra xem có phải giai đoạn hiện tại không
            if p['end_age'] is None:  # Pinnacle 4
                if current_age >= p['start_age']:
                    pinnacle_obj['is_current'] = True
                    current_pinnacle = pinnacle_obj
            elif p['start_age'] <= current_age <= p['end_age']:
                pinnacle_obj['is_current'] = True
                current_pinnacle = pinnacle_obj

            pinnacles_data.append(pinnacle_obj)

        # Xử lý Challenges
        challenges_data = []
        current_challenge = None

        for key in ['challenge_1', 'challenge_2', 'challenge_3', 'challenge_4']:
            c = challenges[key]
            challenge_obj = {
                "stage": key.replace('challenge_', ''),
                "number": c['number'],
                "age_range": c['age_range'],
                "start_age": c['start_age'],
                "end_age": c['end_age'],
                "interpretation": get_interpretation('challenge', c['number']),
                "is_current": False
            }

            # Kiểm tra xem có phải giai đoạn hiện tại không
            if c['end_age'] is None:  # Challenge 4
                if current_age >= c['start_age']:
                    challenge_obj['is_current'] = True
                    current_challenge = challenge_obj
            elif c['start_age'] <= current_age <= c['end_age']:
                challenge_obj['is_current'] = True
                current_challenge = challenge_obj

            challenges_data.append(challenge_obj)

        return {
            "current_age": current_age,
            "pinnacles": {
                "name": "4 Đỉnh Cao (Pinnacle Numbers)",
                "importance": "⭐⭐⭐⭐ Rất quan trọng",
                "meaning": "4 giai đoạn chính trong cuộc đời, mỗi giai đoạn mang cơ hội khác nhau",
                "data": pinnacles_data,
                "current_pinnacle": current_pinnacle,
                "ai_context": f"Hiện tại đang ở giai đoạn Pinnacle {current_pinnacle['stage']} (số {current_pinnacle['number']})." if current_pinnacle else "Chưa xác định được giai đoạn hiện tại."
            },
            "challenges": {
                "name": "4 Số Thử Thách (Challenge Numbers)",
                "importance": "⭐⭐⭐⭐ Rất quan trọng",
                "meaning": "4 thử thách chính cần vượt qua trong từng giai đoạn cuộc đời",
                "data": challenges_data,
                "current_challenge": current_challenge,
                "ai_context": f"Hiện tại đang đối mặt với Challenge {current_challenge['stage']} (số {current_challenge['number']})." if current_challenge else "Chưa xác định được thử thách hiện tại."
            }
        }

    def _generate_summary(self) -> Dict[str, Any]:
        """
        Tạo tóm tắt tổng quan cho AI dễ hiểu
        """
        life_path = self.numerology.life_path_number()
        expression = self.numerology.expression_number()
        soul_urge = self.numerology.soul_urge_number()

        lp_interp = get_interpretation('life_path', life_path)
        exp_interp = get_interpretation('expression', expression)
        su_interp = get_interpretation('soul_urge', soul_urge)

        return {
            "overview": f"{self.numerology.original_name} có Life Path Number là {life_path} ({lp_interp.get('title', '')}), Expression Number là {expression} ({exp_interp.get('title', '')}), và Soul Urge Number là {soul_urge} ({su_interp.get('title', '')}).",

            "key_characteristics": {
                "life_purpose": lp_interp.get('description', '').strip(),
                "natural_talents": exp_interp.get('talents', []),
                "inner_desires": su_interp.get('desires', []),
                "strengths": lp_interp.get('strengths', []),
                "challenges": lp_interp.get('challenges', [])
            },

            "ai_interpretation_guide": {
                "instruction": "Khi phân tích báo cáo này, hãy chú ý đến:",
                "priorities": [
                    "1. Life Path Number - Mục đích cuộc đời và con đường chính",
                    "2. Expression Number - Tài năng và cách thể hiện bản thân",
                    "3. Soul Urge Number - Động lực nội tâm và mong muốn sâu xa",
                    "4. Pinnacle hiện tại - Giai đoạn và cơ hội hiện tại",
                    "5. Challenge hiện tại - Thử thách cần vượt qua ngay bây giờ",
                    "6. Karmic Lessons - Bài học cần học trong đời"
                ],
                "interpretation_approach": "Hãy kết hợp tất cả các chỉ số để tạo ra một bức tranh toàn diện về con người này. Chú ý đến sự tương tác giữa các chỉ số, đặc biệt là khi có mâu thuẫn giữa mong muốn nội tâm (Soul Urge) và hình ảnh bên ngoài (Personality)."
            }
        }

    def to_json(self, indent: int = 2, ensure_ascii: bool = False) -> str:
        """
        Xuất báo cáo ra JSON string

        Args:
            indent: Số space để indent (mặc định 2)
            ensure_ascii: Có encode Unicode thành ASCII không (mặc định False để giữ tiếng Việt)

        Returns:
            JSON string
        """
        report = self.generate_complete_report()
        return json.dumps(report, indent=indent, ensure_ascii=ensure_ascii)

    def to_dict(self) -> Dict[str, Any]:
        """
        Xuất báo cáo ra Python dictionary

        Returns:
            Dictionary chứa toàn bộ báo cáo
        """
        return self.generate_complete_report()

    def save_to_file(self, filename: str, indent: int = 2) -> None:
        """
        Lưu báo cáo vào file JSON

        Args:
            filename: Tên file để lưu
            indent: Số space để indent
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.to_json(indent=indent))
        print(f"✅ Đã lưu báo cáo vào file: {filename}")


def create_ai_report(full_name: str, birth_date: str,
                     use_translation: bool = True) -> Dict[str, Any]:
    """
    Helper function để tạo báo cáo nhanh

    Args:
        full_name: Tên đầy đủ
        birth_date: Ngày sinh (DD/MM/YYYY)
        use_translation: Tự động dịch tên không phải Latin

    Returns:
        Dictionary chứa báo cáo hoàn chỉnh
    """
    reporter = AINumerologyReport(full_name, birth_date, use_translation)
    return reporter.to_dict()


# ========== EXAMPLE USAGE ==========
if __name__ == "__main__":
    # Ví dụ 1: Tạo báo cáo và in ra JSON
    print("=" * 80)
    print("VÍ DỤ 1: Tạo báo cáo Thần Số Học cho AI")
    print("=" * 80)

    reporter = AINumerologyReport("Nguyen Van A", "15/08/1990")

    # Xuất ra JSON
    json_report = reporter.to_json(indent=2)
    print(json_report)

    print("\n" + "=" * 80)
    print("VÍ DỤ 2: Lưu báo cáo vào file")
    print("=" * 80)

    # Lưu vào file
    reporter.save_to_file("numerology_report.json")

    print("\n" + "=" * 80)
    print("VÍ DỤ 3: Sử dụng helper function")
    print("=" * 80)

    # Sử dụng helper function
    report_dict = create_ai_report("Tran Thi B", "20/12/1995")
    print(f"Report type: {report_dict['metadata']['report_type']}")
    print(f"Life Path: {report_dict['core_numbers']['life_path']['number']}")
    print(f"Current Age: {report_dict['personal_information']['age']}")
