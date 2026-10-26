# Session 01: Prompt Basics — Assignment Solutions

**Course:** Prompt Engineering  
**Student:** Dhruv Munjpara  
**Topic:** Foundations of Prompt Engineering: Clarity, Context, Common Mistakes, and Quality Evaluation  

---

## 📌 Task 1: Clear vs. Unclear Prompts (Trending Songs in India)

### Objective
Write two prompts for ChatGPT:
1. **Unclear Prompt:** Asking for a list of trending songs in India.
2. **Clear Prompt:** Asking for a list of trending Bollywood songs released after 2022 with artist names.
3. Compare the responses and note the difference in detail and relevance.

---

### 1. Unclear Prompt
```text
List trending songs in India.
```

#### ChatGPT Response to Unclear Prompt:
> Here are some trending songs in India right now:
> 1. Tauba Tauba
> 2. Illuminati
> 3. Aaj Ki Raat
> 4. Big Dawgs
> 5. Winning Speech
> 6. O Sajni Re
> 7. Aayi Nai
> 8. Soulmate
> 9. Husn
> 10. Chuttamalle

---

### 2. Clear Prompt
```text
Provide a curated list of 5 trending Bollywood Hindi film songs released after 2022. For each song, include:
1. Song Title
2. Movie / Album Name
3. Release Year
4. Primary Singer(s) & Music Composer
5. Genre / Vibe (e.g., Party, Romantic ballad, Soulful)
```

#### ChatGPT Response to Clear Prompt:
> Here is a curated list of trending Bollywood Hindi songs released after 2022:
>
> 1. **Song Title:** *Tauba Tauba*
>    - **Movie:** *Bad Newz*
>    - **Release Year:** 2024
>    - **Primary Singer(s) & Composer:** Karan Aujla (Singer & Composer)
>    - **Genre / Vibe:** High-energy Punjabi-Bollywood Dance / Party Anthem
>
> 2. **Song Title:** *O Sajni Re*
>    - **Movie:** *Laapataa Ladies*
>    - **Release Year:** 2024
>    - **Primary Singer(s) & Composer:** Arijit Singh (Singer), Ram Sampath (Composer)
>    - **Genre / Vibe:** Soulful Romantic Melancholy
>
> 3. **Song Title:** *Aaj Ki Raat*
>    - **Movie:** *Stree 2*
>    - **Release Year:** 2024
>    - **Primary Singer(s) & Composer:** Madhubanti Bagchi & Divya Kumar (Singers), Sachin-Jigar (Composers)
>    - **Genre / Vibe:** Uptempo Folk-Electronic Dance
>
> 4. **Song Title:** *Chaleya*
>    - **Movie:** *Jawan*
>    - **Release Year:** 2023
>    - **Primary Singer(s) & Composer:** Arijit Singh & Shilpa Rao (Singers), Anirudh Ravichander (Composer)
>    - **Genre / Vibe:** Breezy Romantic Pop
>
> 5. **Song Title:** *Tere Pyaar Mein*
>    - **Movie:** *Tu Jhoothi Main Makkaar*
>    - **Release Year:** 2023
>    - **Primary Singer(s) & Composer:** Arijit Singh & Nikhita Gandhi (Singers), Pritam (Composer)
>    - **Genre / Vibe:** Vibrant Peppy Romance

---

### 3. Comparison & Analysis
| Evaluation Parameter | Unclear Prompt Response | Clear Prompt Response |
| :--- | :--- | :--- |
| **Specificity & Focus** | Mixes Malayalam (Illuminati), English Rap (Big Dawgs), Punjabi, and Hindi arbitrarily. | Exclusively targets Bollywood Hindi releases. |
| **Temporal Accuracy** | Does not guarantee release year criteria. | Strictly respects the post-2022 boundary (2023 & 2024). |
| **Metadata & Detail** | Only lists bare titles without credits or context. | Supplies Singer, Composer, Film, and Musical Mood. |
| **Actionability** | Requires follow-up prompts to obtain details. | Ready for immediate use in playlists or articles. |

**Key Takeaway:** Unclear prompts force the LLM to make statistical guesses regarding language, genre, and metadata level. Adding explicit constraints (language, time window, required fields) eliminates ambiguity and yields production-grade output on the first turn.

---

## 📌 Task 2: 3 Common Prompting Mistakes with Do's & Don'ts

### Mistake 1: Extreme Ambiguity (Lack of Constraints)
* **Explanation:** Assuming the model understands your personal taste, location, or unstated requirements without giving criteria.
* **Scenario:** Ordering food on Zomato.
* **Don't Example:**
  > *"Suggest something good to eat for dinner."*
* **Do Example:**
  > *"Recommend 3 vegetarian North Indian dinner combos under ₹350 available for delivery in Navrangpura, Ahmedabad on Zomato. Include restaurant name, dish name, and approximate delivery time."*

---

### Mistake 2: Missing Format and Length Specifications
* **Explanation:** Not specifying the desired structure, resulting in overwhelming walls of conversational text instead of structured data.
* **Scenario:** Booking a movie on BookMyShow.
* **Don't Example:**
  > *"Tell me about the new movies in theaters this weekend."*
* **Do Example:**
  > *"List the top 3 movies currently playing in IMAX theaters on BookMyShow. Present the output in a markdown table with columns: Movie Name, Language, Certification (UA/A), Duration, and IMDb Rating."*

---

### Mistake 3: Conflicting or Multi-intent Overload
* **Explanation:** Blending multiple unrelated tasks into a single run-on sentence without logical ordering or criteria.
* **Scenario:** Choosing a cinema and booking snacks on BookMyShow.
* **Don't Example:**
  > *"Find me a horror movie, also tell me about popcorn prices, check if seats are cheap and should I go to PVR or Inox?"*
