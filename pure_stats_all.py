import csv
from collections import defaultdict, Counter
from math import sqrt

def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

def compute_stats(values):
    stats = {}
    values = [v for v in values if v != '']
    numeric_values = [float(v) for v in values if is_float(v)]
    
    stats['count'] = len(values)
    stats['unique'] = len(set(values))
    stats['most_frequent'] = Counter(values).most_common(1)[0][0] if values else None

    if numeric_values:
        stats['mean'] = sum(numeric_values) / len(numeric_values)
        stats['min'] = min(numeric_values)
        stats['max'] = max(numeric_values)
        stats['std'] = sqrt(sum((x - stats['mean'])**2 for x in numeric_values) / len(numeric_values))
    return stats

def summarize_dataset(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        columns = defaultdict(list)
        for row in reader:
            for col, val in row.items():
                columns[col].append(val)

    print(f"=== Summary for: {file_path} ===")
    for col, values in columns.items():
        stats = compute_stats(values)
        print(f"\nColumn: {col}")
        for k, v in stats.items():
            print(f"  {k}: {v}")
    print("\n")

def aggregate_by(file_path, group_cols):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        groups = defaultdict(lambda: defaultdict(list))
        
        for row in reader:
            group_key = tuple(row[col] for col in group_cols)
            for col, val in row.items():
                groups[group_key][col].append(val)

    print(f"=== Aggregated by {group_cols} ===")
    for group_key, cols in list(groups.items())[:5]:  # limit to first 5 groups
        print(f"\nGroup: {group_key}")
        for col, values in cols.items():
            stats = compute_stats(values)
            print(f"  Column: {col}")
            for k, v in stats.items():
                print(f"    {k}: {v}")

# Example Usage
file_paths = [
    "facebook_posts_cleaned.csv",
    "facebook_ads_cleaned.csv",
    "twitter_posts_cleaned.csv"
]

# Summarize all datasets
for path in file_paths:
    summarize_dataset(path)

# Aggregation examples
aggregate_by("facebook_ads_cleaned.csv", ["page_id"])
aggregate_by("facebook_ads_cleaned.csv", ["page_id", "ad_id"])
