"""
Day 8 Challenge: Lambda Functions / چالش روز ۸: توابع لامبدا
-----------------------------------------------------------
Practice: Lambda with map, filter, reduce, sorting
تمرین: لامبدا با map، filter، reduce، مرتب‌سازی
"""

from functools import reduce

# ===== CHALLENGE 1: Lambda with Map =====
print("=" * 50)
print("CHALLENGE 1: Lambda with Map")
print("=" * 50)

def apply_to_each(numbers, operation):
    """Apply operation to each number using map / اعمال عملیات روی هر عدد با map"""
    # TODO: Implement with map and lambda
    pass

def convert_to_upper(words):
    """Convert all words to uppercase / تبدیل همه کلمات به بزرگ"""
    # TODO: Implement with map and lambda
    pass

# Test / تست
# numbers = [1, 2, 3, 4, 5]
# print(apply_to_each(numbers, lambda x: x ** 2))  # [1, 4, 9, 16, 25]
# 
# words = ["hello", "world", "python"]
# print(convert_to_upper(words))  # ["HELLO", "WORLD", "PYTHON"]

# ===== CHALLENGE 2: Lambda with Filter =====
print("\n" + "=" * 50)
print("CHALLENGE 2: Lambda with Filter")
print("=" * 50)

def filter_by_condition(data, condition):
    """Filter data using condition / فیلتر داده با شرط"""
    # TODO: Implement with filter and lambda
    pass

def filter_adults(people):
    """Filter people aged 18 or older / فیلتر افراد بالای ۱۸ سال"""
    # TODO: Implement with filter and lambda
    pass

# Test / تست
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(filter_by_condition(numbers, lambda x: x % 2 == 0))  # [2, 4, 6, 8, 10]
# 
# people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 15}]
# print(filter_adults(people))  # [{"name": "Alice", "age": 25}]

# ===== CHALLENGE 3: Lambda with Reduce =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Lambda with Reduce")
print("=" * 50)

def find_max(numbers):
    """Find maximum number using reduce / پیدا کردن بزرگترین عدد با reduce"""
    # TODO: Implement with reduce and lambda
    pass

def concatenate_strings(strings):
    """Concatenate strings with comma / اتصال رشته‌ها با کاما"""
    # TODO: Implement with reduce and lambda
    pass

# Test / تست
# numbers = [5, 3, 8, 1, 9, 2]
# print(find_max(numbers))  # 9
# 
# strings = ["apple", "banana", "orange"]
# print(concatenate_strings(strings))  # "apple, banana, orange"

# ===== CHALLENGE 4: Lambda with Sorting =====
print("\n" + "=" * 50)
print("CHALLENGE 4: Lambda with Sorting")
print("=" * 50)

def sort_by_key(data, key_func):
    """Sort data by custom key / مرتب‌سازی داده با کلید سفارشی"""
    # TODO: Implement sorting with key function
    pass

def sort_products_by_price(products):
    """Sort products by price / مرتب‌سازی محصولات بر اساس قیمت"""
    # TODO: Implement sorting by price
    pass

# Test / تست
# data = ["apple", "banana", "kiwi", "strawberry"]
# print(sort_by_key(data, lambda x: len(x)))  # ["kiwi", "apple", "banana", "strawberry"]
# 
# products = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 25}]
# print(sort_products_by_price(products))  # [{"name": "Mouse", "price": 25}, ...]
