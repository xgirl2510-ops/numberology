#!/usr/bin/env python3
"""
Test script to verify library installation
"""

print("=" * 60)
print("TESTING NUMEROLOGY LIBRARY INSTALLATION")
print("=" * 60)

# Test 1: Import package
print("\n1. Testing import...")
try:
    from numerology import Numerology
    print("   ✅ Import successful!")
except ImportError as e:
    print(f"   ❌ Import failed: {e}")
    exit(1)

# Test 2: Check version
print("\n2. Checking version...")
try:
    import numerology
    print(f"   ✅ Version: {numerology.__version__}")
except Exception as e:
    print(f"   ⚠️  Version check failed: {e}")

# Test 3: Create instance
print("\n3. Creating Numerology instance...")
try:
    calc = Numerology("Test Name", "15/07/1990", language='en')
    print("   ✅ Instance created!")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    exit(1)

# Test 4: Calculate Life Path
print("\n4. Testing Life Path calculation...")
try:
    life_path = calc.life_path_number()
    print(f"   ✅ Life Path: {life_path}")
    assert isinstance(life_path, int)
    assert 1 <= life_path <= 9 or life_path in [11, 22, 33]
except Exception as e:
    print(f"   ❌ Failed: {e}")
    exit(1)

# Test 5: Calculate Expression
print("\n5. Testing Expression calculation...")
try:
    expression = calc.expression_number()
    print(f"   ✅ Expression: {expression}")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    exit(1)

# Test 6: Vietnamese name with Y
print("\n6. Testing Vietnamese name with Y processing...")
try:
    calc_vi = Numerology("Nguyễn Thị Uyên Yên", "15/07/1990", language='vi')

    expression_vi = calc_vi.expression_number()
    soul_urge_vi = calc_vi.soul_urge_number()
    personality_vi = calc_vi.personality_number()

    print(f"   ✅ Expression: {expression_vi} (expected: 7)")
    print(f"   ✅ Soul Urge: {soul_urge_vi} (expected: 3)")
    print(f"   ✅ Personality: {personality_vi} (expected: 22)")

    # Verify expected values
    assert expression_vi == 7, f"Expression should be 7, got {expression_vi}"
    assert soul_urge_vi == 3, f"Soul Urge should be 3, got {soul_urge_vi}"
    assert personality_vi == 22, f"Personality should be 22, got {personality_vi}"

except Exception as e:
    print(f"   ❌ Failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 7: Master Number
print("\n7. Testing Master Number preservation...")
try:
    calc_master = Numerology("Test", "08/06/1988", language='en')
    life_path_master = calc_master.life_path_number()
    print(f"   ✅ Life Path: {life_path_master} (expected: 22)")
    assert life_path_master == 22, f"Should be 22, got {life_path_master}"
except Exception as e:
    print(f"   ❌ Failed: {e}")
    exit(1)

# Test 8: Get all numbers
print("\n8. Testing get_all_numbers()...")
try:
    data = calc.get_all_numbers()
    print(f"   ✅ Core numbers: {list(data['core_numbers'].keys())}")
    print(f"   ✅ Secondary numbers: {list(data['secondary_numbers'].keys())}")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    exit(1)

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
print("\nLibrary is ready to use!")
print("\nExample usage:")
print("  from numerology import Numerology")
print("  calc = Numerology('Your Name', 'DD/MM/YYYY', language='vi')")
print("  print(calc.life_path_number())")
