# Session 05: Hallucination Handling & Real Projects — Assignment Solutions

**Course:** Prompt Engineering  
**Student:** Dhruv Munjpara  
**Topic:** Hallucination Identification, Strict Context Grounding, Self-Audit Verification, Grounded Refactoring, and Fact Attribution  

---

## 📌 Task 1: Hallucination Detection — Trending Dishes on Zomato in Ahmedabad

### Objective
Ask an AI chatbot to list the top 5 trending dishes on Zomato in Ahmedabad. Check if the AI gives real, verifiable live answers or hallucinates, and document the hallucinations spotted.

### Prompt Used
```text
List the top 5 trending dishes currently on Zomato in Ahmedabad today.
```

### AI Response Received
> 1. **Gwalior Butter Dosa** at *Manek Chowk*
> 2. **Jini Dosa with Extra Mozzarella** at *Balaji Sandwiches & Fast Food*
> 3. **Mexican Cheese Hot Dog** at *Karnavati Dabeli, Vastrapur*
> 4. **Signature Truffle Cold Brew & Avocado Toast** at *Zen Cafe, Amdavad ni Gufa*
> 5. **Royal Awadhi Mutton Biryani** at *Bawarchi Biryani, CG Road*

### Critical Verification & Hallucination Analysis
* **Nature of the Query:** Demands real-time, dynamic algorithmic platform data ("trending on Zomato today").
* **Verification Check:**
  - LLMs do not possess live socket or API access to Zomato's real-time ranking algorithm unless explicitly connected to real-time search / browsing tools.
  - The model synthesized well-known tourist food tropes and general popular items from training data rather than actual telemetry data from Zomato.
* **Specific Hallucinations Spotted:**
  1. *Fabricated Menu Item:* Zen Cafe at Amdavad ni Gufa is known for filter coffee, cookies, and pizza; it does not serve "Truffle Cold Brew".
  2. *Fabricated Trending Metric:* Presenting these specific 5 items as "Zomato's official trending top 5 today" is a synthetic hallucination. The model presents static historical associations with false authoritative certainty.
* **Takeaway:** When querying real-time or rapidly changing platform states, standard LLMs will hallucinate plausible-sounding generalizations instead of acknowledging lack of live data unless prompted with strict epistemic humility directives.

---

## 📌 Task 2: Strict Context Grounding — IPL 2023 Final Match

### Objective
Write a prompt that asks an AI to summarize the IPL 2023 final match, instructing it to ONLY use the supplied text:
*"Chennai Super Kings won the IPL 2023 final against Gujarat Titans by 5 wickets."*  
Check if it sticks to the given data or adds outside details.

### Context-Grounded Prompt
```text
You are a strict, closed-domain summarization engine.
Summarize the match based SOLELY on the provided context below.

CONTEXT:
"Chennai Super Kings won the IPL 2023 final against Gujarat Titans by 5 wickets."

STRICT RULES:
1. Use ONLY the facts directly stated in the context above.
2. Do NOT add ANY external knowledge, player names (e.g., Dhoni, Jadeja, Hardik Pandya), venue names, match dates, overs, or margin of victory details not written in the context.
3. If information is not explicitly mentioned, it does not exist.
4. Keep the summary to 1–2 sentences.
```

### Full AI Response
> *"In the IPL 2023 final, Chennai Super Kings defeated Gujarat Titans to claim victory by a margin of 5 wickets."*

### Boundary & Grounding Check
- **External Player Names Added?** None (MS Dhoni, Ravindra Jadeja, and Shubman Gill were completely withheld).
- **Match Circumstances Added?** None (No mention of rain delays, DLS method, Narendra Modi Stadium, or final ball boundaries).
- **Factual Integrity:** 100% faithful to the 1-sentence source context.

---

## 📌 Task 3: Self-Audit & Assumption Verification — Flipkart Earbud Description

### Objective
Prompt the AI to generate a product description for a new wireless earbud for Flipkart, paired with a mandatory follow-up verification audit asking it to list any details it invented.

### Part 1: Product Generation Prompt
```text
Write a high-converting Flipkart product description for a newly launched wireless TWS earbud called 'AcousticPulse Pods Pro'.
```

#### AI Generated Product Description:
> **AcousticPulse Pods Pro (Midnight Black)**  
> Experience studio-grade acoustic depth with the all-new AcousticPulse Pods Pro. Engineered with **13mm Titanium-coated dynamic drivers**, these earbuds deliver heart-thumping bass and crisp highs. Featuring **Active Noise Cancellation up to 32dB**, you can drown out street noise effortlessly. Enjoy marathon sessions with **45 hours of total playback time** and **InstaCharge technology (10 mins charge = 5 hours playtime)**. Equipped with **Quad-Mic AI ENC** for crystal-clear calls, ultra-low 40ms latency gaming mode, and **IPX5 sweat resistance**, they are the ultimate companion for work, workout, and play.

---

### Part 2: Follow-up Verification Audit Prompt
```text
AUDIT QUERY:
Is all the information in your previous answer based on real data or did you make any assumptions? List any details you invented or fabricated.
```

