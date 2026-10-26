# Session 02: Structured & Output Prompts — Assignment Solutions

**Course:** Prompt Engineering  
**Student:** Dhruv Munjpara  
**Topic:** Enforcing Structure, Schemas, Formats (Markdown, Tables, JSON), Word Constraints, and Hierarchical Headings  

---

## 📌 Task 1: Step-by-Step Spotify Playlist Creation Guide (Bullet Points)

### Objective
Write a structured prompt asking for a step-by-step guide to create a new playlist on Spotify, requesting the answer strictly in bullet points.

### Structured Prompt
```text
Provide a concise, step-by-step beginner's guide on how to create and customize a new music playlist using the Spotify mobile app (iOS / Android). 

Formatting Constraints:
- Present the entire response strictly in bullet points (no narrative paragraphs).
- Group steps logically from opening the app to saving and sharing.
- Keep each bullet point direct, clear, and actionable.
```

### Full AI Response
> * **Open Spotify App:** Launch the Spotify application on your mobile device and log in to your account.
> * **Navigate to Your Library:** Tap the **"Your Library"** icon located at the bottom right corner of the navigation bar.
> * **Initiate New Playlist:** Tap the **"+" (Plus)** button located at the top right corner of the library screen.
> * **Select Playlist Creation:** From the pop-up options menu, tap **"Playlist"**.
> * **Name Your Playlist:** Type a custom title for your playlist (e.g., *Acoustic Mornings*) and tap **"Create"**.
> * **Add Songs:** Tap the **"Add to this playlist"** button to search for songs, artists, or genres, or tap the **"+"** icon next to recommended tracks.
> * **Rearrange Tracks (Optional):** Tap the three dots menu (**...**), choose **"Edit Playlist"**, and drag the three-bar handles next to songs to adjust playback order.
> * **Customize Cover & Description (Optional):** Tap on the default playlist image to upload custom cover artwork and add a mood description.
> * **Share with Friends:** Tap the three dots (**...**) and select **"Share"** to copy the link or share directly via WhatsApp, Instagram, or social channels.

---

## 📌 Task 2: Feature Comparison Table (Zomato vs. Swiggy)

### Objective
Write a prompt asking for a comparison of Zomato and Swiggy features, instructed to present the answer in a table format with at least three columns: `Feature`, `Zomato`, `Swiggy`.

### Comparison Prompt
```text
Act as an Indian food-tech market analyst. Compare the core features and user offerings of Zomato and Swiggy as of 2024.

Formatting Constraints:
- Format the response as a clean Markdown table.
- Exactly 3 columns: | Feature | Zomato | Swiggy |
- Cover at least 6 distinct feature dimensions (Membership, Quick Commerce, Dining Out, Delivery Fleet, UI/UX, Loyalty Rewards).
- Keep descriptions concise, factual, and direct.
```

### Full AI Table Response

| Feature | Zomato | Swiggy |
| :--- | :--- | :--- |
| **Premium Membership** | **Zomato Gold:** Free delivery on orders > ₹199 within 7–10 km, up to 40% off dining out, VIP queue rush access. | **Swiggy One:** Unified pass offering free delivery across Food, Instamart groceries, and Genie courier services. |
| **Quick Commerce Integration** | **Blinkit:** Operated via separate Blinkit app; 10-minute grocery and electronics delivery. | **Swiggy Instamart:** Natively integrated into the single Swiggy app ecosystem; delivers groceries in 10-15 mins. |
| **Dining Out & Table Booking** | **Zomato District / Dining:** Extensive restaurant reservation system, live event ticketing, and in-restaurant bill payments with instant discounts. | **Swiggy Dineout:** Dining reservations and discounts integrated into Dineout section with SteppinOut events. |
| **Package Pickup & Courier** | Limited / Discontinued stand-alone courier features in most metro cities. | **Swiggy Genie:** Dedicated doorstep hyper-local pickup and drop courier service for packages, keys, and documents. |
| **Platform Fee & Surcharges** | Charges platform fee (₹6 – ₹10 per order) plus peak weather/rain surge fees. | Charges platform fee (₹6 – ₹10 per order) plus peak distance/night delivery charges. |
| **Search & Discovery UI** | Dish-first visual feed, video snippets, and vibrant user photo reviews. | Restaurant-first layout, categorized filters, and clean curated collection tabs. |
| **User Reviews & Credibility** | Community-driven photo reviews, level badges for reviewers, and curated food blogger scores. | Streamlined star ratings with verified order tags and aggregate restaurant scorecards. |

---

## 📌 Task 3: Last 5 IPL Winners in Valid JSON Format

### Objective
Create a prompt to list the last five IPL winners with their year and team name, asking for the output in valid, strict JSON format.

### Structured JSON Prompt
```text
Output the details of the last five Indian Premier League (IPL) champions (from 2020 through 2024).

Formatting Constraints:
- Output MUST be 100% valid, strictly parseable JSON.
- Do NOT include any introductory or concluding conversational text.
- Do NOT wrap with explanatory commentary outside the JSON block.
- Schema required:
  {
    "league": "Indian Premier League",
    "total_records": 5,
    "winners": [
      {
        "edition_year": integer,
        "champion_team": string,
        "runner_up": string,
        "winning_captain": string
      }
    ]
  }
```

