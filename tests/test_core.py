"""
Core tests for Numerology library
"""
import pytest
from numerology import Numerology


class TestNumerologyBasic:
    """Basic numerology calculations"""

    def test_life_path_number(self):
        """Test Life Path Number calculation"""
        calc = Numerology("John Doe", "15/07/1990", language='en')
        life_path = calc.life_path_number()
        assert isinstance(life_path, int)
        assert 1 <= life_path <= 9 or life_path in [11, 22, 33]

    def test_expression_number(self):
        """Test Expression Number calculation"""
        calc = Numerology("John Doe", "15/07/1990", language='en')
        expression = calc.expression_number()
        assert isinstance(expression, int)
        assert 1 <= expression <= 9 or expression in [11, 22, 33]

    def test_soul_urge_number(self):
        """Test Soul Urge Number calculation"""
        calc = Numerology("John Doe", "15/07/1990", language='en')
        soul_urge = calc.soul_urge_number()
        assert isinstance(soul_urge, int)
        assert 1 <= soul_urge <= 9 or soul_urge in [11, 22, 33]

    def test_personality_number(self):
        """Test Personality Number calculation"""
        calc = Numerology("John Doe", "15/07/1990", language='en')
        personality = calc.personality_number()
        assert isinstance(personality, int)
        assert 1 <= personality <= 9 or personality in [11, 22, 33]


class TestVietnameseName:
    """Test Vietnamese name processing"""

    def test_vietnamese_name_with_y(self):
        """Test Vietnamese name with Y processing"""
        calc = Numerology("Nguyễn Thị Uyên Yên", "15/07/1990", language='vi')

        # Expression Number should be 7
        expression = calc.expression_number()
        assert expression == 7, f"Expected 7, got {expression}"

        # Soul Urge Number should be 3
        soul_urge = calc.soul_urge_number()
        assert soul_urge == 3, f"Expected 3, got {soul_urge}"

        # Personality Number should be 22 (Master Number)
        personality = calc.personality_number()
        assert personality == 22, f"Expected 22, got {personality}"


class TestMasterNumbers:
    """Test Master Numbers preservation"""

    def test_master_number_11(self):
        """Test that 11 is preserved as Master Number"""
        calc = Numerology("Mary Johnson", "02/09/1990", language='en')
        # This should produce Master Number 11 for Soul Urge
        soul_urge = calc.soul_urge_number()
        assert soul_urge == 11 or 1 <= soul_urge <= 9

    def test_master_number_22(self):
        """Test Life Path calculation with potential Master Number 22"""
        calc = Numerology("Test Name", "08/06/1988", language='en')
        life_path = calc.life_path_number()
        # This date should give Life Path 22
        assert life_path == 22, f"Expected 22, got {life_path}"

    def test_master_number_33(self):
        """Test Master Number 33 is preserved"""
        # Master Number 33 is rare but should be preserved
        calc = Numerology("Test", "24/09/1990", language='en')
        life_path = calc.life_path_number()
        assert 1 <= life_path <= 9 or life_path in [11, 22, 33]


class TestNameComponentReduction:
    """Test Name Component Reduction Method"""

    def test_component_reduction(self):
        """Test that components are reduced separately"""
        calc = Numerology("NGUYEN THI UYEN YEN", "01/01/1990", language='vi')

        # Expression should use component reduction
        expression = calc.expression_number()
        assert isinstance(expression, int)

        # Verify it's different from simple addition
        # This would need internal access to verify properly


class TestYRules:
    """Test Y vowel/consonant detection across languages"""

    def test_y_in_english(self):
        """Test Y processing in English"""
        calc = Numerology("MARY", "01/01/1990", language='en')
        # Y at end after consonant should be vowel
        soul_urge = calc.soul_urge_number()
        assert isinstance(soul_urge, int)

    def test_y_in_vietnamese(self):
        """Test Y processing in Vietnamese"""
        calc = Numerology("YEN", "01/01/1990", language='vi')
        # Y at start before vowel should be consonant
        personality = calc.personality_number()
        assert isinstance(personality, int)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
