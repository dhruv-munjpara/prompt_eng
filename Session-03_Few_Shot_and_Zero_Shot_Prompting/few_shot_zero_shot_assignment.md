# Session 03: Few Shot & Zero Shot Prompting — Assignment Solutions

**Course:** Prompt Engineering  
**Student:** Dhruv Munjpara  
**Topic:** Zero-Shot, One-Shot, and Few-Shot In-Context Learning and Pattern Conditioning  

---

## 📌 Task 1: Zero-Shot Prompting — IPL Match One-Line Summary

### Concept Definition
*Zero-Shot prompting* involves prompting an LLM to perform a task directly without providing any prior solved examples (exemplars) in the context window. The model relies entirely on its pre-trained weights and instruction-following capability.

### Exact Prompt Used
```text
Provide a punchy, one-line summary of the IPL 2024 Final match between Kolkata Knight Riders (KKR) and Sunrisers Hyderabad (SRH), highlighting the winner and key performance in under 25 words.
```

### Full AI Response Received
> *"Kolkata Knight Riders clinched their third IPL title with an emphatic eight-wicket demolition of Sunrisers Hyderabad, powered by Mitchell Starc’s lethal opening spell."*

---

## 📌 Task 2: One-Shot Prompting — Zomato Food Review (Dosa Restaurant in Ahmedabad)

### Concept Definition
*One-Shot prompting* supplies exactly one high-quality exemplar that demonstrates the expected output tone, structure, rating format, and pros/cons balance. The model mirrors this schema on the target entity.

### Exact One-Shot Prompt Used
```text
You are a food critic writing authentic restaurant reviews for Zomato. Emulate the structure, tone, and formatting of the example below to write a review for a new dosa restaurant in Ahmedabad.

---
### EXAMPLE REVIEW:
Restaurant: Milano Sourdough Pizza, Ahmedabad
Rating: 4.5/5 ⭐
Cuisine: Neapolitan Pizza & Italian Appetizers
The Vibe: Warm industrial lighting with an open wood-fired oven centerpiece.
Must-Try Dishes: Burrata Pesto Pizza, Truffle Fries, Tiramisu.
The Experience:
The sourdough crust achieves the holy grail of pizza: blistered leopard spotting, airy chewiness, and zero sogginess. The San Marzano tomato sauce has a bright acidity that cuts through the creaminess of the fresh burrata. Service was attentive despite a 25-minute wait on Saturday night.
Damage for Two: ₹1,100.
Pro-Tip: Book via Zomato District to skip the weekend sidewalk queue.
---

### YOUR TURN:
Generate a review following the exact same format for:
Restaurant: Dakshin Delight (Authentic South Indian Dosa specialty in Navrangpura, Ahmedabad)
Key highlights to incorporate: Davanagere Benne Dosa, Guntur Podi Dosa, Filter Coffee, aromatic ghee aromas, stainless steel tumbler service.
```

### Full AI Generated Review
> **Restaurant:** Dakshin Delight, Navrangpura, Ahmedabad  
> **Rating:** 4.7/5 ⭐  
> **Cuisine:** Authentic Karnataka & Tamil Nadu South Indian Tiffins  
> **The Vibe:** Minimalist brass accents, nostalgic Carnatic instrumental music, and the intoxicating aroma of sizzling pure desi ghee.  
> **Must-Try Dishes:** Davanagere Benne Dosa, Guntur Podi Ghee Roast, Classic Degree Filter Coffee.  
> **The Experience:**  
> Dakshin Delight brings authentic Bengaluru tiffin culture straight to Navrangpura. The Davanagere Benne Dosa is a triumph—golden, pillowy, and soaked in authentic white butter with a mildly spiced potato palya that melts instantly. The Guntur Podi Dosa packs a fierce roasted chili kick tempered by creamy coconut chutney. Ending the meal with their piping-hot filter coffee served frothing in a traditional brass tumbler is non-negotiable.  
> **Damage for Two:** ₹380.  
> **Pro-Tip:** Arrive before 8:30 AM on Sunday mornings to grab a table without waiting in the outdoor token queue.

---