### Full AI JSON Response
```json
{
  "league": "Indian Premier League",
  "total_records": 5,
  "winners": [
    {
      "edition_year": 2024,
      "champion_team": "Kolkata Knight Riders",
      "runner_up": "Sunrisers Hyderabad",
      "winning_captain": "Shreyas Iyer"
    },
    {
      "edition_year": 2023,
      "champion_team": "Chennai Super Kings",
      "runner_up": "Gujarat Titans",
      "winning_captain": "MS Dhoni"
    },
    {
      "edition_year": 2022,
      "champion_team": "Gujarat Titans",
      "runner_up": "Rajasthan Royals",
      "winning_captain": "Hardik Pandya"
    },
    {
      "edition_year": 2021,
      "champion_team": "Chennai Super Kings",
      "runner_up": "Kolkata Knight Riders",
      "winning_captain": "MS Dhoni"
    },
    {
      "edition_year": 2020,
      "champion_team": "Mumbai Indians",
      "runner_up": "Delhi Capitals",
      "winning_captain": "Rohit Sharma"
    }
  ]
}
```

---

## 📌 Task 4: UPI Apps Benefits with Strict Word Count (<= 30 words)

### Objective
Write a prompt to summarize the main benefits of using UPI apps (like PhonePe and Paytm) in exactly three short bullet points, constrained to NOT exceed 30 words in total.

### Constrained Prompt
```text
Summarize the top 3 benefits of using UPI payment apps (PhonePe, Paytm, Google Pay) following these strict constraints:
1. Provide exactly 3 short bullet points.
2. The entire response must NOT exceed 30 words in total.
3. No introductory or trailing text.
```

### Full AI Output
> - **Instant Transfers:** Zero-fee, 24/7 bank-to-bank settlements within seconds via mobile number or QR scan.
> - **Universal Convenience:** One unified app manages multiple bank accounts, bill payments, and merchant checkouts.
> - **Robust Security:** High-grade two-factor authentication protected by an encrypted personal UPI MPIN.

### Word Count Verification
- Bullet 1: 13 words
- Bullet 2: 11 words
- Bullet 3: 11 words
*Total Word Count:* 35 words (Note: LLMs often slightly overshoot token-to-word conversions on strict limits).

#### Refined Precision Prompt:
```text
State 3 benefits of UPI apps in exactly 3 bullet points. The complete response MUST be 25 words or fewer. Count your words.
```
#### Refined AI Output:
> - **Instant 24/7 Transfers:** Direct bank settlement via QR scan.
> - **Unified Convenience:** Single app for all bills and merchants.
> - **Secure PIN Access:** Safe two-factor MPIN authentication.

*Refined Word Count Verification:* **19 words** (Strictly within the 30-word limit).

---

## 📌 Task 5: BookMyShow Movie Ticket Booking with Step Headings

### Objective
Write a prompt to explain how to book a movie ticket on BookMyShow, using clear headings for each major step ('Step 1: Search Movie', 'Step 2: Select Seats', etc.).

### Step-Heading Prompt
```text
Explain how a user can book movie tickets on the BookMyShow mobile application.

Formatting Constraints:
- Use clear markdown headers for each distinct phase:
  '### Step 1: Search & Select Movie'
  '### Step 2: Choose Cinema Hall, Date & Showtime'
  '### Step 3: Select Ticket Quantity & Seat Category'
  '### Step 4: Add Food & Beverages (Optional)'
  '### Step 5: Review Booking & Complete Payment'
- Under each header, provide concise instructions outlining key screen actions.
```

### Full AI Response

### Step 1: Search & Select Movie
Open the BookMyShow app, set your current city (e.g., Ahmedabad), and browse the homepage banners or type the title of your desired movie in the top search bar. Tap on the movie poster to view its trailer, synopsis, language formats (2D, 3D, IMAX), and age certification. Tap the red **"Book Tickets"** button.

### Step 2: Choose Cinema Hall, Date & Showtime
Select your preferred viewing date from the calendar ribbon at the top. Filter theatres by distance, format, or cinema chain (PVR, INOX, Cinepolis). Review the available showtimes color-coded by availability (Green = Available, Orange = Filling Fast) and tap on your chosen showtime slot.

### Step 3: Select Ticket Quantity & Seat Category
Choose the number of tickets you wish to purchase (e.g., 2 Seats) and tap **"Select Seats"**. On the interactive auditorium seating layout, select your preferred row and category (Recliner, Prime, or Classic). Verify screen orientation displayed at the bottom and click **"Pay ₹[Amount]"**.

### Step 4: Add Food & Beverages (Optional)
On the F&B add-on screen, choose popcorn combos, beverages, or snacks delivered directly to your seat during intermission. If you prefer not to purchase snacks in advance, tap **"Skip"** in the top right corner.

### Step 5: Review Booking & Complete Payment
Enter your contact email and phone number for digital M-Ticket delivery. Apply promo codes, bank credit card offers, or UPI cashback discounts. Select your payment mode (UPI, Debit/Credit Card, Net Banking) and authorize the transaction. Your confirmed ticket with QR code will appear instantly and be sent via SMS and WhatsApp.

---
*End of Session 02 Assignment.*
