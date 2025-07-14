import polars as pl

# File paths
facebook_file = "facebook_posts_cleaned.csv"
twitter_file = "twitter_posts_cleaned.csv"
ads_file = "facebook_ads_cleaned.csv"

# Function to print stats for a dataset
def analyze_file(path, label):
    print(f"\n=== {label.upper()} ===")
    df = pl.read_csv(path, infer_schema_length=10000)

    # Describe (numeric summary only)
    print("\n--- Describe ---")
    print(df.describe())

    # Unique values
    print("\n--- nunique (number of unique values) ---")
    for col in df.columns:
        print(f"{col}: {df.select(pl.col(col).n_unique()).item()}")

    # Most frequent value per column
    print("\n--- Most Frequent Values (value_counts) ---")
    for col in df.columns:
        try:
            val_counts = df.select(pl.col(col).value_counts().sort("counts", descending=True))
            top_value = val_counts[0, 0]
            top_count = val_counts[0, 1]
            print(f"{col}: {top_value} ({top_count} times)")
        except Exception:
            print(f"{col}: Skipped (non-categorical or high-cardinality)")

# Analyze all 3 files
analyze_file(facebook_file, "Facebook Posts")
analyze_file(twitter_file, "Twitter Posts")
analyze_file(ads_file, "Facebook Ads")
