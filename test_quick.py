#!/usr/bin/env python3
"""Quick test for extended report"""

print("Testing extended report...")

try:
    from numerology import Numerology
    print("✅ Import successful")

    # Create instance
    calc = Numerology("Nguyen Van A", "15/08/1990", language='vi')
    print("✅ Instance created")

    # Test extended report
    print("\nCalling get_extended_report()...")
    report = calc.get_extended_report()
    print("✅ Extended report generated!")

    # Show basic structure
    print(f"\nTop-level keys: {list(report.keys())}")
    print(f"Metadata: {report['metadata']}")
    print(f"Age: {report['personal_information']['age']}")
    print(f"Life Path: {report['core_numbers']['life_path']['number']}")
    print(f"Current age: {report['life_cycles']['current_age']}")

    # Save to file
    import json
    with open('test_output.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("\n✅ Saved to test_output.json")
    print(f"✅ File size: {len(json.dumps(report))} bytes")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
