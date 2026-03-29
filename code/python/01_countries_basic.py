## 01_countries_basic.py
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
# プロジェクトルートを明示的に固定
PROJECT_ROOT = Path(r"E:\Analytics\My-Statistics-for-Data-Analysis")
DATA_PATH = PROJECT_ROOT / "data" / "01_countries_basic.csv"
df = pd.read_csv(DATA_PATH)


# データの確認
print(df.head())
print(df.info())
print(df.describe())

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
# 相関係数(Population × GDP)
# -----------------------
corr_pop_gdp = df["population_million"].corr(df["gdp_billion_usd"])
print("Correlation (Population × GDP):", round(corr_pop_gdp, 3))

# -----------------------
# 相関係数(Area × Population)
# -----------------------
corr_area_pop = df["area_thousand_km2"].corr(df["population_million"])
print("Correlation (Area × Population):", round(corr_area_pop, 3))  



# -----------------------
# 地域ごとの平均比較
# -----------------------
region_mean = (
    df.groupby("region")[["population_million", "gdp_billion_usd", "average_age"]]
    .mean()
)

print("\nAverage by Region")
print(region_mean)


# 地域ごとの平均を棒グラフで可視化
region_mean.plot(kind="bar", figsize=(10, 6))
plt.title("Average Population, GDP, and Age by Region")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.legend(["Population (million)", "GDP (billion USD)", "Average Age"])
plt.tight_layout()
plt.show()