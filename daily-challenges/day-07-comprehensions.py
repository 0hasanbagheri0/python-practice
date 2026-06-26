"""
Day 7 Challenge: Comprehensions / چالش روز ۷: کامپرهنشن‌ها
---------------------------------------------------------
Practice: List, dict, set comprehensions
تمرین: کامپرهنشن‌های لیست، دیکشنری، مجموعه
"""

# ===== CHALLENGE 1: Data Processing / پردازش داده =====
print("=" * 50)
print("CHALLENGE 1: Data Processing")
print("=" * 50)

def square_even_numbers(numbers):
    """Square only even numbers using list comprehension / مربع اعداد زوج با کامپرهنشن لیست"""
    # TODO: Implement with list comprehension
    pass

def filter_long_words(words, min_length=5):
    """Filter words longer than min_length / فیلتر کلمات بلندتر از min_length"""
    # TODO: Implement with list comprehension
    pass

def extract_values(data, key):
    """Extract specific values from list of dictionaries / استخراج مقادیر خاص از لیست دیکشنری‌ها"""
    # TODO: Implement with list comprehension
    pass

# Test / تست
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(square_even_numbers(numbers))  # [4, 16, 36, 64]
# 
# words = ["apple", "hi", "python", "ok", "programming"]
# print(filter_long_words(words, 4))  # ["apple", "python", "programming"]
# 
# data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
# print(extract_values(data, "name"))  # ["Alice", "Bob"]

# ===== CHALLENGE 2: Dictionary Transformations / تبدیل دیکشنری =====
print("\n" + "=" * 50)
print("CHALLENGE 2: Dictionary Transformations")
print("=" * 50)

def invert_dictionary(d):
    """Invert dictionary (keys become values) / معکوس کردن دیکشنری"""
    # TODO: Implement with dict comprehension
    pass

def filter_by_value(d, threshold):
    """Filter dictionary by value / فیلتر دیکشنری بر اساس مقدار"""
    # TODO: Implement with dict comprehension
    pass

def group_by_key(data, key):
    """Group list of dictionaries by a key / گروه‌بندی لیست دیکشنری‌ها بر اساس کلید"""
    # TODO: Implement grouping
    pass

# Test / تست
# d = {"a": 1, "b": 2, "c": 3}
# print(invert_dictionary(d))  # {1: "a", 2: "b", 3: "c"}
# 
# scores = {"Alice": 85, "Bob": 70, "Charlie": 95}
# print(filter_by_value(scores, 80))  # {"Alice": 85, "Charlie": 95}

# ===== CHALLENGE 3: Set Operations / عملیات مجموعه =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Set Operations")
print("=" * 50)

def common_elements(list1, list2):
    """Find common elements between two lists / پیدا کردن عناصر مشترک"""
    # TODO: Implement with set comprehension
    pass

def unique_characters(text):
    """Get unique characters from text / دریافت کاراکترهای یکتا از متن"""
    # TODO: Implement with set comprehension
    pass

# Test / تست
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# print(common_elements(list1, list2))  # {4, 5}
# 
# text = "hello world"
# print(unique_characters(text))  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
