# 📊 Research Task 4 – Descriptive Statistics Analysis

This project provides descriptive statistical insights from political datasets using three different Python approaches:

- ✅ **Pure Python (No third-party libraries)**
- ✅ **Pandas**
- ✅ **Polars**
- ✅ **Data Visualizations**

---

## 📂 Project Structure

```
RESEARCH TASK 4/
├── .venv/                          # Virtual environment (excluded from version control)
├── .gitignore                     # Ignores .venv and large raw files
├── facebook_ads_cleaned.csv      # Cleaned Facebook ad data
├── facebook_posts_cleaned.csv    # Cleaned Facebook posts
├── twitter_posts_cleaned.csv     # Cleaned Twitter posts
├── pure_stats_all.py             # Pure Python analysis
├── pandas_stats_all.py           # Pandas-based analysis
├── polars_stats_all.py           # Polars-based analysis
├── visualizations_descriptive.py # Visual summaries (matplotlib/seaborn)
```

---

## 🚀 How to Run

### 1. Set up your virtual environment (optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 2. Install dependencies
```bash
pip install pandas polars matplotlib seaborn
```

### 3. Run analysis scripts
```bash
python pure_stats_all.py
python pandas_stats_all.py
python polars_stats_all.py
```

### 4. Run visualizations
```bash
python visualizations_descriptive.py
```

---

## 📈 Features

Each script performs:

- `DataFrame.describe()` equivalent
- `.value_counts()` for key categorical features
- `.nunique()` for uniqueness insights
- Aggregations by `page_id`, `ad_id`, `age_group`, `gender`
- Visualizations: histograms, bar plots, boxplots

---

## 🧠 Insights Summary

### Facebook Ads
- **Most common age group:** 45–54  
- **Most targeted platform combination:** Facebook + Instagram  
- **Zero spend** on ~30% of ads  
- **Message types:** High frequency of advocacy and CTA-related ads

### Facebook Posts
- **Post duplication** across days suggests reposting strategy  
- **High frequency** from certain political candidates' pages

### Twitter Posts
- **Lower repost rate** than Facebook  
- **More diverse content** per user  
- **Peak activity** close to debate/election events

---

## 📊 Visualizations

File: `visualizations_descriptive.py`

Plots included:
- Histogram of `impressions` and `spend`
- Bar plot of ad counts by `age_group` and `gender`
- Boxplot of `estimated_audience_size` by `platforms`

Plots saved as `.png` files in the same directory for use in reports or presentations.

---

## 📌 Tools Used

- Python 3.11+
- `pandas`, `polars`
- `matplotlib`, `seaborn`

---

## 📅 Submission Checklist

- ✅ All `.py` scripts completed
- ✅ README.md with summary and instructions
- ✅ Visualizations generated

---

## 👩‍💻 Author

**Esha Alva**  
_M.S. Information Systems – Syracuse University_  
