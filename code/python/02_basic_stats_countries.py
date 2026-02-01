## 02_basic_stats_countries.py
# Basic statistics for countries dataset

from config import DATA_DIR
import pandas as pd
import matplotlib.pyplot as plt

# ===== Path (fixed) =====
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

# Mean / Median / Var / Std
stats = pd.DataFrame({
    "mean": df[numeric_cols].mean(),
    "median": df[numeric_cols].median(),
    "var": df[numeric_cols].var(ddof=1),   # sample variance
    "std": df[numeric_cols].std(ddof=1),   # sample std
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
for col in numeric_cols:
    plt.figure()
    # region order to keep stable
    regions = sorted(df["region"].unique())
    data = [df.loc[df["region"] == r, col].dropna() for r in regions]
    plt.boxplot(data, labels=regions)
    plt.title(f"Boxplot by region: {col}")
    plt.xlabel("Region")
    plt.ylabel(col)
    plt.show()
