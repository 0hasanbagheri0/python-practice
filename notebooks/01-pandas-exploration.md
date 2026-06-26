# 📊 Pandas Exploration - 10 Days Learning Journey

**Author:** Hasan Bagheri  
**Start Date:** June 17, 2026  
**Goal:** Practical exploration of Pandas library for data analysis

---

## 📚 About This Notebook

This document contains all the code and analysis from my 10-day Pandas learning journey. Each day covers a specific topic with practical examples using real datasets.

---

## 📦 1. Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)

print(f"✅ Pandas version: {pd.__version__}")
print(f"✅ NumPy version: {np.__version__}")
print("\n🎯 All libraries imported successfully!")
```

---

## 🎬 DAY 1: Pandas Basics (June 17, 2026)

```python
# Load movies dataset
df_movies = pd.read_csv('../data/movies.csv')
print(f"Shape: {df_movies.shape}")
df_movies.head()
```

```python
df_movies.info()
```

```python
df_movies['score'].describe()
```

```python
missing = df_movies.isnull().sum()
missing[missing > 0]
```

**📝 Summary:** Loaded 7,666 movies with 15 columns. Found missing values in 'vote', 'writer', 'star', 'score', 'rating'.

---

## 🎬 DAY 2: Filtering Data (June 18, 2026)

```python
# Movies with score >= 9
high_score = df_movies[df_movies['score'] >= 9]
print(f"Movies with score >= 9: {len(high_score)}")
high_score[['name', 'score', 'year']].head()
```

```python
# Movies with score between 7 and 8
cond1 = df_movies['score'] >= 7
cond2 = df_movies['score'] <= 8
mid_score = df_movies[cond1 & cond2]
print(f"Movies with score 7-8: {len(mid_score)}")
mid_score[['name', 'score', 'year']].head()
```

```python
# High score movies after 2015
recent_high = df_movies[(df_movies['score'] >= 8.5) & (df_movies['year'] >= 2015)]
print(f"High score movies after 2015: {len(recent_high)}")
recent_high[['name', 'score', 'year']].head()
```

---

## 🎬 DAY 3-4: Series (June 19-20, 2026)

```python
# Creating Series from different objects
s1 = pd.Series([1, 3, 5, 7, 9], name="Odd Numbers")
s2 = pd.Series({'Iran': 'Tehran', 'Germany': 'Berlin', 'France': 'Paris'})
s3 = pd.Series(['A', 'B', 'C', 'D'], index=['w', 'x', 'y', 'z'])

print("s1:\n", s1, "\n")
print("s2:\n", s2, "\n")
print("s3:\n", s3)
```

```python
# Series statistics
scores_series = df_movies['score']
print(f"Count: {scores_series.count()}")
print(f"Mean: {scores_series.mean():.2f}")
print(f"Median: {scores_series.median():.2f}")
print(f"Min: {scores_series.min():.2f}")
print(f"Max: {scores_series.max():.2f}")
```

---

## 🎬 DAY 5-6: Important Series Features (June 21-22, 2026)

```python
# Series with missing values
s_test = pd.Series([1, 3, 5, None, 9, 11, 13])
print(f"Count: {s_test.count()}")
print(f"Sum: {s_test.sum()}")
print(f"Product: {s_test.prod()}")
print(f"Cumulative Sum:\n{s_test.cumsum()}")
```

```python
# describe() method
df_movies['score'].describe()
```

```python
# Mode and sampling
s_mode = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"Mode: {s_mode.mode().tolist()}")
print(f"Sample: {df_movies['score'].sample(5).tolist()}")
print(f"Top 3: {df_movies['score'].nlargest(3).tolist()}")
```

---

## 🎬 DAY 7: Arithmetic Operations (June 23, 2026)

```python
# Basic arithmetic
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([1, 2, 3, 4, 5])

print(f"s1 + s2: {(s1 + s2).tolist()}")
print(f"s1 - s2: {(s1 - s2).tolist()}")
print(f"s1 * s2: {(s1 * s2).tolist()}")
print(f"s1 / s2: {(s1 / s2).tolist()}")
print(f"s1 ** 2: {(s1 ** 2).tolist()}")
```

```python
# Using methods
print(f"s1.add(10): {s1.add(10).tolist()}")
print(f"s1.mul(2): {s1.mul(2).tolist()}")
```

```python
# Different lengths
s3 = pd.Series([1, 2, 3])
s4 = pd.Series([10, 20, 30, 40, 50])
print(f"s3 + s4 (different lengths): {(s3 + s4).tolist()}")
```

---

## 🎬 DAY 8: Converting Series (June 24, 2026)

```python
# Create Series with custom index
s_countries = pd.Series(
    data=['Tehran', 'Ankara', 'Baku', 'Berlin'],
    index=['Iran', 'Turkey', 'Azerbaijan', 'Germany']
)

