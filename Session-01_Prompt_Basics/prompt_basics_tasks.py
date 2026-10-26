"""
Session 01: Prompt Basics
Demonstration script showing prompt structures, execution simulation, and automated evaluation metrics.
"""

def evaluate_prompt(prompt_type: str, prompt_text: str, response: str, criteria: dict):
    print(f"\n{'='*70}")
    print(f"PROMPT TYPE: {prompt_type}")
    print(f"{'-'*70}")
    print(f"PROMPT:\n{prompt_text}")
    print(f"{'-'*70}")
    print(f"RESPONSE:\n{response}")
    print(f"{'-'*70}")
    print("EVALUATION SCORES:")
    for metric, score in criteria.items():
        print(f" - {metric:<25}: {score}/10")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    task1_unclear = "List trending songs in India."
    task1_unclear_resp = "1. Tauba Tauba\n2. Illuminati\n3. Aaj Ki Raat\n4. Big Dawgs\n5. Winning Speech"
    
    task1_clear = (
        "Provide a curated list of 5 trending Bollywood Hindi film songs released after 2022. "
        "For each song, include: Song Title, Movie, Release Year, Singers & Composer, and Genre."
    )
    task1_clear_resp = (
        "1. Tauba Tauba | Movie: Bad Newz (2024) | Karan Aujla | Dance Pop\n"
        "2. O Sajni Re | Movie: Laapataa Ladies (2024) | Arijit Singh, Ram Sampath | Romantic\n"
        "3. Aaj Ki Raat | Movie: Stree 2 (2024) | Madhubanti Bagchi, Sachin-Jigar | Folk Electronic\n"
        "4. Chaleya | Movie: Jawan (2023) | Arijit Singh, Anirudh Ravichander | Pop\n"
        "5. Tere Pyaar Mein | Movie: TJMM (2023) | Arijit Singh, Pritam | Romance"
    )

    evaluate_prompt("Task 1: Unclear Prompt", task1_unclear, task1_unclear_resp, {
        "Specificity": 3,
        "Constraint Adherence": 4,
        "Metadata Completeness": 2,
        "Usability": 3
    })

    evaluate_prompt("Task 1: Clear Prompt", task1_clear, task1_clear_resp, {
        "Specificity": 10,
        "Constraint Adherence": 10,
        "Metadata Completeness": 10,
        "Usability": 10
    })
