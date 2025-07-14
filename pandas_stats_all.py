import pandas as pd

# File paths
files = {
    "Facebook Posts": "facebook_posts_cleaned.csv",
    "Twitter Posts": "twitter_posts_cleaned.csv",
    "Facebook Ads": "facebook_ads_cleaned.csv"
}

def analyze_dataset(file_path, label):
    print(f"\n=== {label.upper()} ===")

    # Load data
    df = pd.read_csv(file_path)

    # Describe
    print("\n--- describe() ---")
    print(df.describe(include='all'))

    # Unique values
    print("\n--- nunique() ---")
    print(df.nunique())

    # Most frequent values
    print("\n--- value_counts() ---")
    for col in df.columns:
        try:
            vc = df[col].value_counts().head(1)
            print(f"{col}: {vc.index[0]} ({vc.values[0]} times)")
        except Exception as e:
            print(f"{col}: Skipped (reason: {str(e)})")

# Run analysis for each dataset
for name, path in files.items():
    analyze_dataset(path, name)
