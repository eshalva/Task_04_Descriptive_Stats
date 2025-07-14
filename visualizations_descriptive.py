import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (change filename as needed)
df = pd.read_csv("facebook_ads_cleaned.csv")

# Sample 10000 rows if dataset is too large
if len(df) > 10000:
    df = df.sample(10000, random_state=42)

# Clean column names
df.columns = df.columns.str.strip()

# Auto-detect numeric and categorical columns
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
categorical_cols = df.select_dtypes(include=["object", "category", "bool"]).columns

# Create histograms for numeric variables
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{col}_histogram.png")
    plt.close()

# Create boxplots for numeric columns
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.tight_layout()
    plt.savefig(f"{col}_boxplot.png")
    plt.close()

# Create bar plots for top 10 categories in categorical columns
for col in categorical_cols:
    top_values = df[col].value_counts().nlargest(10)
    if len(top_values) > 1:
        plt.figure(figsize=(8, 4))
        sns.barplot(x=top_values.values, y=top_values.index)
        plt.title(f"Top 10 {col} Values")
        plt.xlabel("Count")
        plt.ylabel(col)
        plt.tight_layout()
        plt.savefig(f"{col}_barplot.png")
        plt.close()

print("✅ Visualizations saved as PNGs.")
