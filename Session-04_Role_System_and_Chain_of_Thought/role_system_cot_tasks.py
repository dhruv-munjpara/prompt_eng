"""
Session 04: Role, System & Chain-of-Thought
Demonstration script showing chain-of-thought calculation and system prompt boundary evaluation.
"""

def solve_wallet_problem(wallet_balance: float, items: list) -> dict:
    total_cost = sum(items)
    difference = wallet_balance - total_cost
    has_sufficient_balance = difference >= 0
    return {
        "wallet_balance": wallet_balance,
        "items": items,
        "total_cost": total_cost,
        "difference": difference,
        "has_sufficient_balance": has_sufficient_balance
    }

def evaluate_system_guardrail(query: str, system_domain: str, response: str) -> bool:
    print(f"\n[Guardrail Test] Query: '{query}'")
    is_ipl_related = "ipl" in query.lower() or "cricket" in query.lower()
    if not is_ipl_related:
        refusal_keywords = ["cannot assist", "exclusively to the indian premier league", "refuse", "outside the ipl"]
        adheres = any(keyword in response.lower() for keyword in refusal_keywords)
        print(f" -> Query is Out-of-Domain. Refusal Triggered: {adheres}")
        return adheres
    return True

if __name__ == "__main__":
    print("=== Task 3: Chain-of-Thought Programmatic Proof ===")
    result = solve_wallet_problem(2000.0, [499.0, 799.0, 899.0])
    print(f"Wallet Balance: Rs. {result['wallet_balance']}")
    print(f"Item Prices   : {result['items']}")
    print(f"Total Cost    : Rs. {result['total_cost']}")
    print(f"Balance Diff  : Rs. {result['difference']}")
    print(f"Sufficient?   : {result['has_sufficient_balance']}")

    print("\n=== Task 2: System Guardrail Test ===")
    sample_response = (
        "I am CricStat AI, an assistant dedicated exclusively to the Indian Premier League (IPL). "
        "I cannot assist with entertainment, Bollywood, or other topics outside the IPL tournament."
    )
    evaluate_system_guardrail("Tell me about the latest Bollywood movie", "IPL Cricket", sample_response)

    print("\n=== Task 5: Word Count Constraint Verification ===")
    insta_caption = "Crispy butter chicken samosa chaat on SBR is pure heaven! Amdavad foodies, run, don't walk!"
    words = insta_caption.split()
    print(f"Caption: '{insta_caption}'")
    print(f"Word count: {len(words)} (Limit: < 20 words) -> {'PASSED' if len(words) < 20 else 'FAILED'}")