## 📌 Task 3: Few-Shot Prompting — Flipkart Product Descriptions

### Concept Definition
*Few-Shot prompting* provides multiple exemplars (typically 3 to 5) that demonstrate subtle stylistic nuances, feature bulleting, technical specifications, and target buyer persona hooks before prompting for the target item.

### Exact Few-Shot Prompt Used
```text
You are an expert e-commerce copywriter for Flipkart. Follow the exact style, tone, and 4-tier structured format shown in the 3 examples below to write a product listing description for a new Smartwatch.

---
### EXAMPLE 1 (Category: Mobile Phone)
Product: Realme Narzo 60 Pro 5G
Tagline: Speed Meets Ultra-Curved Elegance
Key Specs:
- 120Hz Curved AMOLED Display with 950 nits peak brightness
- 100MP OIS Street Photography Camera
- MediaTek Dimensity 7050 5G Processor
- 5000mAh Battery with 67W SUPERVOOC Charge
The Hook: Engineered for heavy multitaskers and binge-watchers who demand flagship screen aesthetics without flagship prices.
Warranty & Inside Box: 1 Year Manufacturer Warranty; Handset, 67W Charger, Cable, Protective Case.

---
### EXAMPLE 2 (Category: Headphones)
Product: boAt Rockerz 551ANC
Tagline: Silence the Chaos, Unleash the Bass
Key Specs:
- Hybrid Active Noise Cancellation up to 35dB
- Massive 100 Hours Playtime with ASAP Fast Charge (10 mins = 10 hrs)
- 40mm Dynamic Drivers with Signature boAt Bass
- Ambient Sound Mode for quick outdoor situational awareness
The Hook: Built for commuters and hostel students seeking uninterrupted focus in noisy environments.
Warranty & Inside Box: 1 Year Warranty; Headphones, Type-C Charging Cable, AUX Cable, User Manual.

---
### EXAMPLE 3 (Category: Running Shoes)
Product: Puma Nitro Velocity 3
Tagline: Featherlight Cushioning for Everyday Miles
Key Specs:
- Advanced NITROFOAM™ responsive cushioning technology
- PUMAGRIP high-traction multi-surface rubber outsole
- Engineered breathable mesh upper with reflective accents
- TPU heel spoiler for gait stability and stride guidance
The Hook: The ultimate daily trainer for fitness enthusiasts transitioning from 5K jogs to full half-marathons.
Warranty & Inside Box: 3 Months Brand Warranty; 1 Pair Running Shoes.
---

### YOUR TURN:
Generate a product listing description matching the EXACT format above for:
Product: Noise ColorFit Ultra 3 Smartwatch (Bluetooth Calling, 1.96-inch AMOLED display, metallic chassis, health suite).
```

### Full AI Generated Product Description
> ### Product: Noise ColorFit Ultra 3 Smartwatch  
> **Tagline:** Monumental Display, Seamless Wrist Connectivity  
> **Key Specs:**  
> - 1.96-inch Always-On AMOLED Display with 410x502 resolution and 500 nits brightness  
> - Single-chip Bluetooth 5.3 Calling with functional metallic rotating crown  
> - Comprehensive Noise Health Suite: 24/7 Heart Rate, SpO2, Sleep Tracking, and Stress Monitor  
> - Premium Metallic Chassis with IP68 Water and Dust Resistance  
> - Up to 7-Day Battery Life (2-Day standby with active Bluetooth calling)  
> **The Hook:** Crafted for modern working professionals and fitness enthusiasts who demand executive boardroom elegance alongside high-precision daily wellness tracking.  
> **Warranty & Inside Box:** 1 Year Manufacturer Warranty; Smartwatch, Magnetic Charging Cable, User Manual, Quick Start Guide.

---

## 📌 Task 4: Comparative Study — Spotify 'Monsoon Vibes' Playlist Description

### 1. Zero-Shot Implementation
* **Prompt:**
  ```text
  Write a Spotify playlist description for a playlist named 'Monsoon Vibes'.
  ```
* **AI Output:**
  > *"Enjoy the rainy days with soothing melodies and romantic tracks. Perfect songs for chai, pakoras, and watching the raindrops fall outside your window."*

