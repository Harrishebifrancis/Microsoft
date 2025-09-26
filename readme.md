🎮 Steam Marketplace Analytics

A focused analytics project that examines how price and genre relate to review quality and audience reach across Steam games. The goal is to surface publisher-ready insights (e.g., high-performing genres, trade-offs between free-to-play and paid, and quality vs. audience patterns) and present them in a compact, interactive dashboard.

What this project does

Ingests marketplace data for Steam titles (name, release date, price, genres, ratings, owners).

Derives core metrics used throughout the analysis:

review_total = positive_ratings + negative_ratings

review_score = positive_ratings / review_total (quality proxy, 0–1)

main_genre = first genre token (for clean grouping)

owners_num ≈ numeric lower bound parsed from the owners range (audience proxy)

Analyzes relationships (no price-band bucketing):

Price ↔ Review quality (overall and by genre)

Genre-level performance (quality, audience, typical price)

Differences between free-to-play and paid titles (if identifiable from price/metadata)

Presents insights visually in an interactive dashboard:

Filters: genre, price cap, minimum review volume (to avoid low-signal titles)

KPIs: games count, average price, average review score, median owners

Charts: Price vs Review Score; Top Genres by average quality

Sample Games table with configurable sorting (quality, review volume, owners, price ascending, newest first)

Examples of the insights it’s built to reveal

Genres that pair high review quality with strong audience reach.

Overall price–quality relationship (often weak/negative) plus genre-specific exceptions.

Differences in audience and quality between free-to-play and paid titles.

(Replace this section with 3–5 concise bullets backed by numbers from your outputs.)

Repository structure
steam-marketplace-analytics/
├─ data/
│  └─ steam_games.csv
│
├─ app/
│  └─ streamlit_app.py
│
├─ scripts/
│  └─ eda_steam_games.py
│
├─ outputs/
│   ├─ price_vs_review_score.png
│   ├─ top_genres_avg_review.png
│   └─ *.csv / *.png (generated artifacts)
│
├─ assets/
│  └─ screenshots for README (optional)
│
├─ requirements.txt
└─ README.md

What each piece is for

data/steam_games.csv
Raw marketplace data. Expected columns typically include:
name, release_date, price, genres, positive_ratings, negative_ratings, owners.

app/streamlit_app.py
The interactive dashboard:

Filters for genre, price cap, minimum total reviews

KPIs (games count, avg price, avg review score, median owners)

Price vs Review Score scatter; Top Genres bar chart

Sample Games table with sorting options:

Review score (quality)

Total reviews (volume)

Owners (approx)

Price (low→high)

Newest first

scripts/eda_steam_games.py
Lightweight exploratory script:

Cleans/derives core fields (review_total, review_score, main_genre, owners_num)

Produces reference charts saved to outputs/ for use in your write-up

outputs/
Generated artifacts (PNGs/CSVs) that back the insights you summarize in this README.

assets/
Optional screenshots of the dashboard for documentation.

requirements.txt
Python dependencies (analytics + visualization stack).

How the parts fit together (conceptual flow)

Data layer → data/steam_games.csv
Minimal cleaning + creation of derived fields.

Analysis layer → scripts/
Reusable transforms and reference plots that quantify relationships.

Presentation layer → app/streamlit_app.py
Interactive exploration to validate patterns, communicate findings, and capture screenshots.

Artifacts → outputs/
Concrete evidence (charts/tables) cited in your conclusions and resume bullets.

Why this matters

For publishers: informs genre positioning, pricing context, and the quality vs audience trade-off.

For your portfolio: demonstrates end-to-end analytics—feature engineering, clear metrics, interpretable visuals, and a concise story aligned with Xbox’s focus on publisher success and data-driven insights.