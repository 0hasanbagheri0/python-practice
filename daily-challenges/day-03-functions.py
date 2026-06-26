"""
Day 3 Challenge: Functions / چالش روز ۳: توابع
-----------------------------------------------
Practice: Defining functions, parameters, return values
تمرین: تعریف توابع، پارامترها، مقادیر بازگشتی
"""

# ===== CHALLENGE 1: String Operations / عملیات روی رشته =====
print("=" * 50)
print("CHALLENGE 1: String Operations")
print("=" * 50)

def reverse_string(text):
    """Reverse a string / معکوس کردن رشته"""
    # TODO: Implement string reversal
    pass

def count_vowels(text):
    """Count vowels in a string / شمارش حروف صدادار"""
    # TODO: Implement vowel counting
    pass

def is_palindrome(text):
    """Check if a string is a palindrome / بررسی پالیندروم بودن"""
    # TODO: Implement palindrome check
    pass

# Test / تست
# print(reverse_string("python"))  # "nohtyp"
# print(count_vowels("hello"))     # 2
# print(is_palindrome("radar"))    # True

# ===== CHALLENGE 2: List Operations / عملیات روی لیست =====
print("\n" + "=" * 50)
print("CHALLENGE 2: List Operations")
print("=" * 50)

def find_maximum(numbers):
    """Find maximum number in list / پیدا کردن بزرگترین عدد"""
    # TODO: Implement find maximum
    pass

def find_minimum(numbers):
    """Find minimum number in list / پیدا کردن کوچکترین عدد"""
    # TODO: Implement find minimum
    pass

def calculate_average(numbers):
    """Calculate average of list / محاسبه میانگین"""
    # TODO: Implement average calculation
    pass

def remove_duplicates(numbers):
    """Remove duplicates from list / حذف تکراری‌ها"""
    # TODO: Implement duplicate removal
    pass

# Test / تست
# numbers = [1, 2, 3, 2, 4, 5, 3, 6]
# print(find_maximum(numbers))     # 6
# print(find_minimum(numbers))     # 1
# print(calculate_average(numbers)) # 3.25
# print(remove_duplicates(numbers)) # [1, 2, 3, 4, 5, 6]

# ===== CHALLENGE 3: Shopping Cart / سبد خرید =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Shopping Cart")
print("=" * 50)

def add_item(cart, item, price):
    """Add item to cart / اضافه کردن کالا به سبد"""
    # TODO: Implement add item
    pass

def remove_item(cart, item):
    """Remove item from cart / حذف کالا از سبد"""
    # TODO: Implement remove item
    pass

def calculate_total(cart):
    """Calculate total price / محاسبه قیمت کل"""
    # TODO: Implement total calculation
    pass

def show_cart(cart):
    """Display cart contents / نمایش محتویات سبد"""
    # TODO: Implement cart display
    pass

# Test / تست
# cart = {}
# add_item(cart, "Apple", 1.5)
# add_item(cart, "Banana", 0.8)
# add_item(cart, "Orange", 1.2)
# show_cart(cart)
# print(f"Total: ${calculate_total(cart)}")
# remove_item(cart, "Banana")
# show_cart(cart)
