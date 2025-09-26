# 🎮 Steam Marketplace Analytics

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

```
steam-marketplace-analytics/
├─ data/
│  └─ steam_games.csv                  # raw marketplace data (CSV)
│
├─ app/
│  └─ streamlit_app.py                 # interactive dashboard (filters, KPIs, charts, table)
│
├─ scripts/
│  └─ eda_steam_games.py               # lightweight exploratory analysis; saves reference charts
│
├─ outputs/
│   ├─ price_vs_review_score.png       # generated artifacts used in write-ups
│   ├─ top_genres_avg_review.png
│   └─ *.csv / *.png                   # additional exports as needed
│
├─ requirements.txt
└─ README.md
```

**Key components**
- **`data/steam_games.csv`** – Source dataset with fields like  
  `name, release_date, price, genres, positive_ratings, negative_ratings, owners`.
- **`app/streamlit_app.py`** – Dashboard logic: parsing, derived metrics, filters, KPIs, charts, sortable sample table.
- **`scripts/eda_steam_games.py`** – One-off exploration to generate baseline plots and CSV summaries saved into `outputs/`.
- **`outputs/`** – Evidence for insights (charts/tables) referenced in this README or presentations.



---


