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
        """Add a book to library / اضافه کردن کتاب به کتابخانه"""
        # TODO: Add book with validation / اضافه کردن کتاب با اعتبارسنجی
        # Rating must be 0-5 / امتیاز باید ۰-۵ باشد
        # Year must be valid / سال باید معتبر باشد
        pass
    
    def search_books(self, query, field="title"):
        """
        Search books by field / جستجوی کتاب‌ها بر اساس فیلد
        Use lambda for filtering / استفاده از لامبدا برای فیلتر
        """
        # TODO: Implement search with lambda / پیاده‌سازی جستجو با لامبدا
        pass
    
    def get_books_by_author(self, author):
        """Get all books by an author / دریافت همه کتاب‌های یک نویسنده"""
        # TODO: Use list comprehension / استفاده از کامپرهنشن لیست
        pass
    
    def get_books_by_rating(self, min_rating):
        """Get books with rating >= min_rating / دریافت کتاب‌های با امتیاز >= min_rating"""
        # TODO: Use filter with lambda / استفاده از filter با لامبدا
        pass
    
    def get_statistics(self):
        """
        Get library statistics / دریافت آمار کتابخانه
        Returns: total_books, unique_authors, average_rating, genres_count
        """
        # TODO: Calculate statistics / محاسبه آمار
        # Use sets for unique authors / استفاده از مجموعه برای نویسندگان یکتا
        # Use dict for genre counts / استفاده از دیکشنری برای تعداد ژانرها
        pass
    
    def get_top_rated(self, n=5):
        """Get top n highest rated books / دریافت n کتاب با بالاترین امتیاز"""
        # TODO: Sort by rating with lambda / مرتب‌سازی بر اساس امتیاز با لامبدا
        pass
    
    def delete_book(self, title):
        """Delete a book by title / حذف کتاب بر اساس عنوان"""
        # TODO: Delete with error handling / حذف با مدیریت خطا
        pass
    
    def display_books(self, books=None):
        """Display books in formatted output / نمایش کتاب‌ها به صورت فرمت‌شده"""
        # TODO: Display books nicely / نمایش زیبای کتاب‌ها
        pass


def main():
    """
    Main interactive function / تابع تعاملی اصلی
    """
    # TODO: Create library manager / ایجاد مدیریت کتابخانه
    # TODO: Show menu / نمایش منو
    # TODO: Handle user input / مدیریت ورودی کاربر
    # TODO: Add error handling / افزودن مدیریت خطا
    pass


if __name__ == "__main__":
    main()

print("\n" + "=" * 60)
print("🎯 FINAL CHALLENGE INSTRUCTIONS")
print("=" * 60)

print("""
📝 Complete the LibraryManager class by implementing all methods:

1. add_book(title, author, year, genre, rating)
2. search_books(query, field)
3. get_books_by_author(author)
4. get_books_by_rating(min_rating)
5. get_statistics()
6. get_top_rated(n)
7. delete_book(title)
8. display_books(books)

✅ Use: lists, dicts, functions, file I/O, error handling
✅ Use: comprehensions, lambda, sorting, filtering
✅ Use: validation, statistics, formatted output

🌟 Bonus: Add recursion for nested operations
🌟 Bonus: Add tests for each function

Test your implementation with sample data:
Sample books:
- "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 4.5
- "1984", "George Orwell", 1949, "Dystopian", 4.8
- "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 4.7
""")

print("\n🎉 Congratulations on completing the 10-day challenge!")
print("   Keep practicing and building on what you've learned!")