print(f"To List: {s_countries.tolist()}")
print(f"To Dict: {s_countries.to_dict()}")
print(f"To Tuple: {tuple(s_countries)}")
print(f"To NumPy: {s_countries.to_numpy()}")
```

```python
# Membership testing
print(f"'Tehran' in values: {'Tehran' in s_countries.values}")
print(f"'Iran' in index: {'Iran' in s_countries.index}")
```

---

## 🎬 DAY 9: Reading from File (June 25, 2026)

```python
# Load Bitcoin data
btc_df = pd.read_csv(
    '../data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date']
)
print(f"Shape: {btc_df.shape}")
btc_df.head()
```

```python
# Close price as Series
close_series = btc_df['Close']
print(f"Type: {type(close_series)}")
close_series.describe()
```

```python
# Using squeeze()
close_squeezed = pd.read_csv(
    '../data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date'],
    usecols=['Date', 'Close']
).squeeze()

print(f"Type after squeeze: {type(close_squeezed)}")
close_squeezed.head()
```

---

## 🎬 DAY 10: Sorting Series (June 26, 2026)

```python
# Load employee data
emp_series = pd.read_csv(
    '../data/employees.csv',
    index_col='First Name',
    usecols=['First Name', 'Salary']
).squeeze()

emp_series.head(10)
```

```python
# Sort by index
emp_series.sort_index().head(10)
```

```python
# Sort by values
emp_series.sort_values().head(10)
```

```python
# Top and bottom values
print("Top 5 highest salaries:")
print(emp_series.nlargest(5))
print("\nTop 5 lowest salaries:")
print(emp_series.nsmallest(5))
```

---

## 📊 BONUS: Data Visualization

```python
plt.style.use('seaborn-v0_8-darkgrid')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Movie scores distribution
axes[0, 0].hist(df_movies['score'].dropna(), bins=30, edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Movie Scores Distribution')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].axvline(df_movies['score'].mean(), color='red', linestyle='--', label='Mean')
axes[0, 0].legend()

# 2. Average score by year
years_avg = df_movies.groupby('year')['score'].mean().dropna()
axes[0, 1].plot(years_avg.index, years_avg.values, marker='o')
axes[0, 1].set_title('Average Score by Year')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('Average Score')
axes[0, 1].grid(True, alpha=0.3)

# 3. Bitcoin price
axes[1, 0].plot(close_series.index, close_series.values, color='orange', linewidth=1)
axes[1, 0].set_title('Bitcoin Price (USD)')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Price')
axes[1, 0].grid(True, alpha=0.3)

# 4. Employee salaries
emp_sorted = emp_series.dropna().sort_values()
axes[1, 1].barh(emp_sorted.index[:20], emp_sorted.values[:20])
axes[1, 1].set_title('Top 20 Employee Salaries')
axes[1, 1].set_xlabel('Salary')
axes[1, 1].set_ylabel('Employee')

plt.tight_layout()
plt.show()
```

---

## 🎯 Final Summary

### What I Learned in 10 Days:

| Day | Topic | Key Skills |
|-----|-------|------------|
| 1 | Pandas Basics | Series, DataFrame, Loading CSV |
| 2 | Filtering | Single & Multiple Conditions |
| 3-4 | Series | Creation, Indexing, Data Types |
| 5-6 | Features | Stats, describe(), sample(), mode() |
| 7 | Arithmetic | add(), sub(), mul(), div(), pow() |
| 8 | Converting | List, Dict, Tuple, NumPy Array |
| 9 | Reading | read_csv(), usecols, squeeze() |
| 10 | Sorting | sort_index(), sort_values(), nlargest() |

### 📊 Total Achievements:
- ✅ **10 Days** of consistent practice
- ✅ **3 Datasets** analyzed (Movies, Bitcoin, Employees)
- ✅ **40+ Concepts** learned
- ✅ **Average Score**: 8.6/10

---

**🎉 Congratulations on completing the 10-day Pandas journey!**

**Created by:** Hasan Bagheri  
**Date:** June 26, 2026  
**GitHub:** [0hasanbagheri0](https://github.com/0hasanbagheri0)
