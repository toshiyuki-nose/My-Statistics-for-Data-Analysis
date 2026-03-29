# 02_basic_stats_countries.py
# Basic statistics for countries dataset

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
# プロジェクトルートを明示的に固定
PROJECT_ROOT = Path(r"E:\Analytics\My-Statistics-for-Data-Analysis")
DATA_PATH = PROJECT_ROOT / "data" / "02_countries_basic_stats.csv"
df = pd.read_csv(DATA_PATH)


# データの確認
print(df.head())
print(df.info())
print(df.describe())



# 基本統計量の計算
# 平均（mean）
mean_values = df.mean(numeric_only=True)
# 中央値（median）
median_values = df.median(numeric_only=True)
# 四分位数（quartiles）
quartiles = df.quantile([0.25, 0.5, 0.75], numeric_only=True)

# ばらつきの指標
# 分散（variance）
variance_values = df.var(numeric_only=True, ddof=1)  # 標本分散
# 標準偏差（standard deviation）
std_values = df.std(numeric_only=True, ddof=1)  # 標本標準偏差
# 最小値（min）
min_values = df.min(numeric_only=True)
# 最大値（max）
max_values = df.max(numeric_only=True)



# 可視化
# ヒストグラムの作成
df["population_million"].hist(bins=10, edgecolor="black")
plt.title("Population Distribution")
plt.xlabel("Population (million)")
plt.ylabel("Frequency")
plt.show()


# 箱ひげ図の作成
df.boxplot(column="gdp_per_capita_usd")
plt.title("GDP Distribution")
plt.ylabel("GDP (per capita, USD)")
plt.show()