* **Do Example:**
  > *"I want to watch a horror movie at PVR or INOX this Friday evening. Step 1: Recommend the highest-rated horror movie currently showing. Step 2: Compare ticket pricing between PVR and INOX for evening shows. Step 3: List popular snack combo prices."*

---

## 📌 Task 3: Restaurant Review Generation (Vague vs. Detailed)

### Scenario
Generating a restaurant review for a newly opened café.

### 1. Vague Prompt
```text
Write a review for a new cafe.
```

#### ChatGPT Output (Vague Prompt):
> **A Charming New Spot in Town! ⭐⭐⭐⭐☆**
> 
> I recently visited this lovely new café and had a wonderful experience. The vibe is cozy and welcoming with great background music. The coffee was fresh, and the pastries were delicious. The staff was friendly and attentive. Whether you want to catch up with friends or read a book, this place is definitely worth checking out!

---

### 2. Detailed Prompt
```text
Write a detailed, authentic customer review for a newly opened café named 'The Bohemian Roast'. Include the following specifics:
- Cuisine: Artisanal specialty coffee, sourdough toasts, and vegan pastries.
- Ambience: Minimalist Scandinavian aesthetic, abundant indoor plants, natural sunlight, and quiet work-friendly seating with charging sockets.
- Price Range: Moderate (₹600 - ₹800 for two people).
- Specific Highlight: The signature Iced Spanish Latte and Truffle Mushroom Sourdough.
- Constructive Feedback: Suggest slightly faster service during peak weekend brunch hours.
- Tone: Enthusiastic, foodie-friendly, and balanced.
```

#### ChatGPT Output (Detailed Prompt):
> **Review: 'The Bohemian Roast' — A Sunlit Haven for Specialty Coffee Lovers (4.5/5 ⭐)**
>
> Stepping into **The Bohemian Roast** feels like walking into an airy Scandinavian design studio. Bathed in natural sunlight with cascading monstera plants, blonde wood tables, and conveniently placed power sockets at every nook, it is effortlessly tailored for remote work or peaceful weekend mornings.
>
> The culinary spread is distinctively refined. The **Truffle Mushroom Sourdough** was stellar—earthy, rich, and balanced on a blistered, crunchy sourdough crust. Pairing it with their signature **Iced Spanish Latte** was a treat; the espresso was smooth, boasting rich notes of caramel and hazelnut without being cloyingly sweet. Their vegan pistachio croissant is also a must-try.
>
> At approximately **₹700 for two**, the pricing is fair for artisanal specialty ingredients. The only slight hiccup was the wait time—weekend brunch rush slowed down food delivery by around 20 minutes. However, the warm, hospitable staff handled the crowd gracefully. Highly recommended for digital nomads and serious coffee purists!

---

### 3. Critical Evaluation: Which is Better and Why?
**The Detailed Prompt output is significantly superior.**
* **Authenticity & Texture:** The vague output is generic and could describe literally any café on Earth ("fresh coffee", "delicious pastries"). The detailed output features sensory descriptions ("blistered crunchy sourdough crust", "notes of caramel and hazelnut").
* **Target Audience Relevance:** The detailed prompt provides utility to readers—noting remote-work feasibility (charging sockets), actual pricing (₹700 for two), and specific dish recommendations.
* **Balanced Credibility:** By including a minor constructive critique (weekend service speed), the review reads like a genuine human customer review rather than generic AI marketing fluff.

---

## 📌 Task 4: App Feature Prompting — Flipkart Product Recommendation Engine

### App Feature Selected
**Flipkart's "You Might Also Like" Personalized Carousel / Recommendation Notification**

### Prompt Designed Following 3 Core Do's
```text
Role: You are an e-commerce personalization copywriter for Flipkart.
Task: Generate 3 personalized product recommendation push notifications for a user who recently purchased a 'Sony WH-1000XM5 Noise Cancelling Headphones'.

Follow these strict guidelines (The 3 Do's):
1. [Do Specify Context & Persona]: Speak directly to an audiophile and tech enthusiast who values premium build and gadget care.
2. [Do Define Structure & Formatting]: Present each notification in the format:
   - Header (Max 6 words, catchy with an emoji)
   - Body (Max 20 words, highlighting synergy with their headphones)
   - Recommended Product Category & Suggested Item
   - Call to Action (CTA button text)
3. [Do Set Tone & Guardrails]: Keep the tone enthusiastic, helpful, and premium. Do not use generic spammy words like 'Hurry Buy Now' or 'Cheapest Offer'.
```

#### Generated AI Output:
> **Option 1: Protection & Travel**
> - **Header:** 🎧 Protect Your Sound Sanctuary
> - **Body:** Pair your Sony XM5 with a military-grade hardshell travel case. Water-resistant, compact, and tailored for your journeys.
> - **Recommended Product:** Spigen Rugged Armor Headphone Travel Case
> - **CTA:** Explore Cases
>
> **Option 2: High-Fidelity Audio Accessory**
> - **Header:** 🎵 Elevate Every Single Note
> - **Body:** Unlock loss-free studio audio on your smartphone with a dedicated 32-bit Hi-Res Type-C DAC amplifier dongle.
> - **Recommended Product:** Audiocular D07 Hi-Res USB-C DAC Dongle
> - **CTA:** Upgrade Audio
>
> **Option 3: Ergonomic Workspace Setup**
> - **Header:** 🪵 A Worthy Home for XM5
> - **Body:** Keep your desk clutter-free with an ergonomic solid walnut wood and aluminum headphone stand.
> - **Recommended Product:** Gizga Essentials Wooden Desktop Headphone Stand
> - **CTA:** View Desk Stands

---
*End of Session 01 Assignment.*