#### AI Self-Audit Response:
> **Self-Audit & Fact Disclosure:**  
> **All technical specifications and product features in the previous response were fabricated assumptions (synthetic generation).**  
> Because 'AcousticPulse Pods Pro' was provided without a product spec sheet, I invented the following details:
> 1. **Hardware Specs:** 13mm Titanium-coated dynamic drivers (Invented).
> 2. **Noise Cancellation Metric:** Active Noise Cancellation up to 32dB (Invented).
> 3. **Battery Performance:** 45 hours total playtime and "10 mins = 5 hours" fast charge (Invented).
> 4. **Mic & Latency:** Quad-Mic AI Environmental Noise Cancellation and 40ms low-latency gaming mode (Invented).
> 5. **Durability Rating:** IPX5 sweat and water resistance (Invented).
> 6. **Color Variant:** "Midnight Black" (Invented).
>
> **Production Recommendation:** Before publishing this listing to Flipkart, replace all fabricated placeholder specs with the official OEM specification sheet.

---

## 📌 Task 4: Anti-Hallucination Prompt Refactoring — iPhone Review

### Original Flawed Prompt
> *"Write a review of the latest iPhone."*

### Why the Original Prompt Causes Hallucinations:
- **No Model Anchor:** "Latest" is subjective and dependent on model cutoff dates; the model may confuse iPhone 15 Pro, iPhone 16 Pro, or speculate on unreleased models.
- **No Grounding Source:** Allows the model to pull unverified rumors, blogs, or speculative tech forum claims.
- **Unbounded Scope:** Without defined criteria (camera, battery, chip), it invents benchmark figures and battery life hours.

---

### Refactored Anti-Hallucination Prompt
```text
Provide a factual technical review of the iPhone 16 Pro based STRICTLY on official hardware specifications published by Apple Inc. (apple.com/iphone-16-pro/specs).

Strict Instructions:
1. Report ONLY confirmed hardware specifications: Chipset (A18 Pro), Display (6.3-inch Super Retina XDR with ProMotion), Camera hardware (48MP Fusion, 48MP Ultra Wide, 5x Telephoto), and new physical buttons (Camera Control, Action Button).
2. For battery life and performance, quote ONLY Apple's official claims (e.g., "up to 27 hours video playback"). Do NOT invent third-party benchmark scores (e.g., Geekbench or AnTuTu) or anecdotal battery test hours.
3. If an exact technical specification is unknown or unverified by Apple's public spec sheet, explicitly output "Not specified in official documentation" rather than estimating.
```

### One-Line Justification:
> *This refactored prompt eliminates hallucinations by anchoring the target entity to a specific model (iPhone 16 Pro), restricting claims to an official verifiable primary source (Apple spec sheet), and explicitly barring synthetic third-party benchmarks.*

---

## 📌 Task 5: BookMyShow Movie Summary with Mandatory Source Attribution

### Objective
Design a prompt for a BookMyShow movie summary generator that forces the AI to cite the source URL or state *"source not found"* after every single factual claim.

### Source-Attributed Prompt
```text
You are an editorial movie researcher for BookMyShow.
Task: Write a comprehensive factual summary of the blockbuster film 'Kalki 2898 AD'.

MANDATORY FACT-CHECKING & ATTRIBUTION CONSTRAINTS:
1. Every factual statement regarding director, cast, box office collections, production budget, runtime, and plot premise MUST be immediately followed by a citation in brackets: `[Source: URL or Publication]`
2. If you are citing a fact from general knowledge that does not have a verified, direct source URL in your context, you MUST append `[Source: source not found]`.
3. Do NOT make any unverified claims without attribution.
```

### Full AI Response

> ### Editorial Overview: *Kalki 2898 AD*
>
> - **Director & Writer:** Directed by Nag Ashwin and produced by C. Aswani Dutt under Vyjayanthi Movies `[Source: https://www.imdb.com/title/tt12735488/]`.
> - **Star Cast:** Features an ensemble cast including Prabhas as Bhairava, Amitabh Bachchan as Ashwatthama, Kamal Haasan as Supreme Yaskin, and Deepika Padukone as SUM-80 `[Source: https://en.wikipedia.org/wiki/Kalki_2898_AD]`.
> - **Genre & Premise:** A post-apocalyptic dystopian science-fiction film set in the year 2898 AD in a desolate Kasi, inspired by Hindu mythological events of the Mahabharata and the prophecy of Kalki, the tenth avatar of Vishnu `[Source: https://www.imdb.com/title/tt12735488/]`.
> - **Production Scale & Budget:** Produced on an estimated budget of ₹600 crore, making it one of the most expensive Indian films ever produced `[Source: https://indianexpress.com/entertainment/telugu/kalki-2898-ad-budget-box-office]`.
> - **Theatrical Runtime:** The film has an official theatrical running time of 180 minutes (3 hours) with a U/A certification by the CBFC `[Source: https://in.bookmyshow.com]`.
> - **Box Office Performance:** Grossed over ₹1,000 crore worldwide across all language dubs during its theatrical run `[Source: https://www.hindustantimes.com/entertainment/telugu-cinema/kalki-2898-ad-box-office-1000-crore]`.
> - **Future Installment:** The story ends on a cliffhanger setting up Kalki Cinematic Universe Part 2, whose production timeline remains unconfirmed `[Source: source not found]`.

### Attribution Audit
- Every line has an explicit source citation.
- When describing future unconfirmed sequel production dates, the model adhered to the fallback rule: `[Source: source not found]`.
- This ensures 100% traceability for downstream publishing workflows.

---
*End of Session 05 Assignment.*
