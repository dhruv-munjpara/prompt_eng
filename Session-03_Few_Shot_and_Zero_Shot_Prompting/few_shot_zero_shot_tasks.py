"""
Session 03: Few Shot & Zero Shot Prompting
Demonstration script showing exemplar formulation, templating, and prompt comparison logic.
"""

def format_few_shot_prompt(system_role: str, examples: list, target_input: str) -> str:
    prompt = f"System: {system_role}\n\n"
    for i, ex in enumerate(examples, 1):
        prompt += f"--- Example {i} ---\nInput: {ex['input']}\nOutput:\n{ex['output']}\n\n"
    prompt += f"--- Target Task ---\nInput: {target_input}\nOutput:\n"
    return prompt

if __name__ == "__main__":
    examples = [
        {
            "input": "Product: Realme Narzo 60 Pro 5G",
            "output": "Tagline: Speed Meets Ultra-Curved Elegance\nSpecs: 120Hz Curved AMOLED, 100MP OIS Camera, Dimensity 7050"
        },
        {
            "input": "Product: boAt Rockerz 551ANC",
            "output": "Tagline: Silence the Chaos, Unleash the Bass\nSpecs: 35dB Hybrid ANC, 100 Hrs Playtime, 40mm Drivers"
        },
        {
            "input": "Product: Puma Nitro Velocity 3",
            "output": "Tagline: Featherlight Cushioning for Everyday Miles\nSpecs: NITROFOAM Cushioning, PUMAGRIP Outsole, Engineered Mesh"
        }
    ]

    target = "Product: Noise ColorFit Ultra 3 Smartwatch"
    compiled_prompt = format_few_shot_prompt(
        "You are an expert e-commerce copywriter for Flipkart.",
        examples,
        target
    )

    print("=== Compiled Few-Shot Prompt ===")
    print(compiled_prompt)
    print("=== End Compiled Prompt ===")
