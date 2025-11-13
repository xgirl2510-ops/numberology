#!/usr/bin/env python3
"""
Demo: Get Extended Report (Format like example_full_report.json)
Tạo báo cáo đầy đủ với metadata, age, importance, ai_context cho AI luận giải
"""

from numerology import Numerology
import json

print("=" * 70)
print("DEMO: EXTENDED REPORT FOR AI INTERPRETATION")
print("=" * 70)

# INPUT
full_name = "Nguyen Van A"
birth_date = "15/08/1990"
language = 'vi'

print(f"\nINPUT:")
print(f"  Name: {full_name}")
print(f"  Birth Date: {birth_date}")
print(f"  Language: {language}")

# Create instance
print("\nCreating Numerology instance...")
calc = Numerology(full_name, birth_date, language=language)
print("  ✅ Instance created!")

# Get extended report
print("\nGenerating extended report...")
print("  Calling: calc.get_extended_report()")

extended_report = calc.get_extended_report()

print("  ✅ Extended report generated!")

# Show structure
print("\n" + "=" * 70)
print("EXTENDED REPORT STRUCTURE")
print("=" * 70)

print(f"\nTop-level keys:")
for key in extended_report.keys():
    print(f"  ✓ {key}")

print(f"\nMetadata:")
print(f"  - report_type: {extended_report['metadata']['report_type']}")
print(f"  - generated_at: {extended_report['metadata']['generated_at']}")
print(f"  - version: {extended_report['metadata']['version']}")
print(f"  - language: {extended_report['metadata']['language']}")

print(f"\nPersonal Information:")
print(f"  - original_name: {extended_report['personal_information']['original_name']}")
print(f"  - normalized_name: {extended_report['personal_information']['normalized_name']}")
print(f"  - birth_date: {extended_report['personal_information']['birth_date']}")
print(f"  - age: {extended_report['personal_information']['age']}")

print(f"\nCore Numbers:")
for key, data in extended_report['core_numbers'].items():
    print(f"  {key}:")
    print(f"    - number: {data['number']}")
    print(f"    - name: {data['name']}")
    print(f"    - importance: {data['importance']}")
    print(f"    - ai_context: {data['ai_context'][:50]}...")

# Show one example in detail
print("\n" + "=" * 70)
print("EXAMPLE: LIFE PATH NUMBER (CHI TIẾT)")
print("=" * 70)

lp = extended_report['core_numbers']['life_path']
print(f"\nNumber: {lp['number']}")
print(f"Name: {lp['name']}")
print(f"Importance: {lp['importance']}")
print(f"Meaning: {lp['meaning']}")
print(f"\nInterpretation:")
print(f"  Title: {lp['interpretation'].get('title', 'N/A')}")
print(f"  Keywords: {lp['interpretation'].get('keywords', [])}")
print(f"  Description: {lp['interpretation'].get('description', 'N/A')[:100]}...")
print(f"\nAI Context:")
print(f"  {lp['ai_context']}")

# Show current pinnacle/challenge
print("\n" + "=" * 70)
print("LIFE CYCLES (CURRENT)")
print("=" * 70)

current_age = extended_report['life_cycles']['current_age']
print(f"\nCurrent Age: {current_age}")

current_pinnacle = extended_report['life_cycles']['pinnacles']['current_pinnacle']
if current_pinnacle:
    print(f"\n✨ Current Pinnacle:")
    print(f"  Stage: {current_pinnacle['stage']}")
    print(f"  Number: {current_pinnacle['number']}")
    print(f"  Age Range: {current_pinnacle['age_range']}")

current_challenge = extended_report['life_cycles']['challenges']['current_challenge']
if current_challenge:
    print(f"\n⚠️  Current Challenge:")
    print(f"  Stage: {current_challenge['stage']}")
    print(f"  Number: {current_challenge['number']}")
    print(f"  Age Range: {current_challenge['age_range']}")

# Show summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

summary = extended_report['summary']
print(f"\nOverview:")
print(f"  {summary['overview']}")

print(f"\nKey Characteristics:")
print(f"  Life Purpose: {summary['key_characteristics']['life_purpose'][:100]}...")
print(f"  Natural Talents: {summary['key_characteristics']['natural_talents']}")
print(f"  Inner Desires: {summary['key_characteristics']['inner_desires']}")
print(f"  Strengths: {summary['key_characteristics']['strengths']}")
print(f"  Challenges: {summary['key_characteristics']['challenges']}")

print(f"\nAI Interpretation Guide:")
print(f"  Instruction: {summary['ai_interpretation_guide']['instruction']}")
print(f"  Priorities:")
for priority in summary['ai_interpretation_guide']['priorities']:
    print(f"    - {priority}")

# Save to JSON file
output_file = "extended_report_output.json"
print("\n" + "=" * 70)
print(f"SAVING TO {output_file}")
print("=" * 70)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(extended_report, f, indent=2, ensure_ascii=False)

print(f"✅ Extended report saved to: {output_file}")
print(f"✅ File size: {len(json.dumps(extended_report, ensure_ascii=False))} bytes")

# Compare with example_full_report.json structure
print("\n" + "=" * 70)
print("COMPARISON WITH example_full_report.json")
print("=" * 70)

expected_keys = ['metadata', 'personal_information', 'core_numbers', 'secondary_numbers', 'name_analysis', 'life_cycles', 'summary']
actual_keys = list(extended_report.keys())

print("\nExpected keys:")
for key in expected_keys:
    status = "✅" if key in actual_keys else "❌"
    print(f"  {status} {key}")

print("\nCore numbers fields:")
sample_core = extended_report['core_numbers']['life_path']
expected_fields = ['number', 'name', 'importance', 'meaning', 'interpretation', 'ai_context']
for field in expected_fields:
    status = "✅" if field in sample_core else "❌"
    print(f"  {status} {field}")

print("\n" + "=" * 70)
print("✅ DEMO COMPLETE!")
print("=" * 70)

print(f"""
Extended report has been generated with:
  ✅ metadata (timestamp, version, report_type, language)
  ✅ age (calculated from birth_date)
  ✅ name, importance, meaning for each number
  ✅ ai_context for AI interpretation
  ✅ current_pinnacle and current_challenge highlighted
  ✅ summary section with key characteristics
  ✅ ai_interpretation_guide for AI

This format is ready for AI consumption and interpretation!

Output file: {output_file}
""")
