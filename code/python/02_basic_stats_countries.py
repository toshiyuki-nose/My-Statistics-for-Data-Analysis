# 02_basic_stats_countries.py
# Basic statistics for countries dataset

import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# ===== Project root (fixed) =====
PROJECT_ROOT = Path(r"E:\Analytics\My-Statistics-for-Data-Analysis")

# config.py を import できるように、プロジェクトルートを sys.path に追加
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config import DATA_DIR  # noqa: E402

# ===== Load =====
df = pd.read_csv(DATA_DIR / "02_countries_basic_stats.csv")

# ===== Basic check =====
print("== Head ==")
print(df.head(), "\n")

print("== dtypes ==")
print(df.dtypes, "\n")

# ===== Basic statistics (overall) =====
numeric_cols = ["population_million", "gdp_per_capita_usd", "life_expectancy", "average_age"]

print("== Basic statistics (describe) ==")
print(df[numeric_cols].describe(), "\n")

stats = pd.DataFrame({
    "mean": df[numeric_cols].mean(),
    "median": df[numeric_cols].median(),
    "var": df[numeric_cols].var(ddof=1),
    "std": df[numeric_cols].std(ddof=1),
    "min": df[numeric_cols].min(),
    "max": df[numeric_cols].max()
})
print("== Mean/Median/Var/Std/Min/Max ==")
print(stats, "\n")

# ===== By region =====
region_stats = df.groupby("region")[numeric_cols].agg(["mean", "median", "var", "std", "min", "max"])
print("== By region (mean/median/var/std/min/max) ==")
print(region_stats, "\n")

# ===== Plots: Histogram =====
for col in numeric_cols:
    plt.figure()
    plt.hist(df[col].dropna())
    plt.title(f"Histogram: {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()

# ===== Plots: Boxplot by region =====
regions = sorted(df["region"].unique())
for col in numeric_cols:
    plt.figure()
    data = [df.loc[df["region"] == r, col].dropna() for r in regions]
    plt.boxplot(data, labels=regions)
    plt.title(f"Boxplot by region: {col}")
    plt.xlabel("Region")
    plt.ylabel(col)
    plt.show()
