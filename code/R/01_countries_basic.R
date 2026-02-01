## 01_countries_basic.R


# データ読み込み
df <- read.csv("data/01_countries_basic.csv")

# -----------------------
# 散布図① 人口 × GDP
# -----------------------
plot(
  df$population_million,
  df$gdp_billion_usd,
  xlab = "Population (million)",
  ylab = "GDP (billion USD)",
  main = "Population vs GDP"
)

# -----------------------
# 散布図② 面積 × 人口
# -----------------------
plot(
  df$area_thousand_km2,
  df$population_million,
  xlab = "Area (thousand km2)",
  ylab = "Population (million)",
  main = "Area vs Population"
)

# -----------------------
# 相関係数（1行）
# -----------------------
cor_pop_gdp <- cor(df$population_million, df$gdp_billion_usd)
print(paste("Correlation (Population × GDP):", round(cor_pop_gdp, 3)))

# -----------------------
# 地域ごとの平均比較
# -----------------------
region_mean <- aggregate(
  cbind(population_million, gdp_billion_usd, average_age) ~ region,
  data = df,
  FUN = mean
)

print("Average by Region")
print(region_mean)

