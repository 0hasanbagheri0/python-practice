"""
Day 5 Challenge: File Handling / چالش روز ۵: کار با فایل
-------------------------------------------------------
Practice: Reading and writing files
تمرین: خواندن و نوشتن فایل‌ها
"""

import json

# ===== CHALLENGE 1: File Reader / خواننده فایل =====
print("=" * 50)
print("CHALLENGE 1: File Reader")
print("=" * 50)

def read_file_with_stats(filename):
    """
    Read file and return statistics / خواندن فایل و بازگرداندن آمار
    Returns: line_count, word_count, char_count
    """
    # TODO: Implement file reading with statistics
    pass

def write_summary(filename, stats):
    """Write summary to a new file / نوشتن خلاصه در فایل جدید"""
    # TODO: Implement summary writing
    pass

# Test / تست
# stats = read_file_with_stats("sample.txt")
# write_summary("summary.txt", stats)
# print(f"Lines: {stats['lines']}, Words: {stats['words']}, Chars: {stats['chars']}")

# ===== CHALLENGE 2: CSV Operations / عملیات CSV =====
print("\n" + "=" * 50)
print("CHALLENGE 2: CSV Operations")
print("=" * 50)

import csv

def read_csv_as_dict(filename):
    """Read CSV file as list of dictionaries / خواندن CSV به عنوان لیست دیکشنری"""
    # TODO: Implement CSV reading
    pass

def write_csv_from_dict(filename, data):
    """Write data to CSV file / نوشتن داده در فایل CSV"""
    # TODO: Implement CSV writing
    pass

def filter_csv_by_column(data, column, value):
    """Filter CSV data by column value / فیلتر داده‌های CSV بر اساس ستون"""
    # TODO: Implement CSV filtering
    pass

# Test / تست
# data = [
#     {"name": "Alice", "age": "25", "city": "Tehran"},
#     {"name": "Bob", "age": "30", "city": "Mashhad"},
#     {"name": "Charlie", "age": "22", "city": "Tehran"}
# ]
# write_csv_from_dict("people.csv", data)
# loaded = read_csv_as_dict("people.csv")
# filtered = filter_csv_by_column(loaded, "city", "Tehran")
# print(filtered)  # Only Alice and Charlie

# ===== CHALLENGE 3: JSON Operations / عملیات JSON =====
print("\n" + "=" * 50)
print("CHALLENGE 3: JSON Operations")
print("=" * 50)

def save_to_json(data, filename):
    """Save data to JSON file / ذخیره داده در فایل JSON"""
    # TODO: Implement JSON saving
    pass

def load_from_json(filename):
    """Load data from JSON file / بارگیری داده از فایل JSON"""
    # TODO: Implement JSON loading
    pass

def merge_json_files(files):
    """Merge multiple JSON files / ادغام چند فایل JSON"""
    # TODO: Implement JSON merging
    pass

# Test / تست
# data = {"name": "Hasan", "age": 25, "skills": ["Python", "SQL"]}
# save_to_json(data, "profile.json")
# loaded = load_from_json("profile.json")
# print(loaded)
