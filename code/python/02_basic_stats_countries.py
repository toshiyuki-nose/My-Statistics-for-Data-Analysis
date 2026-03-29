# 02_basic_stats_countries.py
# Basic statistics for countries dataset

<<<<<<< HEAD
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
=======
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
>>>>>>> c0369994ec93c3e5e9d093d1e62df06da7c291a1



# 基本統計量の計算
# 平均（mean）
mean_values = df.mean(numeric_only=True)
# 中央値（median）
median_values = df.median(numeric_only=True)
# 四分位数（quartiles）
quartiles = df.quantile([0.25, 0.5, 0.75], numeric_only=True)

<<<<<<< HEAD
# ばらつきの指標
# 分散（variance）
variance_values = df.var(numeric_only=True, ddof=1)  # 標本分散
# 標準偏差（standard deviation）
std_values = df.std(numeric_only=True, ddof=1)  # 標本標準偏差
# 最小値（min）
min_values = df.min(numeric_only=True)
# 最大値（max）
max_values = df.max(numeric_only=True)
=======
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
>>>>>>> c0369994ec93c3e5e9d093d1e62df06da7c291a1



<<<<<<< HEAD
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
=======
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
>>>>>>> c0369994ec93c3e5e9d093d1e62df06da7c291a1
