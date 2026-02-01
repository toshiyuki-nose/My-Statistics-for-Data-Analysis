## 02_basic_stats_countries.R

# ===== Path (fixed) =====
project_root <- "E:/Analytics/My-Statistics-for-Data-Analysis"
data_path <- file.path(project_root, "data", "02_countries_basic_stats.csv")

# ===== Load =====
df <- read.csv(data_path)

# ===== Basic check =====
cat("== Head ==\n")
print(head(df))
cat("\n")

cat("== Structure ==\n")
str(df)
cat("\n")

# ===== Basic statistics (overall) =====
num_cols <- c("population_million", "gdp_per_capita_usd", "life_expectancy", "average_age")

cat("== Summary (overall) ==\n")
print(summary(df[num_cols]))
cat("\n")

basic_stats <- data.frame(
  mean   = sapply(df[num_cols], mean),
  median = sapply(df[num_cols], median),
  var    = sapply(df[num_cols], var),
  sd     = sapply(df[num_cols], sd),
  min    = sapply(df[num_cols], min),
  max    = sapply(df[num_cols], max)
)
cat("== Mean/Median/Var/SD/Min/Max ==\n")
print(basic_stats)
cat("\n")

# ===== By region =====
by_region_mean <- aggregate(df[num_cols], by = list(region = df$region), FUN = mean)
by_region_sd   <- aggregate(df[num_cols], by = list(region = df$region), FUN = sd)

cat("== By region (mean) ==\n")
print(by_region_mean)
cat("\n")

cat("== By region (sd) ==\n")
print(by_region_sd)
cat("\n")

# ===== Plots: Histogram =====
for (col in num_cols) {
  hist(
    df[[col]],
    main = paste("Histogram:", col),
    xlab = col
  )
}

# ===== Plots: Boxplot by region =====
for (col in num_cols) {
  boxplot(
    df[[col]] ~ df$region,
    main = paste("Boxplot by region:", col),
    xlab = "Region",
    ylab = col
  )
}
