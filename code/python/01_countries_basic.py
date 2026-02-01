from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "01_countries_basic.csv"

df = pd.read_csv(DATA_PATH)


# -----------------------
# 散布図① 人口 × GDP
# -----------------------
plt.figure()
plt.scatter(df["population_million"], df["gdp_billion_usd"])
plt.xlabel("Population (million)")
plt.ylabel("GDP (billion USD)")
plt.title("Population vs GDP")
plt.show()

# -----------------------
# 散布図② 面積 × 人口
# -----------------------
plt.figure()
plt.scatter(df["area_thousand_km2"], df["population_million"])
plt.xlabel("Area (thousand km2)")
plt.ylabel("Population (million)")
plt.title("Area vs Population")
plt.show()

# -----------------------
# 相関係数（1行）
# -----------------------
corr_pop_gdp = df["population_million"].corr(df["gdp_billion_usd"])
print("Correlation (Population × GDP):", round(corr_pop_gdp, 3))

# -----------------------
# 地域ごとの平均比較
# -----------------------
region_mean = (
    df.groupby("region")[["population_million", "gdp_billion_usd", "average_age"]]
    .mean()
)

print("\nAverage by Region")
print(region_mean)
