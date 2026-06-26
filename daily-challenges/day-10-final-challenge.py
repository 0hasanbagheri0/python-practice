"""
Day 10 Challenge: Final Challenge / چالش روز ۱۰: چالش نهایی
---------------------------------------------------------
A comprehensive challenge combining everything learned
یک چالش جامع ترکیبی از همه مفاهیم یادگرفته شده
"""

# ===== CHALLENGE: Personal Library Manager / مدیریت کتابخانه شخصی =====
print("=" * 60)
print("FINAL CHALLENGE: Personal Library Manager")
print("چالش نهایی: مدیریت کتابخانه شخصی")
print("=" * 60)

"""
🎯 GOAL / هدف:
Create a library management system that uses everything you've learned:
سیستم مدیریت کتابخانه که از همه مفاهیم یادگرفته شده استفاده می‌کند:

✅ Variables & Data Types / متغیرها و انواع داده
✅ Lists, Dictionaries, Sets / لیست‌ها، دیکشنری‌ها، مجموعه‌ها
✅ Functions / توابع
✅ File Handling / کار با فایل
✅ Error Handling / مدیریت خطا
✅ Comprehensions / کامپرهنشن‌ها
✅ Lambda Functions / توابع لامبدا
✅ Recursion (optional) / بازگشت (اختیاری)
"""

import json
import os
from datetime import datetime

class LibraryManager:
    """
    Library Manager System / سیستم مدیریت کتابخانه
    """
    
    def __init__(self, data_file="library.json"):
        """Initialize library with data file / مقداردهی اولیه کتابخانه با فایل داده"""
        self.data_file = data_file
        self.books = []
        self.load_data()
    
    def load_data(self):
        """Load books from file / بارگیری کتاب‌ها از فایل"""
        # TODO: Load from JSON file / بارگیری از فایل JSON
        # If file doesn't exist, create empty list / اگر فایل وجود ندارد، لیست خالی ایجاد کن
        pass
    
    def save_data(self):
        """Save books to file / ذخیره کتاب‌ها در فایل"""
        # TODO: Save to JSON file / ذخیره در فایل JSON
        pass
    
    def add_book(self, title, author, year, genre, rating=0):
        """Add a book to library / اضافه کردن کتاب
