# 🐍 Python Practice

> A collection of daily Python exercises, small scripts, and coding challenges to sharpen my programming skills  
> مجموعه‌ای از تمرین‌های روزانه پایتون، اسکریپت‌های کوچک و چالش‌های کدنویسی برای تقویت مهارت‌های برنامه‌نویسی

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Days](https://img.shields.io/badge/Days-10-brightgreen.svg)](https://github.com/0hasanbagheri0/python-practice)
[![Progress](https://img.shields.io/badge/Progress-10%25-yellow.svg)](https://github.com/0hasanbagheri0/python-practice)

---

## 📖 درباره این مخزن (About This Repository)

**فارسی:**  
این مخزن شامل تمرین‌های روزانه‌ی من برای تقویت مهارت‌های برنامه‌نویسی پایتون است. هدف از ایجاد این مجموعه، تبدیل مفاهیم تئوری به کدهای عملی و ایجاد یک عادت روزانه برای کدنویسی است. من در این مسیر بر روی **تحلیل داده** با استفاده از کتابخانه‌های **Pandas** و **NumPy** تمرکز دارم و هر روز یک مبحث جدید را یاد گرفته و تمرین می‌کنم.

**English:**  
This repository contains my daily exercises to strengthen my Python programming skills. The goal is to turn theoretical concepts into practical code and build a daily coding habit. I focus on **Data Analysis** using **Pandas** and **NumPy** libraries, learning and practicing a new topic each day.

**اهداف اصلی (Main Objectives):**
- تمرین مستمر مفاهیم پایه و پیشرفته پایتون / Continuous practice of basic and advanced Python concepts
- تسلط بر کتابخانه‌های **Pandas** و **NumPy** برای تحلیل داده / Mastering **Pandas** and **NumPy** for data analysis
- ایجاد یک مرجع شخصی از کدهای مفید و کاربردی / Building a personal reference of useful code snippets
- آماده‌سازی برای پروژه‌های بزرگ‌تر تحلیل داده و یادگیری ماشین / Preparing for larger data analysis and machine learning projects

---

## 🗂️ ساختار مخزن (Repository Structure)

```
Python-Practice/
│
├── README.md                          # این فایل / This file
├── LICENSE                            # مجوز پروژه / Project license
├── requirements.txt                   # وابستگی‌های پروژه / Project dependencies
│
├── basics/                            # تمرین‌های پایه / Basic exercises
│   ├── 01-variables.py                # متغیرها و انواع داده / Variables and data types
│   ├── 02-conditions.py               # ساختارهای شرطی / Conditional statements
│   ├── 03-loops.py                    # حلقه‌ها / Loops
│   ├── 04-functions.py                # توابع / Functions
│   └── 05-data-structures.py          # ساختارهای داده / Data structures
│
├── pandas-journal/                    # 📚 مجله یادگیری Pandas / Pandas Learning Journal
│   ├── day-01-pandas-basics.md        # روز ۱: اصول Pandas / Day 1: Pandas Basics
│   ├── day-02-filtering-data.md       # روز ۲: فیلتر کردن داده‌ها / Day 2: Filtering Data
│   ├── day-03-series-intro.md         # روز ۳: مقدمه‌ای بر سری‌ها / Day 3: Series Intro
│   ├── day-04-making-series.md        # روز ۴: ساخت سری از اشیاء / Day 4: Making Series
│   ├── day-05-series-features.md      # روز ۵: ویژگی‌های سری / Day 5: Series Features
│   ├── day-06-important-features.md   # روز ۶: ویژگی‌های مهم سری / Day 6: Important Features
│   ├── day-07-arithmetic-ops.md       # روز ۷: عملیات‌های حسابی / Day 7: Arithmetic Ops
│   ├── day-08-converting-series.md    # روز ۸: تبدیل سری / Day 8: Converting Series
│   ├── day-09-reading-from-file.md    # روز ۹: خواندن از فایل / Day 9: Reading from File
│   ├── day-10-sorting-series.md       # روز ۱۰: مرتب‌سازی سری‌ها / Day 10: Sorting Series
│   └── README.md                      # راهنمای مجله یادگیری / Learning Journal Guide
│
├── data/                              # دیتاست‌های مورد استفاده / Datasets used
│   ├── movies.csv                     # دیتاست فیلم‌ها / Movies dataset
│   ├── btc-usd.csv                    # داده‌های بیت‌کوین / Bitcoin data
│   └── employees.csv                  # داده‌های کارمندان / Employees data
│
├── notebooks/                         # نوت‌بوک‌های Jupyter / Jupyter Notebooks
│   ├── 01-pandas-exploration.ipynb    # اکتشاف با Pandas / Pandas Exploration
│   └── 02-data-analysis.ipynb         # تحلیل داده / Data Analysis
│
├── intermediate/                      # تمرین‌های متوسط / Intermediate exercises
│   ├── 01-file-handling.py            # کار با فایل‌ها / File handling
│   ├── 02-oop.py                      # برنامه‌نویسی شی‌گرا / OOP
│   ├── 03-error-handling.py           # مدیریت خطا / Error handling
│   ├── 04-comprehensions.py           # کامپرهنشن‌ها / List/dict comprehensions
│   └── 05-lambda-functions.py         # توابع لامبدا / Lambda functions
│
├── algorithms/                        # چالش‌های الگوریتمی / Algorithm challenges
│   ├── sorting/                       # الگوریتم‌های مرتب‌سازی / Sorting algorithms
│   │   ├── bubble_sort.py
│   │   └── quick_sort.py
│   ├── searching/                     # الگوریتم‌های جستجو / Searching algorithms
│   │   ├── binary_search.py
│   │   └── linear_search.py
│   └── recursion/                     # مسائل بازگشتی / Recursive problems
│       ├── factorial.py
│       └── fibonacci.py
│
├── data-structures/                   # پیاده‌سازی ساختارهای داده / Data structures
│   ├── stack.py
│   ├── queue.py
│   └── linked_list.py
│
├── useful-scripts/                    # اسکریپت‌های کاربردی / Useful scripts
│   ├── file_organizer.py              # سازماندهی فایل‌ها / File organizer
│   ├── data_generator.py              # تولید داده‌های ساختگی / Fake data generator
│   └── password_generator.py          # تولید رمز عبور / Password generator
│
└── daily-challenges/                  # چالش‌های روزانه / Daily challenges
    ├── day-01/
    ├── day-02/
    └── ...
```

---

## 📚 منابع تمرین (Practice Resources)

من این تمرین‌ها را از منابع زیر انتخاب می‌کنم:  
*(I select these exercises from the following resources:)*

| منبع (Resource) | توضیحات (Description) |
| :--- | :--- |
| [Pandas Documentation](https://pandas.pydata.org/docs/) | مستندات رسمی Pandas / Official Pandas docs |
| [Kaggle](https://www.kaggle.com/) | دیتاست‌های واقعی برای تمرین / Real datasets for practice |
| [LeetCode](https://leetcode.com/) | سوالات الگوریتمی و مصاحبه / Algorithm & interview questions |
| [HackerRank](https://www.hackerrank.com/) | چالش‌های کدنویسی در سطوح مختلف / Coding challenges |
| [Python.org](https://docs.python.org/3/tutorial/) | مستندات رسمی پایتون / Official Python docs |
| [W3Schools](https://www.w3schools.com/python/) | آموزش و تمرین‌های تعاملی / Tutorials & exercises |

---

## 🚀 نحوه اجرا و استفاده (How to Use)

**مراحل اجرا / Steps to run:**

1. کلون کردن مخزن / Clone the repository:
   ```bash
   git clone https://github.com/0hasanbagheri0/python-practice.git
   cd python-practice
   ```

2. نصب وابستگی‌ها / Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. اجرای اسکریپت مورد نظر / Run the desired script:
   ```bash
   python basics/01-variables.py
   ```

4. مشاهده مجله یادگیری Pandas / View Pandas Learning Journal:
   ```bash
   cd pandas-journal
   # Open any .md file to see daily learnings
   ```

---

## 📈 پیشرفت من (My Progress)

### 📊 آمار کلی / Overall Statistics

| معیار / Metric | مقدار / Value |
| :--- | :--- |
| **روزهای تمرین / Days Practiced** | ۱۰ / ۱۰ |
| **مفاهیم یادگرفته شده / Concepts Learned** | ۴۰+ |
| **تکه‌کدهای نوشته شده / Code Snippets** | ۵۰+ |
| **دیتاست‌های کار شده / Datasets Used** | ۳ (movies, btc-usd, employees) |
| **میانگین امتیاز روزانه / Avg Daily Score** | ۸.۶/۱۰ |
| **ساعت مطالعه / Study Hours** | ~۲۰ ساعت |

---

### 🗓️ مجله یادگیری ۱۰ روزه / 10-Day Learning Journal

| روز (Day) | تاریخ (Date) | موضوع (Topic) | امتیاز (Score) |
| :--- | :--- | :--- | :---: |
| **Day 1** | June 17, 2026 | اصول Pandas / Pandas Basics | ۸/۱۰ |
| **Day 2** | June 18, 2026 | فیلتر کردن داده‌ها / Filtering Data | ۸.۵/۱۰ |
| **Day 3** | June 19, 2026 | مقدمه‌ای بر سری‌ها / Series Intro | ۸.۵/۱۰ |
| **Day 4** | June 20, 2026 | ساخت سری از اشیاء / Making Series | ۸/۱۰ |
| **Day 5** | June 21, 2026 | ویژگی‌های سری / Series Features | ۸/۱۰ |
| **Day 6** | June 22, 2026 | ویژگی‌های مهم سری / Important Features | ۹/۱۰ |
| **Day 7** | June 23, 2026 | عملیات‌های حسابی / Arithmetic Operations | ۹/۱۰ |
| **Day 8** | June 24, 2026 | تبدیل سری / Converting Series | ۸.۵/۱۰ |
| **Day 9** | June 25, 2026 | خواندن از فایل / Reading from File | ۸.۵/۱۰ |
| **Day 10** | June 26, 2026 | مرتب‌سازی سری‌ها / Sorting Series | ۸.۵/۱۰ |
| **میانگین / Average** | - | - | **۸.۶/۱۰** |

---

### 📈 نمودار پیشرفت / Progress Chart

```
Day 1:  ████████░░░░░░░░░░░░  80%  (Pandas Basics)
Day 2:  █████████░░░░░░░░░░░  85%  (Filtering Data)
Day 3:  ████████░░░░░░░░░░░░  80%  (Series Intro)
Day 4:  ████████░░░░░░░░░░░░  80%  (Making Series)
Day 5:  ████████░░░░░░░░░░░░  80%  (Series Features)
Day 6:  █████████░░░░░░░░░░░  90%  (Important Features)
Day 7:  █████████░░░░░░░░░░░  90%  (Arithmetic Operations)
Day 8:  █████████░░░░░░░░░░░  85%  (Converting Series)
Day 9:  █████████░░░░░░░░░░░  85%  (Reading from File)
Day10:  █████████░░░░░░░░░░░  85%  (Sorting Series)
─────────────────────────────────────────────────
Avg:    █████████░░░░░░░░░░░  86%  (Overall Progress)
```

---

### 🎯 نقشه راه / Roadmap

- [x] **فاز ۱: مبانی Pandas** (۱۰۰٪) / **Phase 1: Pandas Basics** (100%)
  - [x] آشنایی با Pandas و نصب / Pandas installation
  - [x] کار با Series و DataFrame / Series & DataFrame
  - [x] فیلتر کردن داده‌ها / Data filtering
  - [x] عملیات‌های حسابی / Arithmetic operations
  - [x] مرتب‌سازی و تبدیل داده‌ها / Sorting & conversion

- [ ] **فاز ۲: مبانی DataFrame** (۰٪) / **Phase 2: DataFrame Basics** (0%)
  - [ ] کار با ستون‌ها و ردیف‌ها / Columns & rows
  - [ ] متدهای پیشرفته DataFrame / Advanced DataFrame methods
  - [ ] گروه‌بندی و تجمیع داده‌ها / Grouping & aggregation

- [ ] **فاز ۳: تحلیل داده پیشرفته** (۰٪) / **Phase 3: Advanced Data Analysis** (0%)
  - [ ] ادغام و اتصال داده‌ها / Merging & joining
  - [ ] تحلیل سری‌های زمانی / Time series analysis
  - [ ] مصورسازی داده‌ها / Data visualization

- [ ] **فاز ۴: پروژه‌های عملی** (۰٪) / **Phase 4: Practical Projects** (0%)
  - [ ] تحلیل داده‌های مالی / Financial data analysis
  - [ ] تحلیل داده‌های فروش / Sales data analysis
  - [ ] پروژه نهایی / Final project

---

## 🧠 مهارت‌های کسب شده / Skills Acquired

### کتابخانه‌های مسلط / Mastered Libraries
- ✅ **Pandas**: عملیات روی Series، فیلتر کردن، مرتب‌سازی، تبدیل، خواندن از فایل / Series operations, filtering, sorting, conversion, file reading
- 🔄 **NumPy**: در حال یادگیری / Learning in progress

### مفاهیم یادگرفته شده / Concepts Learned
- ✅ **Series**: ساخت، ایندکس‌گذاری، عملیات‌های حسابی، متدهای آماری / Series creation, indexing, arithmetic, statistical methods
- ✅ **فیلتر کردن**: شرط‌های تک و چندگانه، استفاده از `&` و `|` / Single & multiple conditions, using `&` and `|`
- ✅ **مرتب‌سازی**: `sort_index()`، `sort_values()`، `nlargest()`، `nsmallest()` / Sorting methods
- ✅ **مدیریت داده**: `dropna()`، مدیریت مقادیر خالی، `squeeze()` / Data management with `dropna()`, missing values, `squeeze()`
- ✅ **خواندن فایل**: `read_csv()`، `usecols`، `parse_dates`، `index_col` / File reading with various parameters

---

## 📝 چگونه از این مخزن استفاده کنم؟

این مخزن برای **تمرین روزانه** طراحی شده است. برنامه من:

1. **هر روز** یک مبحث جدید را انتخاب می‌کنم و آن را به طور کامل یاد می‌گیرم.
2. کدها را می‌نویسم، تست می‌کنم و در مجله یادگیری (pandas-journal) مستند می‌کنم.
3. تغییرات را کامیت کرده و به گیت‌هاب می‌فرستم.
4. در پایان هر هفته، یک مرور کلی انجام می‌دهم و پیشرفت را بررسی می‌کنم.

**چالش روزانه / Daily Challenge:**
- هر روز حداقل **۱ ساعت** کدنویسی
- نوشتن **حداقل ۵ تکه‌کد** جدید
- مستندسازی کامل یادگیری‌ها در فایل‌های Markdown

---

## 🤝 مشارکت (Contributing)

این مخزن یک مجموعه شخصی است، اما اگر پیشنهاد یا ایده‌ای برای بهبود دارید، خوشحال می‌شوم که بشنوم.  
*(This is a personal collection, but I'd be happy to hear your suggestions for improvement.)*

1. مخزن را Fork کنید.
2. یک شاخه جدید ایجاد کنید.
3. تغییرات خود را اعمال کنید.
4. یک Pull Request ایجاد کنید.

---

## 📜 مجوز (License)

این پروژه تحت مجوز **MIT** منتشر شده است - برای جزئیات بیشتر به فایل LICENSE مراجعه کنید.  
*(This project is released under the **MIT** license - see the LICENSE file for details.)*

---

## 👤 درباره من (About Me)

من **حسن باقری** هستم و این مخزن بخشی از مسیر یادگیری من در برنامه‌نویسی پایتون و تحلیل داده است.  
*(I'm **Hasan Bagheri**, and this repository is part of my learning journey in Python programming and data analysis.)*

- 📧 **Email:** hasan111bagheri@gmail.com
- 💼 **GitHub:** [github.com/0hasanbagheri0](https://github.com/0hasanbagheri0)
- 🎯 **هدف:** تبدیل شدن به یک تحلیل‌گر داده حرفه‌ای / Goal: Becoming a professional Data Analyst

---

## 🏷️ برچسب‌ها / Tags

`python` `pandas` `data-science` `data-analysis` `numpy` `learning-journal` `daily-coding` `programming` `beginner`

---

**⭐ اگر این مخزن برای شما مفید بود، لطفاً به آن ستاره (Star) دهید!**  
*(⭐ If you find this repository useful, please give it a Star!)*

---

**📅 آخرین بروزرسانی / Last Updated:** June 26, 2026
