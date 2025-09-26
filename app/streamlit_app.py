import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "steam_games.csv"

st.set_page_config(page_title="Steam Marketplace Analytics", layout="wide")
st.title("🎮 Steam Marketplace Analytics")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA, low_memory=False)
    needed = ["name","release_date","price","genres","positive_ratings","negative_ratings","owners"]
    df = df[[c for c in needed if c in df.columns]].copy()
    df = df.dropna(subset=["price","positive_ratings","negative_ratings","genres"])
    df["review_total"] = df["positive_ratings"] + df["negative_ratings"]
    df = df[df["review_total"] > 0]
    df["review_score"] = df["positive_ratings"] / df["review_total"]
    df["main_genre"] = df["genres"].astype(str).str.split(";").str[0].str.strip()
    # 👇 Parse release date once here
    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    return df

df = load_data()

# sidebar filters
genres = ["All"] + sorted(df["main_genre"].dropna().unique().tolist())
pick_genre = st.sidebar.selectbox("Filter by genre", genres, index=0)
max_price = float(np.nanmax(df["price"]))
price_cap = st.sidebar.slider("Max price", 0.0, max(5.0, max_price), min(30.0, max_price), step=1.0)

sub = df[df["price"] <= price_cap].copy()
if pick_genre != "All":
    sub = sub[sub["main_genre"] == pick_genre]
st.subheader("Sample Games")

# --- Sidebar controls for the sample table
# Guard: owners column can be ranges like "1,000,000 .. 2,000,000".
# We'll approximate by taking the LOWER bound in the range.
if "owners" in sub.columns:
    owners_low = sub["owners"].astype(str).str.extract(r"(\d[\d,]*)")[0]
    owners_num = pd.to_numeric(owners_low.str.replace(",", ""), errors="coerce")
    sub = sub.assign(owners_num=owners_num)
else:
    sub = sub.assign(owners_num=np.nan)

# Optional: let user require a minimum amount of review volume
min_reviews = st.sidebar.slider(
    "Min total reviews", 0, int(sub["review_total"].max()), 100, step=50
)
sub = sub[sub["review_total"] >= min_reviews].copy()

# Sorting options
sort_options = {
    "Review score (quality)": ("review_score", False),   # high → low
    "Total reviews (volume)": ("review_total", False),   # high → low
    "Owners (approx)": ("owners_num", False),            # high → low
    "Price (low to high)": ("price", True),              # low → high
    "Newest first": ("release_date", False),             # recent → old
}
sort_pick = st.sidebar.selectbox("Sort sample by", list(sort_options.keys()), index=0)
sort_col, asc = sort_options[sort_pick]

# How many rows to show
top_n = st.sidebar.slider("How many games to show", 10, 200, 50, step=10)

# Final sort (tie-break by review volume)
# If sorting by a column that might be missing, fall back gracefully
if sort_col not in sub.columns:
    st.warning(f"Sort column '{sort_col}' not found; defaulting to review_score.")
    sort_col, asc = "review_score", False

sub_sorted = sub.sort_values([sort_col, "review_total"], ascending=[asc, False]).head(top_n)

# Columns to display (only show what exists)
cols_to_show = [c for c in ["name","main_genre","price","review_score","review_total","owners","release_date"] if c in sub_sorted.columns]
st.dataframe(sub_sorted[cols_to_show])


# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Games", f"{len(sub):,}")
c2.metric("Avg Price", f"${sub['price'].mean():.2f}")
c3.metric("Avg Review Score", f"{sub['review_score'].mean():.2f}")
if "owners" in sub.columns:
    # owners might be a string range in some datasets; attempt to coerce
    owners_num = pd.to_numeric(sub["owners"].astype(str).str.replace(r"\D", "", regex=True), errors="coerce")
    c4.metric("Median Owners (approx)", f"{np.nanmedian(owners_num):,.0f}")
else:
    c4.metric("Median Owners", "N/A")

# charts
st.subheader("Price vs Review Score")
st.caption("Use sidebar to filter by genre and price cap.")
st.scatter_chart(sub[["price","review_score"]])

st.subheader("Top Genres by Avg Review Score (current filter)")
top = sub.groupby("main_genre")["review_score"].mean().sort_values(ascending=False).head(15)
st.bar_chart(top)

st.subheader("Sample Games")
st.dataframe(sub.sort_values("review_score", ascending=False).head(50)[["name","main_genre","price","review_score","review_total"]])
