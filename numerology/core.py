"""
Thư viện Thần Số Học (Numerology) - Tính toán các chỉ số numerology
Hỗ trợ tiếng Việt và các ngôn ngữ khác thông qua Google Translate API
"""

import re
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from collections import Counter

# Import interpretations module
try:
    from .interpretations import get_interpretation
    INTERPRETATIONS_AVAILABLE = True
except ImportError:
    INTERPRETATIONS_AVAILABLE = False

# Google Translate API (optional)
try:
    from googletrans import Translator
    GOOGLETRANS_AVAILABLE = True
except ImportError:
    GOOGLETRANS_AVAILABLE = False


class Numerology:
    """
    Lớp chính để tính toán các chỉ số Thần Số Học
    """

    # Bảng quy đổi chữ cái sang số theo Pythagorean system
    LETTER_VALUES = {
        'A': 1, 'J': 1, 'S': 1,
        'B': 2, 'K': 2, 'T': 2,
        'C': 3, 'L': 3, 'U': 3,
        'D': 4, 'M': 4, 'V': 4,
        'E': 5, 'N': 5, 'W': 5,
        'F': 6, 'O': 6, 'X': 6,
        'G': 7, 'P': 7, 'Y': 7,
        'H': 8, 'Q': 8, 'Z': 8,
        'I': 9, 'R': 9
    }

    # Các số chủ (Master Numbers) không được rút gọn
    MASTER_NUMBERS = [11, 22, 33]

    # Nguyên âm trong tiếng Anh/Latinh
    VOWELS = set('AEIOU')

    def __init__(self, full_name: str, birth_date: str, use_translation: bool = True, language: str = 'vi'):
        """
        Khởi tạo đối tượng Numerology

        Args:
            full_name: Tên đầy đủ (ví dụ: "NGUYEN VAN A", "田中太郎", "김철수")
            birth_date: Ngày sinh theo định dạng "DD/MM/YYYY" hoặc "DD-MM-YYYY"
            use_translation: Tự động dịch tên không phải Latin sang tiếng Anh (mặc định: True)
            language: Ngôn ngữ để xử lý Y ('vi'=Việt, 'en'=Anh, 'ja'=Nhật, 'ko'=Hàn, 'zh'=Trung, 'fr'=Pháp, 'pt'=Bồ Đào Nha,
                        'es'=Tây Ban Nha, 'de'=Đức, 'nl'=Hà Lan, 'ru'=Nga, 'uk'=Ukraina, 'it'=Ý, 'hi'=Hindi, 'ar'=Ả Rập,
                        'id'=Indonesia, 'tr'=Thổ Nhĩ Kỳ, 'th'=Thái, 'ms'=Mã Lai, 'tl'=Tagalog, 'el'=Hy Lạp,
                        'pl'=Ba Lan, 'my'=Burmese, 'si'=Sinhala, 'ne'=Nepali, 'wo'=Wolof, 'yo'=Yoruba)
        """
        self.original_name = full_name
        self.use_translation = use_translation
        self.language = language.lower()  # 30 ngôn ngữ được hỗ trợ
        self.full_name = self._normalize_name(full_name)
        self.birth_date = self._parse_birth_date(birth_date)

    def _normalize_name(self, name: str) -> str:
        """
        Chuẩn hóa tên: loại bỏ dấu, chuyển thành chữ hoa, loại bỏ ký tự đặc biệt
        Tự động dịch tên không phải Latin sang tiếng Anh nếu cần
        """
        # Kiểm tra xem tên có chứa ký tự không phải Latin không
        if self.use_translation and self._contains_non_latin(name):
            name = self._translate_to_english(name)

        # Loại bỏ dấu tiếng Việt
        name = self._remove_vietnamese_accents(name)
        # Chuyển thành chữ hoa
        name = name.upper()
        # Chỉ giữ lại chữ cái và khoảng trắng
        name = re.sub(r'[^A-Z\s]', '', name)
        # Loại bỏ khoảng trắng thừa
        name = ' '.join(name.split())
        return name

    def _remove_vietnamese_accents(self, text: str) -> str:
        """
        Loại bỏ dấu tiếng Việt, chuyển về ký tự Latin
        """
        vietnamese_map = {
            'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
            'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
            'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
            'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
            'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
            'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
            'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
            'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
            'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
            'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
            'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
            'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
            'đ': 'd',
            'À': 'A', 'Á': 'A', 'Ả': 'A', 'Ã': 'A', 'Ạ': 'A',
            'Ă': 'A', 'Ằ': 'A', 'Ắ': 'A', 'Ẳ': 'A', 'Ẵ': 'A', 'Ặ': 'A',
            'Â': 'A', 'Ầ': 'A', 'Ấ': 'A', 'Ẩ': 'A', 'Ẫ': 'A', 'Ậ': 'A',
            'È': 'E', 'É': 'E', 'Ẻ': 'E', 'Ẽ': 'E', 'Ẹ': 'E',
            'Ê': 'E', 'Ề': 'E', 'Ế': 'E', 'Ể': 'E', 'Ễ': 'E', 'Ệ': 'E',
            'Ì': 'I', 'Í': 'I', 'Ỉ': 'I', 'Ĩ': 'I', 'Ị': 'I',
            'Ò': 'O', 'Ó': 'O', 'Ỏ': 'O', 'Õ': 'O', 'Ọ': 'O',
            'Ô': 'O', 'Ồ': 'O', 'Ố': 'O', 'Ổ': 'O', 'Ỗ': 'O', 'Ộ': 'O',
            'Ơ': 'O', 'Ờ': 'O', 'Ớ': 'O', 'Ở': 'O', 'Ỡ': 'O', 'Ợ': 'O',
            'Ù': 'U', 'Ú': 'U', 'Ủ': 'U', 'Ũ': 'U', 'Ụ': 'U',
            'Ư': 'U', 'Ừ': 'U', 'Ứ': 'U', 'Ử': 'U', 'Ữ': 'U', 'Ự': 'U',
            'Ỳ': 'Y', 'Ý': 'Y', 'Ỷ': 'Y', 'Ỹ': 'Y', 'Ỵ': 'Y',
            'Đ': 'D'
        }

        for viet_char, latin_char in vietnamese_map.items():
            text = text.replace(viet_char, latin_char)

        return text

    def _contains_non_latin(self, text: str) -> bool:
        """
        Kiểm tra xem văn bản có chứa ký tự không phải Latin không
        (Chữ Trung, Nhật, Hàn, Ả Rập, Cyrillic, etc.)
        """
        # Loại bỏ khoảng trắng và ký tự đặc biệt
        clean_text = re.sub(r'[\s\-_.,!?]', '', text)

        # Kiểm tra từng ký tự
        for char in clean_text:
            # Lấy Unicode code point
            code = ord(char)

            # Kiểm tra các khoảng Unicode cho ký tự không phải Latin
            # CJK (Chinese, Japanese, Korean): 0x4E00-0x9FFF, 0x3040-0x30FF, 0xAC00-0xD7AF
            # Arabic: 0x0600-0x06FF
            # Cyrillic: 0x0400-0x04FF
            # Thai: 0x0E00-0x0E7F
            # Hebrew: 0x0590-0x05FF
            non_latin_ranges = [
                (0x4E00, 0x9FFF),   # CJK Unified Ideographs
                (0x3040, 0x309F),   # Hiragana
                (0x30A0, 0x30FF),   # Katakana
                (0xAC00, 0xD7AF),   # Hangul (Korean)
                (0x0600, 0x06FF),   # Arabic
                (0x0400, 0x04FF),   # Cyrillic
                (0x0E00, 0x0E7F),   # Thai
                (0x0590, 0x05FF),   # Hebrew
            ]

            for start, end in non_latin_ranges:
                if start <= code <= end:
                    return True

        return False

    def _translate_to_english(self, text: str) -> str:
        """
        Dịch tên từ ngôn ngữ khác sang tiếng Anh sử dụng Google Translate API

        Args:
            text: Tên cần dịch

        Returns:
            Tên đã được dịch sang tiếng Anh (romanized/transliterated)
        """
        if not GOOGLETRANS_AVAILABLE:
            print("⚠️  Cảnh báo: Thư viện googletrans chưa được cài đặt.")
            print("    Để dịch tên không phải Latin, cài đặt: pip install googletrans==4.0.0rc1")
            print("    Đang sử dụng tên gốc (có thể không chính xác)...")
            return text

        try:
            translator = Translator()

            # Dịch sang tiếng Anh
            result = translator.translate(text, dest='en')

            # Google Translate sẽ romanize các ký tự không phải Latin
            translated_text = result.text

            print(f"🌍 Đã dịch tên: '{text}' → '{translated_text}'")

            return translated_text

        except Exception as e:
            print(f"⚠️  Lỗi khi dịch tên: {e}")
            print(f"    Đang sử dụng tên gốc...")
            return text

    def _parse_birth_date(self, date_str: str) -> datetime:
        """
        Phân tích ngày sinh từ chuỗi
        """
        # Thử các định dạng khác nhau
        formats = ['%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y', '%Y-%m-%d']

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue

        raise ValueError(f"Không thể phân tích ngày sinh: {date_str}. Vui lòng sử dụng định dạng DD/MM/YYYY")

    def _is_vowel(self, letter: str, word: str, position: int) -> bool:
        """
        Xác định xem một chữ cái có phải là nguyên âm hay không
        Gọi hàm xử lý Y tương ứng với ngôn ngữ

        Args:
            letter: Chữ cái cần kiểm tra
            word: Từ chứa chữ cái
            position: Vị trí của chữ cái trong từ
        """
        # Nguyên âm thông thường (A, E, I, O, U)
        if letter in self.VOWELS:
            return True

        # Xử lý đặc biệt cho chữ Y theo ngôn ngữ
        if letter == 'Y':
            if self.language == 'vi':
                return self._is_y_vowel_vietnamese(word, position)
            elif self.language == 'ja':
                return self._is_y_vowel_japanese(word, position)
            elif self.language == 'ko':
                return self._is_y_vowel_korean(word, position)
            elif self.language == 'zh':
                return self._is_y_vowel_chinese(word, position)
            elif self.language == 'fr':
                return self._is_y_vowel_french(word, position)
            elif self.language == 'pt':
                return self._is_y_vowel_portuguese(word, position)
            elif self.language == 'es':
                return self._is_y_vowel_spanish(word, position)
            elif self.language == 'de':
                return self._is_y_vowel_german(word, position)
            elif self.language == 'nl':
                return self._is_y_vowel_dutch(word, position)
            elif self.language == 'ru':
                return self._is_y_vowel_russian(word, position)
            elif self.language == 'uk':  # Ukraina
                return self._is_y_vowel_ukrainian(word, position)
            elif self.language == 'it':
                return self._is_y_vowel_italian(word, position)
            elif self.language == 'hi':
                return self._is_y_vowel_hindi(word, position)
            elif self.language == 'id':
                return self._is_y_vowel_indonesian(word, position)
            elif self.language == 'ms':
                return self._is_y_vowel_malay(word, position)
            elif self.language == 'tr':  # Thổ Nhĩ Kỳ
                return self._is_y_vowel_turkish(word, position)
            elif self.language == 'ar':
                return self._is_y_vowel_arabic(word, position)
            elif self.language == 'th':
                return self._is_y_vowel_thai(word, position)
            elif self.language == 'tl':
                return self._is_y_vowel_tagalog(word, position)
            elif self.language in ['el', 'pl']:  # Hy Lạp, Ba Lan
                return True  # Luôn là nguyên âm
            elif self.language == 'my':
                return self._is_y_vowel_burmese(word, position)
            elif self.language == 'si':
                return self._is_y_vowel_sinhala(word, position)
            elif self.language == 'ne':
                return self._is_y_vowel_nepali(word, position)
            elif self.language == 'wo':
                return self._is_y_vowel_wolof(word, position)
            elif self.language == 'yo':
                return self._is_y_vowel_yoruba(word, position)
            else:  # 'en' hoặc mặc định
                return self._is_y_vowel_english(word, position)

        return False

    def _is_y_vowel_vietnamese(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG VIỆT

        Thuật toán MỚI (sắp xếp lại thứ tự):
        1. Y đầu từ + sau là nguyên âm → PHỤ ÂM (YÊN, YẾU)
        2. Y giữa 2 nguyên âm → PHỤ ÂM (NGUYÊN, HUYỀN)
        3. Y là nguyên âm duy nhất → NGUYÊN ÂM (Y, NY, KỲ)
        4. Y sau nguyên âm, sau không còn nguyên âm → NGUYÊN ÂM (DUY, QUAY)
        5. Y sau phụ âm, sau không còn nguyên âm → NGUYÊN ÂM (HUYNH, MY)
        6. Y giữa 2 phụ âm → NGUYÊN ÂM (TRYM - từ mượn)
        7. Còn lại → PHỤ ÂM
        """
        # Rule 1: Y đầu từ + sau là nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 2: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y là nguyên âm duy nhất → NGUYÊN ÂM
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 4: Y sau nguyên âm, sau không còn nguyên âm → NGUYÊN ÂM
        if position > 0:
            prev_char = word[position - 1]
            if prev_char in self.VOWELS:
                has_vowel_after = any(word[i] in self.VOWELS for i in range(position + 1, len(word)))
                if not has_vowel_after:
                    return True

        # Rule 5: Y sau phụ âm, sau không còn nguyên âm → NGUYÊN ÂM
        if position > 0:
            prev_char = word[position - 1]
            if prev_char not in self.VOWELS:
                has_vowel_after = any(word[i] in self.VOWELS for i in range(position + 1, len(word)))
                if not has_vowel_after:
                    return True

        # Rule 6: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 7: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_english(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG ANH

        Thuật toán MỚI - 9 quy tắc (theo thứ tự ưu tiên):
        1. Y là chữ cái duy nhất → NGUYÊN ÂM (Y, BY, MY, FLY, CRY)
        2. Không có A/E/I/O/U → NGUYÊN ÂM (GYPSY, LYNCH, CRYPT)
        3. Y đầu từ + nguyên âm → PHỤ ÂM (YES, YOUNG, YELLOW, YACHT)
        4. Y cuối từ sau phụ âm → NGUYÊN ÂM (HAPPY, SKY, FLY, PARTY)
        5. Y giữa 2 phụ âm → NGUYÊN ÂM (RHYTHM, LYNX, NYMPH, SYLPH)
        6. Y sau nguyên âm + không còn nguyên âm sau → NGUYÊN ÂM (DAY, BOY, PLAY, GREY)
        7. Y giữa 2 nguyên âm → PHỤ ÂM (ROYAL, LAYER, MAYONNAISE, LOYAL)
        8. Y sau phụ âm + trước nguyên âm → PHỤ ÂM (BEYOND, CANYON, LAWYER)
        9. Còn lại → PHỤ ÂM
        """
        # Rule 1: Y là chữ cái duy nhất (hoặc chỉ có Y, không có A/E/I/O/U)
        if len(word) == 1:
            return True

        # Rule 8: Không có A/E/I/O/U nào khác (check sớm cho hiệu quả)
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 2: Y đầu từ + nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 3: Y cuối từ sau phụ âm → NGUYÊN ÂM
        if position == len(word) - 1 and position > 0:
            prev_char = word[position - 1]
            if prev_char not in self.VOWELS:
                return True

        # Rule 4: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 5: Y sau nguyên âm, không còn nguyên âm sau → NGUYÊN ÂM
        if position > 0:
            prev_char = word[position - 1]
            if prev_char in self.VOWELS:
                has_vowel_after = any(word[i] in self.VOWELS for i in range(position + 1, len(word)))
                if not has_vowel_after:
                    return True

        # Rule 6: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 7: Y sau phụ âm + trước nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 9: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_japanese(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG NHẬT (Romaji)

        Thuật toán MỚI:
        - Y LUÔN LÀ PHỤ ÂM trong Romaji chuẩn
        - Y + a/u/o → YA, YU, YO (phụ âm)
        - Không có trường hợp Y là nguyên âm trong từ Nhật gốc
        - Nếu từ mượn (katakana) → người dùng nên chọn ngôn ngữ gốc
        """
        # Y luôn là phụ âm trong tiếng Nhật gốc
        return False

    def _is_y_vowel_korean(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG HÀN

        Thuật toán MỚI (5 quy tắc):
        1. Y + nguyên âm (a/ae/eo/e/o/u) → PHỤ ÂM (야=YA, 여=YEO, 유=YU, 예=YE, 요=YO, 애=YAE)
        2. Phụ âm + Y + nguyên âm → PHỤ ÂM (햐=HYA, 뷰=BYU, 표=PYO)
        3. Trong từ Hàn gốc, Y luôn là PHỤ ÂM
        4. Nếu Y xuất hiện như vowel trong từ mượn (MY, SKY...) → dùng quy tắc tiếng Anh
        5. Còn lại → PHỤ ÂM

        Lưu ý: Trong tiếng Hàn gốc, Y luôn hoạt động như phụ âm (반모음).
        """
        # Rule 1 & 2: Y + (a/ae/eo/e/o/u) → PHỤ ÂM (bất kể có phụ âm trước hay không)
        if position < len(word) - 1:
            # Kiểm tra ae, eo (2 ký tự)
            if position < len(word) - 2:
                two_chars = word[position + 1:position + 3]
                if two_chars in ['AE', 'EO']:
                    return False

            # Kiểm tra a, e, o, u (1 ký tự)
            next_char = word[position + 1]
            if next_char in ['A', 'E', 'O', 'U']:
                return False

        # Rule 4: Từ mượn tiếng Anh - Y giữa 2 phụ âm → NGUYÊN ÂM (MY, SKY, GYM)
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True  # Dùng quy tắc Anh cho từ mượn

        # Rule 4: Y cuối từ sau phụ âm trong từ mượn → NGUYÊN ÂM (MY, SKY, ANGRY)
        if position == len(word) - 1 and position > 0:
            prev_char = word[position - 1]
            if prev_char not in self.VOWELS:
                return True  # Dùng quy tắc Anh

        # Rule 3 & 5: Trong từ Hàn gốc, Y luôn là PHỤ ÂM
        return False

    def _is_y_vowel_chinese(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG TRUNG (Pinyin)

        Thuật toán MỚI (3 quy tắc):
        1. Y + I → PHỤ ÂM (YI, YIN, YING, YI义/衣)
        2. Y + (a/e/o/u/ü/ao/an/ang/ou) → PHỤ ÂM (YANG, YE, YOU, YU, YUE, YUAN, YAO, YAN)
        3. Còn lại → PHỤ ÂM

        Lưu ý: Trong Pinyin chuẩn, Y luôn là PHỤ ÂM (semi-vowel).
        Không có trường hợp Y là nguyên âm trong tiếng Trung gốc.
        """
        # Rule 1: Y + I → PHỤ ÂM (YI, YIN, YING, YI义/衣)
        if position < len(word) - 1:
            next_char = word[position + 1]
            if next_char == 'I':
                return False

        # Rule 2: Y + (a/e/o/u) → PHỤ ÂM (YANG, YE, YOU, YU, YUE, YUAN, YAO, YAN)
        if position < len(word) - 1:
            next_char = word[position + 1]
            if next_char in ['A', 'E', 'O', 'U']:
                return False

        # Rule 3: Còn lại → PHỤ ÂM
        # Trong Pinyin chuẩn, Y luôn là phụ âm
        return False

    def _is_y_vowel_french(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG PHÁP

        Thuật toán MỚI - 8 quy tắc:
        1. Y đầu từ/âm tiết + nguyên âm → PHỤ ÂM (YVES, YASMINE, YANN)
        2. Y giữa 2 nguyên âm → PHỤ ÂM (VOYAGE, ROYAL, MOYEN, JOYEUX)
        3. Y là nguyên âm duy nhất → NGUYÊN ÂM (hiếm trong Pháp chuẩn)
        4. Hai Y liền nhau (PAYY-, GUYY-) → Y₁ = NGUYÊN ÂM, Y₂ = PHỤ ÂM (PAYSAGE thực tế là PA-Y-SAGE)
        5. Y sau nguyên âm + phụ âm → NGUYÊN ÂM (RAYMOND, SAYNÈTE)
        6. Y cuối từ sau nguyên âm → NGUYÊN ÂM (HENRY, DAVY)
        7. Y giữa 2 phụ âm → NGUYÊN ÂM (LYNCH, LYNX - từ mượn)
        8. Còn lại → PHỤ ÂM
        """
        # Rule 3: Kiểm tra "yy" (hai Y liền nhau) → Y₁ = NGUYÊN ÂM, Y₂ = PHỤ ÂM
        if position > 0 and word[position - 1] == 'Y':
            return False  # THAY ĐỔI: Y thứ hai trong "yy" → PHỤ ÂM
        if position < len(word) - 1 and word[position + 1] == 'Y':
            return True   # Y thứ nhất trong "yy" → NGUYÊN ÂM

        # Rule 6: Không có nguyên âm nào khác ngoài Y
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 7: Y trong âm tiết cuối "-Y" (Y ở cuối từ) → NGUYÊN ÂM
        if position == len(word) - 1:
            return True

        # Rule 1: Y đầu từ/âm tiết + sau là nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 2: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 5: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 4: Y sau nguyên âm + (trước phụ âm hoặc cuối từ) → NGUYÊN ÂM
        if position > 0:
            prev_char = word[position - 1]
            if prev_char in self.VOWELS:
                # Y trước phụ âm
                if position < len(word) - 1:
                    next_char = word[position + 1]
                    if next_char not in self.VOWELS:
                        return True

        # Rule 8: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_portuguese(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG BỒ ĐÀO NHA

        Thuật toán:
        1. Nếu Y đứng đầu từ và sau là nguyên âm ⇒ Y = PHỤ ÂM
        2. Nếu Y nằm giữa hai nguyên âm ⇒ Y = PHỤ ÂM
        3. Nếu Y đứng giữa hai phụ âm ⇒ Y = NGUYÊN ÂM
        4. Nếu Y đứng cuối từ và sau phụ âm ⇒ Y = NGUYÊN ÂM
        5. Nếu Y là nguyên âm duy nhất trong từ ⇒ Y = NGUYÊN ÂM
        6. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 5: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 1: Y đầu từ + sau là nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 2: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 4: Y cuối từ + sau phụ âm → NGUYÊN ÂM
        if position == len(word) - 1 and position > 0:
            prev_char = word[position - 1]
            if prev_char not in self.VOWELS:
                return True

        # Rule 6: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_spanish(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG TÂY BAN NHA

        Thuật toán:
        1. Nếu Y đứng đầu từ + sau là nguyên âm ⇒ Y = PHỤ ÂM
        2. Nếu Y nằm giữa hai nguyên âm ⇒ Y = PHỤ ÂM
        3. Nếu Y nằm giữa hai phụ âm ⇒ Y = NGUYÊN ÂM
        4. Nếu Y đứng cuối từ ⇒ Y = NGUYÊN ÂM
        5. Nếu trong từ không có nguyên âm nào khác ngoài Y ⇒ Y = NGUYÊN ÂM
        6. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 5: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 4: Y đứng cuối từ → NGUYÊN ÂM
        if position == len(word) - 1:
            return True

        # Rule 1: Y đầu từ + sau là nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 2: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 6: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_german(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG ĐỨC

        Thuật toán:
        1. Khi Y đứng đầu từ + sau là nguyên âm ⇒ Y = PHỤ ÂM
        2. Nếu Y đứng đầu từ + sau là phụ âm ⇒ Y = NGUYÊN ÂM
        3. Nếu Y đứng giữa hai phụ âm ⇒ Y = NGUYÊN ÂM
        4. Nếu Y đứng cuối từ ⇒ Y = NGUYÊN ÂM
        5. Nếu Y đứng giữa hai nguyên âm ⇒ Y = PHỤ ÂM
        6. Nếu trong từ không có nguyên âm nào khác ngoài Y ⇒ Y = NGUYÊN ÂM
        7. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 6: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 4: Y cuối từ → NGUYÊN ÂM
        if position == len(word) - 1:
            return True

        # Rule 1 & 2: Y đầu từ
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False  # Rule 1: sau là nguyên âm → PHỤ ÂM
            else:
                return True   # Rule 2: sau là phụ âm → NGUYÊN ÂM

        # Rule 5: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 7: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_dutch(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG HÀ LAN

        Thuật toán:
        1. Nếu Y đứng đầu từ + theo sau là nguyên âm ⇒ Y = PHỤ ÂM
        2. Nếu Y đứng đầu từ + theo sau là phụ âm ⇒ Y = NGUYÊN ÂM
        3. Nếu Y nằm giữa hai phụ âm ⇒ Y = NGUYÊN ÂM
        4. Nếu Y đứng cuối từ ⇒ Y = NGUYÊN ÂM
        5. Nếu Y nằm giữa hai nguyên âm ⇒ Y = PHỤ ÂM
        6. Nếu trong từ không có nguyên âm nào khác ngoài Y ⇒ Y = NGUYÊN ÂM
        7. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 6: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 4: Y cuối từ → NGUYÊN ÂM
        if position == len(word) - 1:
            return True

        # Rule 1 & 2: Y đầu từ
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False  # Rule 1: sau là nguyên âm → PHỤ ÂM
            else:
                return True   # Rule 2: sau là phụ âm → NGUYÊN ÂM

        # Rule 5: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 7: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_russian(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG NGA

        Thuật toán MỚI (6 quy tắc):
        1. Y phiên âm từ "Ы" (sau phụ âm) → LUÔN LÀ NGUYÊN ÂM (DMITRY, SERGEY, YEVGENY, BYKOV, VYACHESLAV)
        2. Y cuối tên → NGUYÊN ÂM (ANDREY, NIKOLAY, DMITRY, SERGEY, GRIGORY, YURY)
        3. Y giữa 2 phụ âm → NGUYÊN ÂM (VYACHESLAV, BYKOV, RYKOV)
        4. Y đầu từ → NGUYÊN ÂM (YURY, YEVGENY - phiên âm từ Ю/Е/Ы)
        5. Y phiên âm từ "Й" (i ngắn) + sau là nguyên âm → PHỤ ÂM (rất hiếm)
        6. Trong 99% trường hợp → Y LÀ NGUYÊN ÂM

        Lưu ý: Trong tiếng Nga, Y hầu hết là nguyên âm vì phiên âm từ "Ы" hoặc "Ю/Е".
        Chỉ rất hiếm khi Y là phụ âm (phiên âm "Й" trong vài trường hợp đặc biệt).
        """
        # Rule 2: Y cuối từ → NGUYÊN ÂM (ANDREY, NIKOLAY, DMITRY, SERGEY, GRIGORY, YURY)
        if position == len(word) - 1:
            return True

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM (VYACHESLAV, BYKOV, RYKOV)
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 1: Y sau phụ âm → NGUYÊN ÂM (phiên âm "Ы")
        # Ví dụ: DMITRY (T-Y), SERGEY (G-Y), YEVGENY (G-Y)
        if position > 0:
            prev_char = word[position - 1]
            if prev_char not in self.VOWELS:
                return True

        # Rule 4: Y đầu từ → NGUYÊN ÂM (YURY, YEVGENY - phiên âm Ю/Е/Ы)
        if position == 0:
            return True

        # Rule 5: Y đầu từ + sau là nguyên âm → PHỤ ÂM (rất hiếm - phiên âm "Й")
        # (Đã được xử lý ở Rule 4, hầu hết Y đầu từ là nguyên âm)

        # Rule 6: Default → NGUYÊN ÂM (99% trường hợp)
        return True

    def _is_y_vowel_ukrainian(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG UKRAINA

        Thuật toán MỚI (5 quy tắc):
        1. Y phiên âm từ "И" → LUÔN LÀ NGUYÊN ÂM (YURIY, ANDRIY, VASYL, OLEKSIY)
        2. Y cuối tên → NGUYÊN ÂM (ANDRIY, YURIY, VASYL, DMITRY, SERGIY, OLEKSIY)
        3. Y giữa 2 phụ âm → NGUYÊN ÂM (KYRYL, PAVLYK)
        4. Y đầu từ → NGUYÊN ÂM (YURIY, YAROSLAV, YEVHEN - phiên âm từ Ю/Я/Є/И)
        5. Trong hầu hết trường hợp → Y LÀ NGUYÊN ÂM (giống tiếng Nga 99%)

        Lưu ý: Trong tiếng Ukraina, Y hầu như luôn là nguyên âm vì phiên âm từ "И"
        hoặc các chữ cái Cyrillic khác (Ю/Я/Є). Y là phụ âm rất hiếm.
        """
        # Rule 2: Y cuối từ → NGUYÊN ÂM (ANDRIY, YURIY, VASYL, SERGIY, OLEKSIY)
        if position == len(word) - 1:
            return True

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM (KYRYL, PAVLYK)
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 1: Y sau phụ âm → NGUYÊN ÂM (phiên âm "И")
        # Ví dụ: YURIY (R-Y), ANDRIY (R-Y), VASYL (S-Y)
        if position > 0:
            prev_char = word[position - 1]
            if prev_char not in self.VOWELS:
                return True

        # Rule 4: Y đầu từ → NGUYÊN ÂM (YURIY, YAROSLAV, YEVHEN)
        if position == 0:
            return True

        # Rule 5: Default → NGUYÊN ÂM (hầu hết trường hợp)
        return True

    def _is_y_vowel_italian(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG Ý

        Thuật toán:
        1. Y đứng đầu từ + theo sau là nguyên âm ⇒ Y = PHỤ ÂM
        2. Y đứng đầu từ + theo sau là phụ âm ⇒ Y = NGUYÊN ÂM
        3. Nếu Y nằm giữa hai phụ âm ⇒ Y = NGUYÊN ÂM
        4. Nếu Y đứng giữa hai nguyên âm ⇒ Y = PHỤ ÂM
        5. Nếu Y đứng cuối từ ⇒ Y = NGUYÊN ÂM
        6. Nếu trong từ không còn nguyên âm nào khác ngoài Y ⇒ Y = NGUYÊN ÂM
        7. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 6: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 5: Y cuối từ → NGUYÊN ÂM
        if position == len(word) - 1:
            return True

        # Rule 1 & 2: Y đầu từ
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False  # Rule 1: sau là nguyên âm → PHỤ ÂM
            else:
                return True   # Rule 2: sau là phụ âm → NGUYÊN ÂM

        # Rule 4: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 7: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_hindi(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG HINDI

        Thuật toán MỚI (5 quy tắc):
        1. Y gốc Hindi (phiên âm "य") đầu từ/sau phụ âm → LUÔN LÀ PHỤ ÂM (YASH, PRIYA, MAYA)
        2. Y cuối từ sau nguyên âm → NGUYÊN ÂM (VIJAY, SANJAY, AJAY, AARAV)
        3. Y giữa 2 phụ âm → NGUYÊN ÂM (từ mượn Anh: RHYTHM)
        4. Y là nguyên âm duy nhất → NGUYÊN ÂM (hiếm)
        5. Còn lại → PHỤ ÂM
        """
        # Rule 4: Y là nguyên âm duy nhất → NGUYÊN ÂM
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 2: Y cuối từ sau nguyên âm → NGUYÊN ÂM
        if position == len(word) - 1:
            if position > 0:
                prev_char = word[position - 1]
                if prev_char in self.VOWELS:
                    return True
            # Y cuối từ sau phụ âm → cũng NGUYÊN ÂM (VIJAY, SANJAY)
            return True

        # Rule 1: Y đầu từ + trước nguyên âm → PHỤ ÂM (phiên âm "य")
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 1: Y sau phụ âm + trước nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y giữa 2 phụ âm → NGUYÊN ÂM (từ mượn Anh)
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 5: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_indonesian(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG INDONESIA

        Thuật toán MỚI (3 quy tắc):
        1. Y trong từ gốc → LUÔN LÀ PHỤ ÂM (SAYA, MAYA, YANI)
        2. Y cuối từ sau nguyên âm (diphthong) → NGUYÊN ÂM (hiếm)
        3. Từ mượn tiếng Anh → dùng quy tắc tiếng Anh

        Lưu ý: Trong tiếng Indonesia gốc, Y hầu hết là phụ âm
        """
        # Rule 2: Y cuối từ sau nguyên âm → NGUYÊN ÂM (hiếm, chủ yếu từ mượn)
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in self.VOWELS:
                return True

        # Rule 1: Y trong từ gốc → PHỤ ÂM
        # Y đầu từ + trước nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Y sau phụ âm + trước nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Từ mượn - Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Default: PHỤ ÂM (theo rule 1)
        return False

    def _is_y_vowel_malay(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG MÃ LAI

        Thuật toán MỚI (3 quy tắc - giống Indonesia):
        1. Y trong từ gốc → LUÔN LÀ PHỤ ÂM (SAYA, MAYA)
        2. Y cuối từ sau nguyên âm (diphthong) → NGUYÊN ÂM (hiếm)
        3. Từ mượn tiếng Anh → dùng quy tắc tiếng Anh

        Lưu ý: Tiếng Mã Lai và Indonesia có quy tắc tương tự
        """
        # Rule 2: Y cuối từ sau nguyên âm → NGUYÊN ÂM (hiếm, chủ yếu từ mượn)
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in self.VOWELS:
                return True

        # Rule 1: Y trong từ gốc → PHỤ ÂM
        # Y đầu từ + trước nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Y sau phụ âm + trước nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Từ mượn - Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Default: PHỤ ÂM (theo rule 1)
        return False

    def _is_y_vowel_turkish(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG THỔ NHĨ KỲ

        Thuật toán MỚI (4 quy tắc):
        1. Y trong từ gốc Thổ Nhĩ Kỳ → LUÔN LÀ PHỤ ÂM (YILMAZ, AYŞE, YUSUF, BEYAZ)
        2. Y cuối tên Thổ → PHỤ ÂM (ÖZGÜR, không có Y cuối thông thường)
        3. Từ mượn tiếng Anh → dùng quy tắc tiếng Anh (HENRY, TONY)
        4. Còn lại → PHỤ ÂM
        """
        # Rule 1 & 2 & 4: Y trong tiếng Thổ luôn là PHỤ ÂM
        # Chỉ kiểm tra nếu là từ mượn Anh (Y giữa 2 phụ âm)

        # Rule 3: Từ mượn Anh - Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                # Có thể là từ mượn như RHYTHM
                return True

        # Rule 1 & 4: Default → PHỤ ÂM
        return False

    def _is_y_vowel_wolof(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG WOLOF

        Thuật toán:
        - Y LUÔN LÀ PHỤ ÂM trong từ gốc Wolof

        Lưu ý: Tiếng Wolof là ngôn ngữ Tây Phi (Senegal),
        Y (orthography Latin) luôn là phụ âm /j/
        """
        return False  # Y luôn là phụ âm

    def _is_y_vowel_yoruba(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG YORUBA

        Thuật toán:
        - Y LUÔN LÀ PHỤ ÂM trong từ gốc Yoruba

        Lưu ý: Tiếng Yoruba là ngôn ngữ Tây Phi (Nigeria),
        Y (orthography Latin) luôn là phụ âm /j/
        """
        return False  # Y luôn là phụ âm

    def _is_y_vowel_arabic(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG Ả RẬP (phiên âm Latin)

        Thuật toán MỚI (7 quy tắc):
        1. Y phiên âm từ "ي" (ya) đầu từ/sau phụ âm → PHỤ ÂM (YASIR, YAHYA, ZAYN)
        2. Y giữa 2 nguyên âm → PHỤ ÂM (RAYAN, LAYALI)
        3. YY kép (gemination "يّ") → PHỤ ÂM GẤP ĐÔI (SAYYID, WAYYIB)
        4. Y cuối từ → NGUYÊN ÂM (ALI علي, ZAKY زكي, HANY هاني)
        5. AY/EY/OY cuối từ → Y = NGUYÊN ÂM (FAYSAL, ZAYD)
        6. Y giữa 2 phụ âm → NGUYÊN ÂM (hiếm)
        7. Còn lại → PHỤ ÂM
        """
        # Rule 3: YY kép → PHỤ ÂM (xử lý như 1 âm phụ âm kéo dài)
        if position > 0 and word[position - 1] == 'Y':
            return False  # Y thứ 2 trong YY → PHỤ ÂM
        if position < len(word) - 1 and word[position + 1] == 'Y':
            return False  # Y thứ 1 trong YY → PHỤ ÂM

        # Rule 4 & 5: Y cuối từ → NGUYÊN ÂM
        if position == len(word) - 1:
            if position > 0:
                prev_char = word[position - 1]
                # Rule 5: AY/EY/OY cuối từ → NGUYÊN ÂM
                if prev_char in ['A', 'E', 'O']:
                    return True
            # Rule 4: Y cuối từ bất kỳ → NGUYÊN ÂM
            return True

        # Rule 1: Y đầu từ + sau là nguyên âm → PHỤ ÂM (phiên âm "ي")
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 1: Y sau phụ âm + trước nguyên âm → PHỤ ÂM (phiên âm "ي")
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 2: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 6: Y giữa 2 phụ âm → NGUYÊN ÂM (hiếm)
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 7: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_thai(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG THÁI (phiên âm Latin)

        Thuật toán MỚI (5 quy tắc):
        1. Y đầu từ hoặc sau phụ âm + trước nguyên âm → PHỤ ÂM (YAI, THAYA)
        2. Y trong diphthongs AI/AY/OI/OY/UI/UY cuối từ → NGUYÊN ÂM (SOMCHAI, THWAY)
        3. Y cuối từ đứng độc lập → NGUYÊN ÂM
        4. Y giữa 2 phụ âm → NGUYÊN ÂM (từ mượn)
        5. Còn lại → PHỤ ÂM
        """
        # Rule 2: Y trong diphthongs AI/AY/OI/OY/UI/UY cuối từ → NGUYÊN ÂM
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in ['A', 'E', 'I', 'O', 'U']:
                return True

        # Rule 3: Y cuối từ đứng độc lập → NGUYÊN ÂM
        if position == len(word) - 1:
            return True

        # Rule 4: Y giữa 2 phụ âm → NGUYÊN ÂM (từ mượn)
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 1: Y đầu từ + trước nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 1: Y sau phụ âm + trước nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 5: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_tagalog(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG TAGALOG

        Thuật toán MỚI (6 quy tắc, BỎ rule "yy"):
        1. Y đầu từ + nguyên âm → PHỤ ÂM (YAYA, YERO)
        2. Y giữa 2 nguyên âm → PHỤ ÂM (SAYA, MAYA)
        3. Y sau phụ âm + trước nguyên âm → PHỤ ÂM (LIYAB)
        4. Y cuối từ trong AY/EY/OY/UY → NGUYÊN ÂM (BABOY, BAHAY, PINOY)
        5. Y giữa 2 phụ âm → NGUYÊN ÂM (hiếm)
        6. Còn lại → PHỤ ÂM

        Lưu ý: BỎ rule 7 về "yy" vì không phổ biến trong Tagalog gốc
        """
        # Rule 4: Y cuối từ trong AY/EY/OY/UY → NGUYÊN ÂM
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in ['A', 'E', 'O', 'U']:
                return True

        # Rule 1: Y đầu từ + sau là nguyên âm → PHỤ ÂM
        if position == 0 and len(word) > 1:
            next_char = word[1]
            if next_char in self.VOWELS:
                return False

        # Rule 2: Y giữa 2 nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Y sau phụ âm + trước nguyên âm → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 5: Y giữa 2 phụ âm → NGUYÊN ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char not in self.VOWELS:
                return True

        # Rule 6: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_burmese(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG BURMESE (phiên âm Latin)

        Thuật toán:
        1. Y = PHỤ ÂM khi nó đứng giữa phụ âm và nguyên âm (C–Y–V)
        2. Y = NGUYÊN ÂM khi nằm ở cuối AY/EY/OY/UY hoặc trong từ mượn tiếng Anh
        3. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 2: Y cuối các nguyên âm đôi AY/EY/OY/UY → NGUYÊN ÂM
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in ['A', 'E', 'O', 'U']:
                return True

        # Rule 1: Y giữa phụ âm và nguyên âm (C-Y-V) → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 3: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_sinhala(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG SINHALA (phiên âm Latin)

        Thuật toán:
        1. Y = PHỤ ÂM khi nằm giữa phụ âm–nguyên âm (C–Y–V) hoặc đứng đầu từ
        2. Y = NGUYÊN ÂM khi đứng cuối trong diphthongs AY/EY/OY/UY
        3. Nếu Y là nguyên âm duy nhất ⇒ NGUYÊN ÂM
        4. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 3: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 2: Y cuối các diphthongs AY/EY/OY/UY → NGUYÊN ÂM
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in ['A', 'E', 'O', 'U']:
                return True

        # Rule 1a: Y đầu từ → PHỤ ÂM
        if position == 0:
            return False

        # Rule 1b: Y giữa phụ âm và nguyên âm (C-Y-V) → PHỤ ÂM
        if position > 0 and position < len(word) - 1:
            prev_char = word[position - 1]
            next_char = word[position + 1]
            if prev_char not in self.VOWELS and next_char in self.VOWELS:
                return False

        # Rule 4: Còn lại → PHỤ ÂM
        return False

    def _is_y_vowel_nepali(self, word: str, position: int) -> bool:
        """
        Xác định Y là nguyên âm hay phụ âm theo quy tắc TIẾNG NEPALI (phiên âm Latin)

        Thuật toán:
        1. Y = PHỤ ÂM khi đứng trước nguyên âm (C–Y–V hoặc Y–V)
        2. Y = NGUYÊN ÂM khi là phần cuối của diphthong AY/EY/OY/UY
        3. Nếu Y là nguyên âm duy nhất ⇒ NGUYÊN ÂM
        4. Còn lại ⇒ PHỤ ÂM
        """
        # Rule 3: Y là nguyên âm duy nhất
        vowel_count = sum(1 for c in word if c in self.VOWELS)
        if vowel_count == 0:
            return True

        # Rule 2: Y cuối diphthongs AY/EY/OY/UY → NGUYÊN ÂM
        if position > 0 and position == len(word) - 1:
            prev_char = word[position - 1]
            if prev_char in ['A', 'E', 'O', 'U']:
                return True

        # Rule 1: Y trước nguyên âm → PHỤ ÂM
        if position < len(word) - 1:
            next_char = word[position + 1]
            if next_char in self.VOWELS:
                return False

        # Rule 4: Còn lại → PHỤ ÂM
        return False

    def _reduce_to_single_digit(self, number: int, keep_master: bool = True) -> int:
        """
        Rút gọn số thành một chữ số (1-9)
        Giữ nguyên Master Numbers (11, 22, 33) nếu keep_master=True

        Args:
            number: Số cần rút gọn
            keep_master: Có giữ Master Numbers hay không
        """
        while number > 9:
            # Kiểm tra Master Numbers
            if keep_master and number in self.MASTER_NUMBERS:
                return number

            # Rút gọn bằng cách cộng các chữ số
            number = sum(int(digit) for digit in str(number))

        return number

    def _letter_to_number(self, letter: str) -> int:
        """
        Chuyển đổi chữ cái thành số
        """
        letter = letter.upper()
        return self.LETTER_VALUES.get(letter, 0)

    def _calculate_name_number(self, name: str, vowels_only: bool = False,
                               consonants_only: bool = False) -> int:
        """
        Tính số từ tên theo Name Component Reduction Method

        Phương pháp: Rút gọn từng phần tên (First, Middle, Last) trước khi cộng
        - Giữ Master Numbers (11, 22, 33) trong quá trình rút gọn
        - Tôn trọng ý nghĩa riêng của từng phần tên

        Args:
            name: Tên cần tính
            vowels_only: Chỉ tính nguyên âm
            consonants_only: Chỉ tính phụ âm

        Example:
            "NGUYEN THI UYEN YEN"
            → NGUYEN: 5+7+3+1+5+5 = 26 → 2+6 = 8
            → THI:    2+8+9       = 19 → 1+9 = 10 → 1+0 = 1
            → UYEN:   3+1+5+5     = 14 → 1+4 = 5
            → YEN:    1+5+5       = 11 (Master Number, giữ nguyên)
            → Total:  8 + 1 + 5 + 11 = 25 → 2+5 = 7
        """
        component_totals = []
        words = name.split()

        # Tính tổng cho từng component (word)
        for word in words:
            word_total = 0
            for i, letter in enumerate(word):
                if letter not in self.LETTER_VALUES:
                    continue

                is_vowel = self._is_vowel(letter, word, i)

                if vowels_only and not is_vowel:
                    continue
                if consonants_only and is_vowel:
                    continue

                word_total += self._letter_to_number(letter)

            # Rút gọn từng component (giữ Master Numbers)
            if word_total > 0:
                word_reduced = self._reduce_to_single_digit(word_total)
                component_totals.append(word_reduced)

        # Cộng các component đã rút gọn
        total = sum(component_totals)

        # Rút gọn tổng cuối cùng (giữ Master Numbers)
        return self._reduce_to_single_digit(total)

    def _get_letter_frequency(self, name: str) -> Dict[int, int]:
        """
        Đếm tần suất xuất hiện của mỗi số (1-9) trong tên
        """
        frequency = {i: 0 for i in range(1, 10)}

        for letter in name.replace(' ', ''):
            if letter in self.LETTER_VALUES:
                number = self._letter_to_number(letter)
                frequency[number] += 1

        return frequency

    # ========== CÁC CHỈ SỐ CHÍNH ==========

    def life_path_number(self) -> int:
        """
        Chỉ Số Đường Đời (Life Path Number) ⭐⭐⭐⭐⭐
        Chỉ số quan trọng nhất, thể hiện mục đích và hướng đi của cuộc đời

        Cách tính: Cộng tất cả các chữ số trong ngày sinh, giữ Master Numbers
        """
        day = self.birth_date.day
        month = self.birth_date.month
        year = self.birth_date.year

        # Rút gọn từng phần nhưng giữ Master Numbers
        day_reduced = self._reduce_to_single_digit(day)
        month_reduced = self._reduce_to_single_digit(month)
        year_reduced = self._reduce_to_single_digit(year)

        total = day_reduced + month_reduced + year_reduced

        return self._reduce_to_single_digit(total)

    def expression_number(self) -> int:
        """
        Chỉ Số Biểu Đạt (Expression Number / Destiny Number) ⭐⭐⭐⭐⭐
        Thể hiện tài năng, khả năng và số mệnh của bạn

        Cách tính: Tổng giá trị của TẤT CẢ các chữ cái trong tên đầy đủ
        """
        return self._calculate_name_number(self.full_name)

    def soul_urge_number(self) -> int:
        """
        Chỉ Số Linh Hồn / Khát Khao Tâm Hồn (Soul Urge Number / Heart's Desire) ⭐⭐⭐⭐⭐
        Thể hiện mong muốn nội tâm, động lực sâu xa

        Cách tính: Tổng giá trị của các NGUYÊN ÂM trong tên
        """
        return self._calculate_name_number(self.full_name, vowels_only=True)

    def personality_number(self) -> int:
        """
        Chỉ Số Nhân Cách (Personality Number) ⭐⭐⭐⭐
        Thể hiện ấn tượng ban đầu, cách người khác nhìn nhận bạn

        Cách tính: Tổng giá trị của các PHỤ ÂM trong tên
        """
        return self._calculate_name_number(self.full_name, consonants_only=True)

    def birthday_number(self) -> int:
        """
        Chỉ Số Ngày Sinh (Birthday Number) ⭐⭐⭐
        Thể hiện tài năng đặc biệt bạn mang theo từ khi sinh ra

        Cách tính: Rút gọn ngày sinh (chỉ ngày, không tính tháng/năm)
        """
        return self._reduce_to_single_digit(self.birth_date.day)

    def maturity_number(self) -> int:
        """
        Số Trưởng Thành (Maturity Number / Reality Number) ⭐⭐⭐
        Thể hiện mục tiêu cuộc đời, điều bạn hướng tới khi trưởng thành

        Cách tính: Tổng của Life Path Number và Expression Number
        """
        lp = self.life_path_number()
        exp = self.expression_number()
        return self._reduce_to_single_digit(lp + exp)

    def balance_number(self) -> int:
        """
        Số Cân Bằng (Balance Number) ⭐⭐⭐
        Cách bạn đối phó với thử thách và khó khăn

        Cách tính: Tổng giá trị của chữ cái ĐẦU TIÊN của mỗi tên
        """
        words = self.full_name.split()
        total = sum(self._letter_to_number(word[0]) for word in words if word)
        return self._reduce_to_single_digit(total)

    def life_path_expression_bridge(self) -> int:
        """
        Cầu Nối Đường Đời - Biểu Đạt (Life Path - Expression Bridge) ⭐⭐⭐⭐
        Khoảng cách giữa đường đời và tài năng bẩm sinh

        Cách tính: |Life Path Number - Expression Number|
        Số càng nhỏ = càng hài hòa giữa mục đích sống và khả năng tự nhiên
        """
        lp = self.life_path_number()
        exp = self.expression_number()
        return abs(lp - exp)

    def soul_urge_personality_bridge(self) -> int:
        """
        Cầu Nối Linh Hồn - Nhân Cách (Soul Urge - Personality Bridge) ⭐⭐⭐⭐
        Khoảng cách giữa mong muốn nội tâm và hình ảnh bên ngoài

        Cách tính: |Soul Urge Number - Personality Number|
        Số càng nhỏ = càng chân thực giữa cái bạn muốn và cái bạn thể hiện
        """
        su = self.soul_urge_number()
        per = self.personality_number()
        return abs(su - per)

    def personal_year_number(self, current_year: Optional[int] = None) -> int:
        """
        Năm Cá Nhân (Personal Year Number) ⭐⭐⭐⭐
        Chu kỳ năm hiện tại, năng lượng và chủ đề của năm

        Cách tính: Ngày sinh + Tháng sinh + Năm hiện tại (rút gọn)
        Lưu ý: Personal Year KHÔNG giữ Master Numbers vì là chu kỳ ngắn hạn

        Args:
            current_year: Năm cần tính (mặc định là năm hiện tại)

        Returns:
            Personal Year Number (1-9, KHÔNG có 11/22/33)
        """
        if current_year is None:
            current_year = datetime.now().year

        day = self.birth_date.day
        month = self.birth_date.month

        # Rút gọn từng phần
        day_reduced = self._reduce_to_single_digit(day, keep_master=False)
        month_reduced = self._reduce_to_single_digit(month, keep_master=False)
        year_reduced = self._reduce_to_single_digit(current_year, keep_master=False)

        total = day_reduced + month_reduced + year_reduced

        # Personal Year KHÔNG giữ Master Numbers
        return self._reduce_to_single_digit(total, keep_master=False)

    def personal_month_number(self, current_month: int, current_year: Optional[int] = None) -> int:
        """
        Tháng Cá Nhân (Personal Month Number) ⭐⭐⭐
        Năng lượng và chủ đề của tháng cụ thể trong năm

        Cách tính: Personal Year + Tháng hiện tại (rút gọn)
        Lưu ý: Personal Month KHÔNG giữ Master Numbers

        Args:
            current_month: Tháng cần tính (1-12)
            current_year: Năm cần tính (mặc định là năm hiện tại)

        Returns:
            Personal Month Number (1-9, KHÔNG có 11/22/33)
        """
        if current_year is None:
            current_year = datetime.now().year

        personal_year = self.personal_year_number(current_year)
        month_reduced = self._reduce_to_single_digit(current_month, keep_master=False)

        total = personal_year + month_reduced

        # Personal Month KHÔNG giữ Master Numbers
        return self._reduce_to_single_digit(total, keep_master=False)

    def rational_thought_number(self) -> int:
        """
        Chỉ Số Tư Duy Lý Trí (Rational Thought Number) ⭐⭐⭐
        Cách bạn xử lý thông tin và ra quyết định

        Cách tính: Chữ cái đầu của TÊN ĐẦU TIÊN + Chữ cái đầu của HỌ (tên cuối)

        Returns:
            Rational Thought Number (1-9 hoặc 11, 22)
        """
        words = self.full_name.split()

        if len(words) == 0:
            return 1

        # Chữ cái đầu của tên đầu tiên
        first_name_initial = words[0][0] if len(words[0]) > 0 else ''

        # Chữ cái đầu của họ (tên cuối cùng)
        last_name_initial = words[-1][0] if len(words) > 0 and len(words[-1]) > 0 else ''

        if not first_name_initial or not last_name_initial:
            return 1

        total = self._letter_to_number(first_name_initial) + self._letter_to_number(last_name_initial)

        return self._reduce_to_single_digit(total)

    def cornerstone(self) -> Tuple[str, int]:
        """
        Đá Góc (Cornerstone) ⭐⭐
        Chữ cái đầu tiên của tên, thể hiện cách bạn tiếp cận cơ hội và thử thách

        Returns:
            Tuple (chữ cái, giá trị số)
        """
        first_letter = self.full_name.replace(' ', '')[0]
        return (first_letter, self._letter_to_number(first_letter))

    def capstone(self) -> Tuple[str, int]:
        """
        Đá Chóp (Capstone) ⭐⭐
        Chữ cái cuối cùng của TÊN ĐẦU TIÊN, thể hiện khả năng hoàn thành công việc

        Returns:
            Tuple (chữ cái, giá trị số)
        """
        first_name = self.full_name.split()[0]  # Lấy tên đầu tiên
        last_letter = first_name[-1]  # Chữ cái cuối của tên đầu tiên
        return (last_letter, self._letter_to_number(last_letter))

    def hidden_passion_number(self) -> int:
        """
        Đam Mê Ẩn (Hidden Passion Number) ⭐⭐⭐
        Điều bạn đam mê nhất, số xuất hiện nhiều nhất trong tên

        Returns:
            Số có tần suất xuất hiện cao nhất (1-9)
        """
        frequency = self._get_letter_frequency(self.full_name)
        max_count = max(frequency.values())

        # Nếu có nhiều số cùng tần suất cao nhất, chọn số nhỏ nhất
        for num in range(1, 10):
            if frequency[num] == max_count:
                return num

        return 1

    def karmic_lesson_numbers(self) -> List[int]:
        """
        Bài Học Nghiệp (Karmic Lesson Numbers) ⭐⭐⭐
        Các số KHÔNG xuất hiện hoặc xuất hiện ít trong tên
        Thể hiện điểm yếu hoặc bài học cần học

        Returns:
            List các số từ 1-9 không có trong tên
        """
        frequency = self._get_letter_frequency(self.full_name)
        return [num for num in range(1, 10) if frequency[num] == 0]

    def subconscious_self(self) -> int:
        """
        Tiềm Thức (Subconscious Self) ⭐⭐
        Thể hiện sự tự tin và khả năng đối phó với tình huống khẩn cấp

        Cách tính: Đếm số lượng các số KHÁC NHAU (1-9) có trong tên
        """
        frequency = self._get_letter_frequency(self.full_name)
        return sum(1 for count in frequency.values() if count > 0)

    def pinnacle_numbers(self) -> Dict[str, Dict]:
        """
        4 Đỉnh Cao (Pinnacle Numbers) ⭐⭐⭐⭐
        4 giai đoạn chính trong cuộc đời, mỗi giai đoạn kéo dài 9 năm

        Returns:
            Dictionary chứa 4 Pinnacle với số và khoảng tuổi
        """
        day = self.birth_date.day
        month = self.birth_date.month
        year = self.birth_date.year

        # Rút gọn các thành phần
        day_reduced = self._reduce_to_single_digit(day)
        month_reduced = self._reduce_to_single_digit(month)
        year_reduced = self._reduce_to_single_digit(year)

        # Tính 4 Pinnacle Numbers
        first_pinnacle = self._reduce_to_single_digit(month_reduced + day_reduced)
        second_pinnacle = self._reduce_to_single_digit(day_reduced + year_reduced)
        third_pinnacle = self._reduce_to_single_digit(first_pinnacle + second_pinnacle)
        fourth_pinnacle = self._reduce_to_single_digit(month_reduced + year_reduced)

        # Tính tuổi bắt đầu mỗi giai đoạn
        life_path = self.life_path_number()
        first_cycle_end = 36 - life_path

        return {
            'pinnacle_1': {
                'number': first_pinnacle,
                'age_range': f'0 - {first_cycle_end}',
                'start_age': 0,
                'end_age': first_cycle_end
            },
            'pinnacle_2': {
                'number': second_pinnacle,
                'age_range': f'{first_cycle_end + 1} - {first_cycle_end + 9}',
                'start_age': first_cycle_end + 1,
                'end_age': first_cycle_end + 9
            },
            'pinnacle_3': {
                'number': third_pinnacle,
                'age_range': f'{first_cycle_end + 10} - {first_cycle_end + 18}',
                'start_age': first_cycle_end + 10,
                'end_age': first_cycle_end + 18
            },
            'pinnacle_4': {
                'number': fourth_pinnacle,
                'age_range': f'{first_cycle_end + 19}+',
                'start_age': first_cycle_end + 19,
                'end_age': None
            }
        }

    def challenge_numbers(self) -> Dict[str, Dict]:
        """
        4 Số Thử Thách (Challenge Numbers) ⭐⭐⭐⭐
        Các thử thách bạn phải đối mặt trong từng giai đoạn cuộc đời

        Returns:
            Dictionary chứa 4 Challenge Numbers
        """
        day = self.birth_date.day
        month = self.birth_date.month
        year = self.birth_date.year

        # Rút gọn các thành phần
        day_reduced = self._reduce_to_single_digit(day)
        month_reduced = self._reduce_to_single_digit(month)
        year_reduced = self._reduce_to_single_digit(year)

        # Tính Challenge Numbers (lấy giá trị tuyệt đối của hiệu)
        first_challenge = abs(month_reduced - day_reduced)
        second_challenge = abs(day_reduced - year_reduced)
        third_challenge = abs(first_challenge - second_challenge)
        fourth_challenge = abs(month_reduced - year_reduced)

        # Tính tuổi bắt đầu mỗi giai đoạn (giống Pinnacle)
        life_path = self.life_path_number()
        first_cycle_end = 36 - life_path

        return {
            'challenge_1': {
                'number': first_challenge,
                'age_range': f'0 - {first_cycle_end}',
                'start_age': 0,
                'end_age': first_cycle_end
            },
            'challenge_2': {
                'number': second_challenge,
                'age_range': f'{first_cycle_end + 1} - {first_cycle_end + 9}',
                'start_age': first_cycle_end + 1,
                'end_age': first_cycle_end + 9
            },
            'challenge_3': {
                'number': third_challenge,
                'age_range': f'{first_cycle_end + 10} - {first_cycle_end + 18}',
                'start_age': first_cycle_end + 10,
                'end_age': first_cycle_end + 18
            },
            'challenge_4': {
                'number': fourth_challenge,
                'age_range': f'{first_cycle_end + 19}+',
                'start_age': first_cycle_end + 19,
                'end_age': None
            }
        }

    def get_interpretation(self, category: str, number: int) -> Dict:
        """
        Lấy luận giải cho một chỉ số cụ thể

        Args:
            category: Loại chỉ số ('life_path', 'expression', 'soul_urge', 'personality', 'birthday')
            number: Số cần luận giải

        Returns:
            Dictionary chứa luận giải
        """
        if not INTERPRETATIONS_AVAILABLE:
            return {"error": "Interpretations module not available"}

        return get_interpretation(category, number)

    def get_all_numbers(self) -> Dict:
        """
        Lấy tất cả các chỉ số Numerology

        Returns:
            Dictionary chứa tất cả các chỉ số
        """
        cornerstone_letter, cornerstone_value = self.cornerstone()
        capstone_letter, capstone_value = self.capstone()

        return {
            'personal_info': {
                'original_name': self.original_name,
                'full_name': self.full_name,
                'birth_date': self.birth_date.strftime('%d/%m/%Y')
            },
            'core_numbers': {
                'life_path': self.life_path_number(),
                'expression': self.expression_number(),
                'soul_urge': self.soul_urge_number(),
                'personality': self.personality_number(),
                'birthday': self.birthday_number()
            },
            'secondary_numbers': {
                'maturity': self.maturity_number(),
                'balance': self.balance_number(),
                'hidden_passion': self.hidden_passion_number(),
                'subconscious_self': self.subconscious_self()
            },
            'bridge_numbers': {
                'life_path_expression_bridge': self.life_path_expression_bridge(),
                'soul_urge_personality_bridge': self.soul_urge_personality_bridge()
            },
            'cycle_numbers': {
                'personal_year': self.personal_year_number(),
                'personal_month': self.personal_month_number(datetime.now().month),
                'rational_thought': self.rational_thought_number()
            },
            'name_analysis': {
                'cornerstone': {
                    'letter': cornerstone_letter,
                    'value': cornerstone_value
                },
                'capstone': {
                    'letter': capstone_letter,
                    'value': capstone_value
                },
                'karmic_lessons': self.karmic_lesson_numbers()
            },
            'life_cycles': {
                'pinnacles': self.pinnacle_numbers(),
                'challenges': self.challenge_numbers()
            }
        }

    def get_all_numbers_with_interpretations(self) -> Dict:
        """
        Lấy tất cả các chỉ số Numerology KÈM THEO luận giải

        Returns:
            Dictionary chứa tất cả các chỉ số và luận giải tương ứng
        """
        cornerstone_letter, cornerstone_value = self.cornerstone()
        capstone_letter, capstone_value = self.capstone()

        # Core numbers
        life_path = self.life_path_number()
        expression = self.expression_number()
        soul_urge = self.soul_urge_number()
        personality = self.personality_number()
        birthday = self.birthday_number()

        # Bridge numbers
        lp_exp_bridge = self.life_path_expression_bridge()
        su_per_bridge = self.soul_urge_personality_bridge()

        # Cycle numbers
        personal_year = self.personal_year_number()
        personal_month = self.personal_month_number(datetime.now().month)
        rational_thought = self.rational_thought_number()

        result = {
            'personal_info': {
                'original_name': self.original_name,
                'full_name': self.full_name,
                'birth_date': self.birth_date.strftime('%d/%m/%Y')
            },
            'core_numbers': {
                'life_path': {
                    'number': life_path,
                    'interpretation': self.get_interpretation('life_path', life_path) if INTERPRETATIONS_AVAILABLE else None
                },
                'expression': {
                    'number': expression,
                    'interpretation': self.get_interpretation('expression', expression) if INTERPRETATIONS_AVAILABLE else None
                },
                'soul_urge': {
                    'number': soul_urge,
                    'interpretation': self.get_interpretation('soul_urge', soul_urge) if INTERPRETATIONS_AVAILABLE else None
                },
                'personality': {
                    'number': personality,
                    'interpretation': self.get_interpretation('personality', personality) if INTERPRETATIONS_AVAILABLE else None
                },
                'birthday': {
                    'number': birthday,
                    'interpretation': self.get_interpretation('birthday', birthday) if INTERPRETATIONS_AVAILABLE else None
                }
            },
            'secondary_numbers': {
                'maturity': self.maturity_number(),
                'balance': self.balance_number(),
                'hidden_passion': self.hidden_passion_number(),
                'subconscious_self': self.subconscious_self()
            },
            'bridge_numbers': {
                'life_path_expression_bridge': {
                    'number': lp_exp_bridge,
                    'interpretation': self.get_interpretation('life_path_expression_bridge', lp_exp_bridge) if INTERPRETATIONS_AVAILABLE else None
                },
                'soul_urge_personality_bridge': {
                    'number': su_per_bridge,
                    'interpretation': self.get_interpretation('soul_urge_personality_bridge', su_per_bridge) if INTERPRETATIONS_AVAILABLE else None
                }
            },
            'cycle_numbers': {
                'personal_year': {
                    'number': personal_year,
                    'interpretation': self.get_interpretation('personal_year', personal_year) if INTERPRETATIONS_AVAILABLE else None
                },
                'personal_month': {
                    'number': personal_month,
                    'interpretation': self.get_interpretation('personal_month', personal_month) if INTERPRETATIONS_AVAILABLE else None
                },
                'rational_thought': {
                    'number': rational_thought,
                    'interpretation': self.get_interpretation('rational_thought', rational_thought) if INTERPRETATIONS_AVAILABLE else None
                }
            },
            'name_analysis': {
                'cornerstone': {
                    'letter': cornerstone_letter,
                    'value': cornerstone_value
                },
                'capstone': {
                    'letter': capstone_letter,
                    'value': capstone_value
                },
                'karmic_lessons': self.karmic_lesson_numbers()
            },
            'life_cycles': {
                'pinnacles': self.pinnacle_numbers(),
                'challenges': self.challenge_numbers()
            }
        }

        return result

    def print_report(self):
        """
        In báo cáo chi tiết về tất cả các chỉ số
        """
        data = self.get_all_numbers()

        print("=" * 70)
        print("BÁOÁO THẦN SỐ HỌC (NUMEROLOGY REPORT)".center(70))
        print("=" * 70)

        print(f"\nThông tin cá nhân:")
        if data['personal_info']['original_name'] != data['personal_info']['full_name']:
            print(f"  Tên gốc: {data['personal_info']['original_name']}")
        print(f"  Tên đầy đủ: {data['personal_info']['full_name']}")
        print(f"  Ngày sinh: {data['personal_info']['birth_date']}")

        print("\n" + "=" * 70)
        print("CÁC CHỈ SỐ CHÍNH (CORE NUMBERS)".center(70))
        print("=" * 70)

        print(f"\n⭐ Chỉ Số Đường Đời (Life Path): {data['core_numbers']['life_path']}")
        print("   → Mục đích và hướng đi của cuộc đời")

        print(f"\n⭐ Chỉ Số Biểu Đạt (Expression): {data['core_numbers']['expression']}")
        print("   → Tài năng và khả năng bẩm sinh")

        print(f"\n⭐ Chỉ Số Linh Hồn (Soul Urge): {data['core_numbers']['soul_urge']}")
        print("   → Mong muốn nội tâm, động lực sâu xa")

        print(f"\n⭐ Chỉ Số Nhân Cách (Personality): {data['core_numbers']['personality']}")
        print("   → Ấn tượng ban đầu với người khác")

        print(f"\n⭐ Chỉ Số Ngày Sinh (Birthday): {data['core_numbers']['birthday']}")
        print("   → Tài năng đặc biệt từ khi sinh ra")

        print("\n" + "=" * 70)
        print("CÁC CHỈ SỐ PHỤ (SECONDARY NUMBERS)".center(70))
        print("=" * 70)

        print(f"\n⭐ Số Trưởng Thành (Maturity): {data['secondary_numbers']['maturity']}")
        print("   → Mục tiêu khi trưởng thành")

        print(f"\n⭐ Số Cân Bằng (Balance): {data['secondary_numbers']['balance']}")
        print("   → Cách đối phó với khó khăn")

        print(f"\n⭐ Đam Mê Ẩn (Hidden Passion): {data['secondary_numbers']['hidden_passion']}")
        print("   → Điều bạn đam mê nhất")

        print(f"\n⭐ Tiềm Thức (Subconscious Self): {data['secondary_numbers']['subconscious_self']}")
        print("   → Sự tự tin trong tình huống khẩn cấp")

        print("\n" + "=" * 70)
        print("CÁC SỐ CẦU NỐI (BRIDGE NUMBERS)".center(70))
        print("=" * 70)

        print(f"\n⭐ Cầu Nối Đường Đời - Biểu Đạt: {data['bridge_numbers']['life_path_expression_bridge']}")
        print("   → Khoảng cách giữa mục đích sống và tài năng bẩm sinh")
        print(f"   → Mức độ hài hòa: {'Càng gần 0 càng hài hòa'}")

        print(f"\n⭐ Cầu Nối Linh Hồn - Nhân Cách: {data['bridge_numbers']['soul_urge_personality_bridge']}")
        print("   → Khoảng cách giữa mong muốn nội tâm và hình ảnh bên ngoài")
        print(f"   → Mức độ chân thực: {'Càng gần 0 càng chân thực'}")

        print("\n" + "=" * 70)
        print("CHU KỲ VÀ TƯ DUY (CYCLES & THINKING)".center(70))
        print("=" * 70)

        current_year = datetime.now().year
        current_month_name = datetime.now().strftime("%B")  # Tên tháng

        print(f"\n⭐ Năm Cá Nhân {current_year} (Personal Year): {data['cycle_numbers']['personal_year']}")
        print("   → Năng lượng và chủ đề của năm hiện tại")

        print(f"\n⭐ Tháng Cá Nhân {current_month_name} (Personal Month): {data['cycle_numbers']['personal_month']}")
        print("   → Năng lượng và chủ đề của tháng hiện tại")

        print(f"\n⭐ Số Tư Duy Lý Trí (Rational Thought): {data['cycle_numbers']['rational_thought']}")
        print("   → Cách bạn xử lý thông tin và ra quyết định")

        print("\n" + "=" * 70)
        print("PHÂN TÍCH TÊN (NAME ANALYSIS)".center(70))
        print("=" * 70)

        print(f"\n⭐ Đá Góc (Cornerstone): {data['name_analysis']['cornerstone']['letter']} = {data['name_analysis']['cornerstone']['value']}")
        print("   → Cách tiếp cận cơ hội")

        print(f"\n⭐ Đá Chóp (Capstone): {data['name_analysis']['capstone']['letter']} = {data['name_analysis']['capstone']['value']}")
        print("   → Khả năng hoàn thành công việc")

        karmic = data['name_analysis']['karmic_lessons']
        if karmic:
            print(f"\n⭐ Bài Học Nghiệp (Karmic Lessons): {', '.join(map(str, karmic))}")
            print("   → Điểm yếu hoặc bài học cần học")
        else:
            print(f"\n⭐ Bài Học Nghiệp (Karmic Lessons): Không có")
            print("   → Bạn có đầy đủ tất cả các số!")

        print("\n" + "=" * 70)
        print("CHU KỲ CUỘC ĐỜI (LIFE CYCLES)".center(70))
        print("=" * 70)

        print("\n⭐ 4 Đỉnh Cao (Pinnacles):")
        for key, pinnacle in data['life_cycles']['pinnacles'].items():
            print(f"   {key}: Số {pinnacle['number']} (Tuổi {pinnacle['age_range']})")

        print("\n⭐ 4 Thử Thách (Challenges):")
        for key, challenge in data['life_cycles']['challenges'].items():
            print(f"   {key}: Số {challenge['number']} (Tuổi {challenge['age_range']})")

        print("\n" + "=" * 70)

    def get_extended_report(self) -> Dict:
        """
        Tạo báo cáo mở rộng với metadata, age, importance, ai_context
        Version 2.1: Improved key names for better AI comprehension
        - Renamed 'data' to 'all_pinnacles' and 'all_challenges'
        - Renamed 'details' to 'master_numbers_found'

        Returns:
            Dict với structure đầy đủ để AI dễ luận giải
        """
        from datetime import datetime

        # Get standard output first
        standard_data = self.get_all_numbers_with_interpretations()

        # Calculate age
        birth = self.birth_date
        today = datetime.now()
        age = (today - birth).days // 365

        # Format birth_date as string
        birth_date_str = birth.strftime('%d/%m/%Y')

        # Helper function to check if number is Master Number
        def is_master_number(num):
            return num in [11, 22, 33]

        # Helper function to get simple interpretation for a number
        def get_simple_interpretation(number, context='general'):
            """Get simple interpretation for pinnacles/challenges/secondary numbers"""
            master_note = " (Master Number - Tiềm năng cao đặc biệt)" if is_master_number(number) else ""

            basic_meanings = {
                0: "Không thử thách đặc biệt, học tất cả",
                1: "Độc lập, lãnh đạo, tự chủ",
                2: "Hợp tác, kiên nhẫn, quan hệ",
                3: "Sáng tạo, giao tiếp, vui vẻ",
                4: "Kỷ luật, tổ chức, nền tảng",
                5: "Tự do, thay đổi, phiêu lưu",
                6: "Trách nhiệm, gia đình, chăm sóc",
                7: "Trí tuệ, phân tích, tâm linh",
                8: "Thành công, quyền lực, vật chất",
                9: "Hoàn thiện, từ bi, phục vụ",
                11: "Soi sáng, truyền cảm hứng, tâm linh cao",
                22: "Xây dựng vĩ đại, tầm nhìn lớn",
                33: "Giảng dạy, chữa lành, phục vụ cao nhất"
            }

            return {
                'theme': basic_meanings.get(number, 'Cần khám phá') + master_note,
                'is_master_number': is_master_number(number)
            }

        # Helper function to get importance stars
        def get_importance(category):
            importance_map = {
                'life_path': '⭐⭐⭐⭐⭐ Quan trọng nhất',
                'expression': '⭐⭐⭐⭐⭐ Rất quan trọng',
                'soul_urge': '⭐⭐⭐⭐⭐ Rất quan trọng',
                'personality': '⭐⭐⭐⭐ Quan trọng',
                'birthday': '⭐⭐⭐ Khá quan trọng',
                'maturity': '⭐⭐⭐ Khá quan trọng',
                'balance': '⭐⭐⭐ Khá quan trọng',
                'hidden_passion': '⭐⭐⭐ Khá quan trọng',
                'subconscious_self': '⭐⭐ Tham khảo',
                'cornerstone': '⭐⭐ Tham khảo',
                'capstone': '⭐⭐ Tham khảo',
                'karmic_lessons': '⭐⭐⭐ Khá quan trọng',
                'pinnacles': '⭐⭐⭐⭐ Rất quan trọng',
                'challenges': '⭐⭐⭐⭐ Rất quan trọng'
            }
            return importance_map.get(category, '⭐⭐⭐')

        # Helper function to get meaning
        def get_meaning(category):
            meaning_map = {
                'life_path': 'Mục đích và hướng đi của cuộc đời',
                'expression': 'Tài năng, khả năng và số mệnh bẩm sinh',
                'soul_urge': 'Mong muốn nội tâm và động lực sâu xa',
                'personality': 'Ấn tượng ban đầu, cách người khác nhìn nhận',
                'birthday': 'Tài năng đặc biệt mang theo từ khi sinh ra',
                'maturity': 'Mục tiêu và phẩm chất phát triển khi trưởng thành',
                'balance': 'Cách đối phó với khó khăn và thử thách',
                'hidden_passion': 'Đam mê và điều bạn yêu thích nhất',
                'subconscious_self': 'Tự tin và khả năng đối phó với tình huống khẩn cấp',
                'cornerstone': 'Cách tiếp cận cơ hội và thử thách',
                'capstone': 'Khả năng hoàn thành và kết thúc công việc',
                'karmic_lessons': 'Các bài học cần học, điểm yếu cần khắc phục',
                'pinnacles': '4 giai đoạn chính trong cuộc đời, mỗi giai đoạn mang cơ hội khác nhau',
                'challenges': '4 thử thách chính cần vượt qua trong từng giai đoạn cuộc đời'
            }
            return meaning_map.get(category, '')

        # Helper function to get Vietnamese name
        def get_vietnamese_name(category):
            name_map = {
                'life_path': 'Chỉ Số Đường Đời (Life Path Number)',
                'expression': 'Chỉ Số Biểu Đạt (Expression Number)',
                'soul_urge': 'Chỉ Số Linh Hồn (Soul Urge Number)',
                'personality': 'Chỉ Số Nhân Cách (Personality Number)',
                'birthday': 'Chỉ Số Ngày Sinh (Birthday Number)',
                'maturity': 'Số Trưởng Thành (Maturity Number)',
                'balance': 'Số Cân Bằng (Balance Number)',
                'hidden_passion': 'Đam Mê Ẩn (Hidden Passion Number)',
                'subconscious_self': 'Tiềm Thức (Subconscious Self)',
                'cornerstone': 'Đá Góc (Cornerstone)',
                'capstone': 'Đá Chóp (Capstone)',
                'karmic_lessons': 'Bài Học Nghiệp (Karmic Lessons)',
                'pinnacles': '4 Đỉnh Cao (Pinnacle Numbers)',
                'challenges': '4 Số Thử Thách (Challenge Numbers)'
            }
            return name_map.get(category, '')

        # Helper function to get AI context
        def get_ai_context(category, number=None):
            context_map = {
                'life_path': 'Đây là chỉ số quan trọng nhất, thể hiện con đường và sứ mệnh cuộc đời của người này.',
                'expression': 'Chỉ số này cho biết tài năng tự nhiên và cách người này thể hiện bản thân với thế giới.',
                'soul_urge': 'Đây là động lực nội tâm sâu xa nhất, những gì linh hồn người này thực sự khao khát.',
                'personality': 'Chỉ số này thể hiện hình ảnh bên ngoài và ấn tượng đầu tiên mà người này tạo ra.',
                'birthday': 'Một tài năng hoặc khả năng đặc biệt mà người này có từ khi sinh ra.',
                'maturity': 'Chỉ số này cho thấy người này sẽ phát triển và trưởng thành như thế nào theo thời gian.',
                'balance': 'Cách tự nhiên mà người này phản ứng và giải quyết vấn đề khi gặp khó khăn.',
                'hidden_passion': 'Điều mà người này có đam mê mãnh liệt nhất, thường thể hiện qua hành động.',
                'subconscious_self': f'Người này có {number if number else "X"} trên 9 số trong tên, cho thấy mức độ tự tin và nguồn lực nội tâm.',
                'cornerstone': 'Chữ cái đầu tiên cho thấy cách người này bắt đầu và tiếp cận mọi việc.',
                'capstone': 'Chữ cái cuối cùng cho thấy cách người này hoàn thành và kết thúc mọi việc.',
                'karmic_lessons': 'Những số KHÔNG xuất hiện trong tên, thể hiện các bài học mà người này cần học trong đời.'
            }
            return context_map.get(category, '')

        # Build extended report
        report = {
            'metadata': {
                'report_type': 'Numerology Complete Analysis',
                'generated_at': datetime.now().isoformat(),
                'version': '2.1',  # Updated version - improved key names
                'language': 'Vietnamese' if self.language == 'vi' else 'English'
            },

            'personal_information': {
                'original_name': standard_data['personal_info']['original_name'],
                'normalized_name': standard_data['personal_info']['full_name'],
                'birth_date': birth_date_str,
                'age': str(age)
            },

            'core_numbers': {},
            'secondary_numbers': {},
            'name_analysis': {},
            'life_cycles': {}
        }

        # Collect all numbers for master number analysis
        all_numbers = {}

        # Process core numbers
        for key in ['life_path', 'expression', 'soul_urge', 'personality', 'birthday']:
            num_data = standard_data['core_numbers'][key]
            num = num_data['number']
            all_numbers[key] = num

            report['core_numbers'][key] = {
                'number': num,
                'name': get_vietnamese_name(key),
                'importance': get_importance(key),
                'meaning': get_meaning(key),
                'interpretation': num_data.get('interpretation', {}),
                'ai_context': get_ai_context(key, num),
                'is_master_number': is_master_number(num)  # NEW
            }

        # Process secondary numbers with basic interpretations
        for key in ['maturity', 'balance', 'hidden_passion', 'subconscious_self']:
            if key in standard_data['secondary_numbers']:
                num_value = standard_data['secondary_numbers'][key]
                all_numbers[key] = num_value

                simple_interp = get_simple_interpretation(num_value, key)

                report['secondary_numbers'][key] = {
                    'number': num_value,
                    'name': get_vietnamese_name(key),
                    'importance': get_importance(key),
                    'meaning': get_meaning(key),
                    'interpretation': {  # NEW: Add basic interpretation
                        'theme': simple_interp['theme']
                    },
                    'ai_context': get_ai_context(key, num_value),
                    'is_master_number': simple_interp['is_master_number']  # NEW
                }

        # Process name analysis
        cornerstone = self.cornerstone()
        capstone = self.capstone()
        karmic_lessons = self.karmic_lesson_numbers()

        report['name_analysis'] = {
            'cornerstone': {
                'letter': cornerstone[0],
                'number': cornerstone[1],
                'name': get_vietnamese_name('cornerstone'),
                'importance': get_importance('cornerstone'),
                'meaning': get_meaning('cornerstone'),
                'interpretation': {
                    'meaning': f'Bạn tiếp cận cơ hội với chữ cái {cornerstone[0]} (số {cornerstone[1]}).'
                },
                'ai_context': get_ai_context('cornerstone').replace('Chữ cái đầu tiên', f"Chữ cái đầu tiên '{cornerstone[0]}'")
            },
            'capstone': {
                'letter': capstone[0],
                'number': capstone[1],
                'name': get_vietnamese_name('capstone'),
                'importance': get_importance('capstone'),
                'meaning': get_meaning('capstone'),
                'interpretation': {
                    'meaning': f'Bạn hoàn thành công việc với chữ cái {capstone[0]} (số {capstone[1]}).'
                },
                'ai_context': get_ai_context('capstone').replace('Chữ cái cuối cùng', f"Chữ cái cuối cùng '{capstone[0]}'")
            },
            'karmic_lessons': {
                'missing_numbers': karmic_lessons,
                'count': len(karmic_lessons),  # NEW
                'severity': 'low' if len(karmic_lessons) < 2 else ('moderate' if len(karmic_lessons) <= 3 else 'high'),  # NEW
                'name': get_vietnamese_name('karmic_lessons'),
                'importance': get_importance('karmic_lessons'),
                'meaning': get_meaning('karmic_lessons'),
                'interpretations': [],
                'ai_context': get_ai_context('karmic_lessons')
            }
        }

        # Add karmic lesson interpretations if available
        if INTERPRETATIONS_AVAILABLE:
            for num in karmic_lessons:
                interp = self.get_interpretation('karmic_lesson', num)
                if interp:
                    report['name_analysis']['karmic_lessons']['interpretations'].append({
                        'number': num,
                        'interpretation': interp
                    })

        # Process life cycles
        pinnacles = self.pinnacle_numbers()
        challenges = self.challenge_numbers()

        # Find current pinnacle and challenge
        current_pinnacle = None
        current_challenge = None

        pinnacle_list = []
        for stage, (key, pinnacle) in enumerate(pinnacles.items(), 1):
            age_range = pinnacle['age_range']
            # Parse age range (formats: "0 - 33" or "52+")
            if '+' in age_range:
                start_age = int(age_range.replace('+', '').strip())
                end_age = None
            else:
                parts = age_range.split('-')
                start_age = int(parts[0].strip())
                end_age = int(parts[1].strip())

            is_current = (age >= start_age and (end_age is None or age <= end_age))

            # Calculate years remaining
            years_remaining = None
            if is_current and end_age is not None:
                years_remaining = end_age - age

            # Get simple interpretation
            simple_interp = get_simple_interpretation(pinnacle['number'], 'pinnacle')

            pinnacle_data = {
                'stage': str(stage),
                'number': pinnacle['number'],
                'age_range': age_range,
                'start_age': start_age,
                'end_age': end_age,
                'interpretation': {  # NEW: Add interpretation
                    'theme': simple_interp['theme']
                },
                'is_current': is_current,
                'is_master_number': simple_interp['is_master_number'],  # NEW
                'years_remaining': years_remaining if is_current else None  # NEW
            }

            pinnacle_list.append(pinnacle_data)

            if is_current:
                current_pinnacle = pinnacle_data.copy()
                all_numbers['current_pinnacle'] = pinnacle['number']

        challenge_list = []
        for stage, (key, challenge) in enumerate(challenges.items(), 1):
            age_range = challenge['age_range']
            # Parse age range (formats: "0 - 33" or "52+")
            if '+' in age_range:
                start_age = int(age_range.replace('+', '').strip())
                end_age = None
            else:
                parts = age_range.split('-')
                start_age = int(parts[0].strip())
                end_age = int(parts[1].strip())

            is_current = (age >= start_age and (end_age is None or age <= end_age))

            # Calculate years remaining
            years_remaining = None
            if is_current and end_age is not None:
                years_remaining = end_age - age

            # Get simple interpretation
            simple_interp = get_simple_interpretation(challenge['number'], 'challenge')

            challenge_data = {
                'stage': str(stage),
                'number': challenge['number'],
                'age_range': age_range,
                'start_age': start_age,
                'end_age': end_age,
                'interpretation': {  # NEW: Add interpretation
                    'theme': simple_interp['theme']
                },
                'is_current': is_current,
                'is_master_number': simple_interp['is_master_number'],  # NEW
                'years_remaining': years_remaining if is_current else None  # NEW
            }

            challenge_list.append(challenge_data)

            if is_current:
                current_challenge = challenge_data.copy()
                all_numbers['current_challenge'] = challenge['number']

        report['life_cycles'] = {
            'current_age': age,
            'pinnacles': {
                'name': get_vietnamese_name('pinnacles'),
                'importance': get_importance('pinnacles'),
                'meaning': get_meaning('pinnacles'),
                'all_pinnacles': pinnacle_list,  # Renamed from 'data' for clarity
                'current_pinnacle': current_pinnacle,
                'ai_context': f"Hiện tại đang ở giai đoạn Pinnacle {current_pinnacle['stage']} (số {current_pinnacle['number']})." if current_pinnacle else "Chưa xác định được giai đoạn hiện tại."
            },
            'challenges': {
                'name': get_vietnamese_name('challenges'),
                'importance': get_importance('challenges'),
                'meaning': get_meaning('challenges'),
                'all_challenges': challenge_list,  # Renamed from 'data' for clarity
                'current_challenge': current_challenge,
                'ai_context': f"Hiện tại đang đối mặt với Challenge {current_challenge['stage']} (số {current_challenge['number']})." if current_challenge else "Chưa xác định được thử thách hiện tại."
            }
        }

        # PHASE 2: MASTER NUMBERS ANALYSIS
        master_numbers_found = {}
        for location, number in all_numbers.items():
            if is_master_number(number):
                if number not in master_numbers_found:
                    master_numbers_found[number] = []
                master_numbers_found[number].append(location)

        master_numbers_analysis = {
            'has_master_numbers': len(master_numbers_found) > 0,
            'count': sum(len(locations) for locations in master_numbers_found.values()),
            'master_numbers_found': []  # Renamed from 'details' for clarity
        }

        master_number_names = {
            11: 'Số Chủ 11 - The Illuminator',
            22: 'Số Chủ 22 - The Master Builder',
            33: 'Số Chủ 33 - The Master Teacher'
        }

        for number, locations in master_numbers_found.items():
            master_numbers_analysis['master_numbers_found'].append({
                'number': number,
                'name': master_number_names.get(number, f'Số Chủ {number}'),
                'locations': locations,
                'count': len(locations),
                'significance': f"Số {number} xuất hiện ở {len(locations)} vị trí, cho thấy tiềm năng tâm linh và sứ mệnh cao"
            })

        # Add AI insight for master numbers
        if master_numbers_analysis['has_master_numbers']:
            insights = []
            for detail in master_numbers_analysis['master_numbers_found']:
                num = detail['number']
                locs = detail['locations']
                if 'life_path' in locs:
                    insights.append(f"Life Path {num}: Sứ mệnh cuộc đời đặc biệt cao")
                if 'soul_urge' in locs:
                    insights.append(f"Soul Urge {num}: Khao khát tâm linh mãnh liệt")
                if 'current_pinnacle' in locs:
                    insights.append(f"Pinnacle hiện tại là {num}: Giai đoạn quan trọng đặc biệt")

            master_numbers_analysis['ai_insight'] = "; ".join(insights) if insights else "Master Numbers cho thấy tiềm năng cao đặc biệt"

        report['master_numbers_analysis'] = master_numbers_analysis

        # PHASE 3: NUMBER INTERACTIONS (Conflicts & Harmonies)
        conflicts = []
        harmonies = []

        lp = all_numbers.get('life_path', 0)
        su = all_numbers.get('soul_urge', 0)
        exp = all_numbers.get('expression', 0)
        pers = all_numbers.get('personality', 0)

        # Detect conflicts
        # LP vs SU conflict patterns
        lp_material = lp in [4, 8]  # Material-focused
        su_spiritual = su in [7, 9, 11, 33]  # Spiritual-focused

        if lp_material and su_spiritual:
            conflicts.append({
                'type': 'life_path_vs_soul_urge',
                'numbers': [lp, su],
                'description': f'Life Path {lp} hướng về thành công vật chất, nhưng Soul Urge {su} khao khát tâm linh',
                'resolution': f'Sử dụng thành công vật chất (LP {lp}) để phục vụ sứ mệnh tâm linh cao hơn (SU {su})',
                'ai_advice': 'Khuyên người này cân bằng giữa mục tiêu vật chất và phát triển tâm linh'
            })

        # SU vs Personality conflict
        su_introverted = su in [2, 4, 7]
        pers_extroverted = pers in [1, 3, 5]

        if su_introverted and pers_extroverted:
            conflicts.append({
                'type': 'inner_vs_outer',
                'numbers': [su, pers],
                'description': f'Soul Urge {su} khao khát sự tĩnh lặng, nhưng Personality {pers} tỏa ra năng lượng hướng ngoại',
                'resolution': 'Tìm thời gian cho bản thân dù hình ảnh bên ngoài rất năng động',
                'ai_advice': 'Người này cần cân bằng giữa nhu cầu nội tâm và hình ảnh bên ngoài'
            })

        # Detect harmonies
        # Expression supports Life Path
        if (lp in [1, 8] and exp in [1, 3, 5]) or (lp in [2, 6, 9] and exp in [2, 6, 9]):
            harmonies.append({
                'type': 'expression_supports_life_path',
                'numbers': [exp, lp],
                'description': f'Expression {exp} hỗ trợ Life Path {lp} rất tốt',
                'benefit': 'Tài năng tự nhiên phù hợp với mục đích cuộc đời, dễ thành công'
            })

        # Soul Urge matches Life Path
        if abs(lp - su) <= 1 or (is_master_number(lp) and is_master_number(su)):
            harmonies.append({
                'type': 'aligned_purpose',
                'numbers': [lp, su],
                'description': f'Life Path {lp} và Soul Urge {su} hài hòa',
                'benefit': 'Mục đích cuộc đời phù hợp với mong muốn nội tâm, ít xung đột nội tại'
            })

        report['number_interactions'] = {
            'conflicts': conflicts,
            'harmonies': harmonies,
            'balance_score': len(harmonies) - len(conflicts),  # Positive = more harmonies
            'ai_insight': f"Tổng thể {'hài hòa' if len(harmonies) >= len(conflicts) else 'cần cân bằng'}: {len(harmonies)} điểm hài hòa, {len(conflicts)} mâu thuẫn cần giải quyết"
        }

        # Build summary section with actionable insights
        lp_interp = report['core_numbers']['life_path']['interpretation']
        exp_interp = report['core_numbers']['expression']['interpretation']
        su_interp = report['core_numbers']['soul_urge']['interpretation']

        # PHASE 3: ACTIONABLE INSIGHTS
        current_focus = []
        warning_signs = []

        # Current Pinnacle insights
        if current_pinnacle:
            pinn_num = current_pinnacle['number']
            years_left = current_pinnacle.get('years_remaining')
            if years_left is not None:
                urgency = "HIGH" if years_left <= 3 else ("MEDIUM" if years_left <= 6 else "LOW")
                current_focus.append(f"Tận dụng Pinnacle {current_pinnacle['stage']} (số {pinn_num}) - còn {years_left} năm")
                if urgency == "HIGH":
                    warning_signs.append(f"Đang ở tuổi {age} - chỉ còn {years_left} năm trong Pinnacle {pinn_num} quan trọng")

        # Current Challenge insights
        if current_challenge:
            chal_num = current_challenge['number']
            current_focus.append(f"Vượt qua Challenge {current_challenge['stage']} (số {chal_num})")

        # Karmic lessons insights
        if karmic_lessons:
            if len(karmic_lessons) >= 3:
                warning_signs.append(f"Có {len(karmic_lessons)} bài học nghiệp cần học - đòi hỏi nhiều nỗ lực")
            current_focus.append(f"Học các bài học số {', '.join(map(str, karmic_lessons))}")

        # Conflicts insights
        for conflict in conflicts:
            warning_signs.append(conflict['description'])

        # Upcoming pinnacle
        upcoming_pinnacle = None
        for p in pinnacle_list:
            if not p['is_current'] and p['start_age'] > age:
                upcoming_pinnacle = p
                break

        long_term_vision = ""
        if upcoming_pinnacle:
            years_until = upcoming_pinnacle['start_age'] - age
            long_term_vision = f"Sau tuổi {upcoming_pinnacle['start_age']}, vào Pinnacle {upcoming_pinnacle['stage']} (số {upcoming_pinnacle['number']}) - {upcoming_pinnacle['interpretation']['theme']}. Chuẩn bị từ bây giờ."

        # Determine personality archetype
        archetypes = {
            (8, 11): ("The Spiritual CEO", "Thành công vật chất với sứ mệnh tâm linh"),
            (11, 22): ("The Visionary Leader", "Lãnh đạo với tầm nhìn tâm linh cao"),
            (6, 9): ("The Compassionate Healer", "Chăm sóc và phục vụ nhân loại"),
            (1, 8): ("The Ambitious Pioneer", "Tiên phong và đạt thành công cao"),
            (3, 5): ("The Creative Adventurer", "Sáng tạo và tự do khám phá"),
            (2, 6): ("The Harmonious Peacemaker", "Hòa giải và tạo sự cân bằng")
        }

        archetype = ("The Numerology Profile", "Hành trình phát triển độc đáo")
        for key, value in archetypes.items():
            if (lp, su) == key or (su, lp) == key:
                archetype = value
                break

        report['summary'] = {
            'overview': f"{standard_data['personal_info']['original_name']} có Life Path Number là {report['core_numbers']['life_path']['number']} ({lp_interp.get('title', '')}), Expression Number là {report['core_numbers']['expression']['number']} ({exp_interp.get('title', '')}), và Soul Urge Number là {report['core_numbers']['soul_urge']['number']} ({su_interp.get('title', '')}).",
            'key_characteristics': {
                'life_purpose': lp_interp.get('description', ''),
                'natural_talents': exp_interp.get('talents', []) if 'talents' in exp_interp else exp_interp.get('strengths', []),
                'inner_desires': su_interp.get('desires', []) if 'desires' in su_interp else su_interp.get('keywords', []),
                'strengths': lp_interp.get('strengths', []),
                'challenges': lp_interp.get('challenges', [])
            },
            'ai_interpretation_guide': {
                'instruction': 'Khi phân tích báo cáo này, hãy chú ý đến:',
                'priorities': [
                    '1. Life Path Number - Mục đích cuộc đời và con đường chính',
                    '2. Expression Number - Tài năng và cách thể hiện bản thân',
                    '3. Soul Urge Number - Động lực nội tâm và mong muốn sâu xa',
                    '4. Pinnacle hiện tại - Giai đoạn và cơ hội hiện tại',
                    '5. Challenge hiện tại - Thử thách cần vượt qua ngay bây giờ',
                    '6. Karmic Lessons - Bài học cần học trong đời',
                    '7. Master Numbers - Tiềm năng tâm linh cao đặc biệt',
                    '8. Number Interactions - Mâu thuẫn và hài hòa giữa các số'
                ],
                'interpretation_approach': 'Hãy kết hợp tất cả các chỉ số để tạo ra một bức tranh toàn diện về con người này. Chú ý đến sự tương tác giữa các chỉ số, đặc biệt là khi có mâu thuẫn giữa mong muốn nội tâm (Soul Urge) và hình ảnh bên ngoài (Personality).'
            },
            # NEW: Actionable Insights
            'actionable_insights': {
                'current_focus': current_focus if current_focus else ['Tiếp tục phát triển theo con đường của mình'],
                'warning_signs': warning_signs if warning_signs else ['Không có cảnh báo đặc biệt'],
                'long_term_vision': long_term_vision if long_term_vision else 'Tiếp tục hành trình phát triển cá nhân'
            },
            # NEW: Personality Profile
            'personality_profile': {
                'archetype': archetype[0],
                'tagline': archetype[1],
                'ideal_path': f"Phát huy {lp_interp.get('title', 'điểm mạnh')} kết hợp với {su_interp.get('title', 'khao khát nội tâm')}"
            }
        }

        return report
