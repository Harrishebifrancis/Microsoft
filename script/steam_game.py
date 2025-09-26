import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "steam_games.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

# --- load
df = pd.read_csv(DATA, low_memory=False)

# --- tidy columns we care about (adjust names if your CSV differs)
keep = ["name", "release_date", "price", "genres", "positive_ratings", "negative_ratings", "owners"]
df = df[[c for c in keep if c in df.columns]].copy()

# drop rows with missing key fields
df = df.dropna(subset=["price", "positive_ratings", "negative_ratings", "genres"])

# create helpers
df["review_total"] = df["positive_ratings"] + df["negative_ratings"]
df = df[df["review_total"] > 0]
df["review_score"] = df["positive_ratings"] / df["review_total"]
df["main_genre"] = df["genres"].astype(str).str.split(";").str[0].str.strip()

print("\n=== SHAPE ===")
print(df.shape)
print("\n=== COLUMNS ===")
print(df.columns.tolist())
print("\n=== SAMPLE ===")
print(df.head(10).to_string(index=False))
print("\n=== BASIC STATS ===")
print(df[["price", "review_score", "review_total"]].describe().round(2))

# --- price vs review score plot
plt.figure(figsize=(8,6))
plt.scatter(df["price"], df["review_score"], alpha=0.2)
plt.xlabel("Price (USD)")
plt.ylabel("Review Score (pos/(pos+neg))")
plt.title("Price vs Review Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / "price_vs_review_score.png", dpi=150)

# --- top genres by average review score
genre_avg = df.groupby("main_genre")["review_score"].mean().sort_values(ascending=False).head(15)
plt.figure(figsize=(10,6))
genre_avg.plot(kind="bar")
plt.title("Top Genres by Avg Review Score")
plt.ylabel("Avg Review Score")
plt.tight_layout()
plt.savefig(OUT / "top_genres_avg_review.png", dpi=150)

print(f"\nSaved charts to: {OUT.resolve()}")
