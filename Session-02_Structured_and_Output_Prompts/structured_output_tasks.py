"""
Session 02: Structured & Output Prompts
Demonstration script showing JSON schema validation and word count constraint verification.
"""

import json



def validate_json_output(json_str: str):
    print("Testing Task 3 JSON output validity:")
    try:
        data = json.loads(json_str)
        print(" [SUCCESS] Output is valid JSON!")
        print(f" Total records found: {len(data.get('winners', []))}")
        for item in data.get('winners', []):
            print(f"  - {item['edition_year']}: {item['champion_team']} (Captain: {item['winning_captain']})")
        return True
    except json.JSONDecodeError as e:
        print(f" [FAILED] Invalid JSON: {e}")
        return False

def check_word_count(text: str, max_words: int = 30):
    words = text.strip().split()
    count = len(words)
    print(f"\nTesting Task 4 Word Count Constraint (Max: {max_words}):")
    print(f" Text: \"{text}\"")
    print(f" Word Count: {count}")
    if count <= max_words:
        print(f" [SUCCESS] Word count {count} is within limit <= {max_words}")
    else:
        print(f" [WARNING] Word count {count} exceeds limit > {max_words}")
    return count

if __name__ == "__main__":
    sample_json = '''{
  "league": "Indian Premier League",
  "total_records": 5,
  "winners": [
    {"edition_year": 2024, "champion_team": "Kolkata Knight Riders", "winning_captain": "Shreyas Iyer"},
    {"edition_year": 2023, "champion_team": "Chennai Super Kings", "winning_captain": "MS Dhoni"},
    {"edition_year": 2022, "champion_team": "Gujarat Titans", "winning_captain": "Hardik Pandya"},
    {"edition_year": 2021, "champion_team": "Chennai Super Kings", "winning_captain": "MS Dhoni"},
    {"edition_year": 2020, "champion_team": "Mumbai Indians", "winning_captain": "Rohit Sharma"}
  ]
}'''
    validate_json_output(sample_json)

    sample_summary = "- Instant 24/7 Transfers: Direct bank settlement via QR scan. - Unified Convenience: Single app for all bills and merchants. - Secure PIN Access: Safe two-factor MPIN authentication."
    check_word_count(sample_summary, 30)
