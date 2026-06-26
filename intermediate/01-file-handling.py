"""
File Handling in Python / کار با فایل‌ها در پایتون
------------------------------------------------
Learning objectives / اهداف یادگیری:
- Reading and writing text files / خواندن و نوشتن فایل‌های متنی
- Working with CSV files / کار با فایل‌های CSV
- Using context managers (with statement) / استفاده از مدیریت زمینه
- File paths and directories / مسیرها و دایرکتوری‌ها
"""

import os
import csv
from pathlib import Path

# === TEXT FILES / فایل‌های متنی ===
print("=" * 50)
print("TEXT FILES / فایل‌های متنی")
print("=" * 50)

# Writing to a file / نوشتن در فایل
with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This is the second line.\n")
    file.write("Python is awesome!\n")

print("File created successfully! / فایل با موفقیت ایجاد شد!")

# Reading from a file / خواندن از فایل
with open('example.txt', 'r') as file:
    content = file.read()
    print(f"File content:\n{content}")

# Reading line by line / خواندن خط به خط
print("\nReading line by line:")
with open('example.txt', 'r') as file:
    for line in file:
        print(f"Line: {line.strip()}")

# Appending to a file / اضافه کردن به فایل
with open('example.txt', 'a') as file:
    file.write("Adding a new line at the end.\n")
    file.write("Another line added.\n")

print("\nFile after appending:")
with open('example.txt', 'r') as file:
    print(file.read())

# === CSV FILES / فایل‌های CSV ===
print("\n" + "=" * 50)
print("CSV FILES / فایل‌های CSV")
print("=" * 50)

# Sample data / داده‌های نمونه
data = [
    ['Name', 'Age', 'City', 'Score'],
    ['Hasan', 25, 'Tehran', 85],
    ['Ali', 30, 'Esfahan', 92],
    ['Sara', 22, 'Shiraz', 78],
    ['Reza', 35, 'Mashhad', 88]
]

# Writing CSV file / نوشتن فایل CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully! / فایل CSV با موفقیت ایجاد شد!")

# Reading CSV file / خواندن فایل CSV
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(', '.join(row))

# Using pandas to read CSV / استفاده از پانداس برای خواندن CSV
import pandas as pd
df = pd.read_csv('data.csv')
print(f"\nUsing pandas:\n{df}")

# === FILE AND DIRECTORY OPERATIONS / عملیات فایل و دایرکتوری ===
print("\n" + "=" * 50)
print("FILE AND DIRECTORY OPERATIONS / عملیات فایل و دایرکتوری")
print("=" * 50)

# Check if file exists / بررسی وجود فایل
file_exists = os.path.exists('example.txt')
print(f"Does example.txt exist? / آیا example.txt وجود دارد؟ {file_exists}")

# Get file size / دریافت حجم فایل
if file_exists:
    size = os.path.getsize('example.txt')
    print(f"File size / حجم فایل: {size} bytes")

# Get file info / دریافت اطلاعات فایل
if file_exists:
    stat = os.stat('example.txt')
    print(f"Last modified / آخرین تغییر: {stat.st_mtime}")

# Working with paths / کار با مسیرها
current_dir = os.getcwd()
print(f"Current directory / دایرکتوری فعلی: {current_dir}")

# Using pathlib (modern approach) / استفاده از pathlib (روش مدرن)
path = Path('.')
print(f"Files in current directory:\n{list(path.glob('*.txt'))}")

# Create directory / ایجاد دایرکتوری
new_dir = Path('test_folder')
new_dir.mkdir(exist_ok=True)
print(f"Directory created: {new_dir}")

# Clean up / پاک‌سازی
# os.remove('example.txt')
# os.remove('data.csv')
# os.rmdir('test_folder')
# print("Cleanup completed!")
