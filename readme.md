 """# 🎮 Steam Marketplace Analytics

Insights on how **price** and **genre** relate to **review quality** and **audience reach** across Steam games. The project is designed to surface **publisher-ready findings** (e.g., high-performing genres, free-to-play vs paid trade-offs, and quality vs audience patterns) and present them in a compact, interactive dashboard.

---

## Overview

This project ingests a Steam marketplace dataset and computes a small set of derived metrics to analyze relationships between pricing, genres, and audience/quality proxies. The results are explored via an interactive dashboard that lets you filter, sort, and inspect representative titles.

**What it does**
- **Ingests marketplace data** for Steam titles (name, release date, price, genres, ratings, owners).
- **Derives core metrics** used throughout the analysis:
  - `review_total = positive_ratings + negative_ratings`
  - `review_score = positive_ratings / review_total` (quality proxy, 0–1)
  - `main_genre` = first genre token (for clean grouping)
  - `owners_num` ≈ numeric lower bound parsed from the owners range (audience proxy)
- **Analyzes relationships** (no price-band bucketing):
  - Price ↔ Review quality (overall and by genre)
  - Genre performance (quality, audience, typical price)
  - Differences between **free-to-play** and **paid** titles (when inferable from price/metadata)
- **Presents insights visually**:
  - **Filters:** genre, price cap, minimum total reviews (reduce noise)
  - **KPIs:** games count, average price, average review score, median owners
  - **Charts:** Price vs Review Score; Top Genres by average review score
  - **Sample Games table:** sortable by review quality, review volume, owners (approx), price (low→high), newest first

---

## Repository Structure

steam-marketplace-analytics/
├─ data/
│ └─ steam_games.csv # raw marketplace data (CSV)
│
├─ app/
│ └─ streamlit_app.py # interactive dashboard (filters, KPIs, charts, table)
│
├─ scripts/
│ └─ eda_steam_games.py # lightweight exploratory analysis; saves reference charts
│
├─ outputs/
│ ├─ price_vs_review_score.png # generated artifacts used in write-ups
│ ├─ top_genres_avg_review.png
│ └─ *.csv / *.png # additional exports as needed
│
├─ assets/
│ └─ screenshots_for_readme.png # optional screenshots embedded in README
│
├─ requirements.txt
└─ README.md

yaml
Always show details

Copy code

**Key components**
- **`data/steam_games.csv`** – Source dataset with fields like  
  `name, release_date, price, genres, positive_ratings, negative_ratings, owners`.
- **`app/streamlit_app.py`** – Dashboard logic: parsing, derived metrics, filters, KPIs, charts, sortable sample table.
- **`scripts/eda_steam_games.py`** – One-off exploration to generate baseline plots and CSV summaries saved into `outputs/`.
- **`outputs/`** – Evidence for insights (charts/tables) referenced in this README or presentations.
- **`assets/`** – Optional screenshots for documentation.

---

## Data Dictionary (project-relevant fields)

- **`price`** *(float)* – Listed price in USD.  
- **`genres`** *(string; “A;B;C”)* – Semicolon-separated genres; **`main_genre`** takes the first token.  
- **`positive_ratings`, `negative_ratings`** *(int)* – Counts of user ratings; combined into **`review_total`** and **`review_score`**.  
- **`owners`** *(string range)* – e.g., “1,000,000 .. 2,000,000”; parsed into **`owners_num`** (lower bound) for approximate audience size.  
- **`release_date`** *(date/string)* – Parsed to enable “Newest first” sorting and optional recency filters.

---

## Method (Conceptual)

1. **Parse & derive**: compute `review_total`, `review_score`, `main_genre`, `owners_num`; parse dates.  
2. **Filter controls**: genre, price cap, minimum review volume to reduce small-sample noise.  
3. **Visualize & compare**:  
   - Scatter: *Price vs Review Score* (overall and by genre via filtering)  
   - Bar: *Top Genres by Avg Review Score*  
   - KPIs: quick, high-signal summaries for the current filtered view  
4. **Inspect exemplars**: the Sample Games table highlights representative titles under the chosen criteria (with flexible sorting).

---

## Example Insights (replace with your real numbers)

- **Top genres by quality and audience:** e.g., *RPG* and *Strategy* show the highest average review scores while retaining strong median owners.  
- **Price–quality relationship:** overall correlation is typically weak to mildly negative; some genres buck the trend.  
- **Free-to-play vs paid:** F2P titles tend to reach larger audiences (owners) but show lower average review scores compared to paid titles.  
- **Recency patterns (optional):** newer releases in certain genres maintain competitive quality at mid-range prices.

---

## Assumptions & Limitations

- **Owners** is a range; **`owners_num`** uses the lower bound as an approximation.  
- **Review score** (positives / total) is a **quality proxy**; it is not a perfect measure of long-term engagement.  
- Genre labels and metadata quality vary across titles; minor normalization is applied.  
- This analysis is **observational**; relationships are correlational rather than causal.

---

## Attribution

- Dataset from publicly available Steam store data (Kaggle-hosted dump).  
- Built for portfolio demonstration: publisher-oriented analytics, interactive exploration, and concise storytelling.
"""