---

### 2. One-Shot Implementation
* **Prompt:**
  ```text
  Write a Spotify playlist description. Follow this example format:
  
  Example:
  Title: Chai & Acoustic
  Description: Warm sips, gentle strings, and acoustic unplugged Hindi tracks to slow down your morning. Features Prateek Kuhad, Jasleen Royal, and Anuv Jain. Updated weekly.
  
  Task:
  Title: Monsoon Vibes
  Description:
  ```
* **AI Output:**
  > *"Title: Monsoon Vibes*  
  > *Description: Petrichor in the air, rhythmic raindrops, and soulful lo-fi Hindi melodies to romanticize your monsoon afternoons. Features Arijit Singh, Mohit Chauhan, and Amit Trivedi. Updated weekly."*

---

### 3. Few-Shot Implementation
* **Prompt:**
  ```text
  You write official curated Spotify playlist descriptions. Here are 3 approved examples:
  
  1. Title: Desi Indie Chill
     Header: Mellow guitars & independent Indian voices.
     Vibe Tags: [Indie, Melancholy, Acoustic]
     Featured Artists: Anuv Jain, Parekh & Singh, When Chai Met Toast.
     Length: 2 sentences. Max 35 words.
  
  2. Title: Late Night Drive India
     Header: Hypnotic synthwaves and midnight highway anthems.
     Vibe Tags: [Electronic, Synth, Midnight]
     Featured Artists: Lifafa, Nucleya, Zaeden, Ritviz.
     Length: 2 sentences. Max 35 words.
  
  3. Title: Punjabi Coffeehouse
     Header: Cozy acoustic strings paired with soulful folk-pop lyrics.
     Vibe Tags: [Folk-Pop, Cozy, Soul]
     Featured Artists: Prabh Deep, Amrinder Gill, Talwiinder.
     Length: 2 sentences. Max 35 words.
  
  Now generate the description for:
  Title: Monsoon Vibes
  ```
* **AI Output:**
  > **Title:** Monsoon Vibes  
  > **Header:** Soul-stirring petrichor melodies and nostalgic monsoon ballads.  
  > **Vibe Tags:** [Rain, Soulful Melancholy, Lo-Fi Hindi]  
  > **Featured Artists:** Mohit Chauhan, Lucky Ali, Papon, Shreya Ghoshal.  
  > **Description:** Let gentle acoustic strums and rain-washed melodies keep you company while savoring hot cutting chai. The ultimate soundtrack for cloudbursts and nostalgic reveries.

---

### 4. Comparative Synthesis & Evaluation

| Prompting Methodology | Relevance & Tone | Schema Consistency | Quality Score | Best Suited For |
| :--- | :--- | :--- | :---: | :--- |
| **Zero-Shot** | Cliché, generic ("chai & pakoras"), lacks artist attribution. | Freeform, single unstructured paragraph. | **6.5 / 10** | Quick exploratory brainstorming or simple direct questions. |
| **One-Shot** | Captures musical feel and names specific artists. | Mirrors the exact 2-sentence pattern with updates. | **8.5 / 10** | Tasks where a single template is sufficient to constrain the structure. |
| **Few-Shot** | Richly atmospheric, precise metadata tags, curated artist synergy. | Strictly conforms to the multifaceted multi-field schema (Tags, Header, Artists, Word Limit). | **10 / 10** | Production applications, API integrations, and catalog publishing requiring consistent schema. |

### Conclusion: Which Method Gave the Most Relevant Result and Why?
**Few-Shot Prompting gave the most relevant result.**
* **Algorithmic Priming:** Showing three diverse yet structurally identical exemplars primes the transformer's self-attention layers to distinguish invariant structural rules (e.g., Header, Vibe Tags, Featured Artists) from variable content.
* **Tone & Vocabulary Calibration:** The model learned the exact cadence of Spotify's editorial curation voice rather than falling back on predictable generic internet stereotypes.
* **Downstream Integration:** The few-shot output is directly parseable into structured UI components (chips, badges, metadata headers).

---
*End of Session 03 Assignment.*
