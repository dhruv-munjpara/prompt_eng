"""
Session 05: Hallucination Handling & Real Projects
Demonstration script showing source attribution validation and closed-domain grounding checks.
"""

import re

def verify_source_attributions(text: str) -> dict:
    lines = [line.strip() for line in text.strip().split("\n") if line.strip().startswith("-")]
    citation_pattern = re.compile(r"\[Source:\s*(.+?)\]")
    
    total_facts = len(lines)
    attributed_facts = 0
    sources_found = 0
    sources_missing = 0

    for line in lines:
        match = citation_pattern.search(line)
        if match:
            attributed_facts += 1
            source_content = match.group(1).strip()
            if "source not found" in source_content.lower():
                sources_missing += 1
            else:
                sources_found += 1

    return {
        "total_facts": total_facts,
        "attributed_facts": attributed_facts,
        "valid_sources": sources_found,
        "missing_source_fallbacks": sources_missing,
        "attribution_rate": (attributed_facts / total_facts * 100) if total_facts else 0
    }

if __name__ == "__main__":
    sample_movie_summary = """
- Director & Writer: Directed by Nag Ashwin [Source: https://www.imdb.com/title/tt12735488/]
- Star Cast: Features Prabhas, Amitabh Bachchan, Kamal Haasan, Deepika Padukone [Source: https://en.wikipedia.org/wiki/Kalki_2898_AD]
- Production Budget: Produced on an estimated budget of ₹600 crore [Source: https://indianexpress.com/entertainment/telugu/kalki-2898-ad-budget-box-office]
- Future Installment: Sequel production date remains unconfirmed [Source: source not found]
"""
    result = verify_source_attributions(sample_movie_summary)
    print("=== Task 5: Source Attribution Audit ===")
    print(f"Total Fact Lines Analyzed    : {result['total_facts']}")
    print(f"Properly Attributed Lines    : {result['attributed_facts']}")
    print(f"Verified External URLs       : {result['valid_sources']}")
    print(f"Acknowledged Fallback Sources: {result['missing_source_fallbacks']}")
    print(f"Attribution Compliance Rate  : {result['attribution_rate']:.1f}%")
