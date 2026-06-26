"""
Comprehensions in Python / کامپرهنشن‌ها در پایتون
-------------------------------------------------
Learning objectives / اهداف یادگیری:
- List comprehension / کامپرهنشن لیست
- Dictionary comprehension / کامپرهنشن دیکشنری
- Set comprehension / کامپرهنشن مجموعه
- Generator expression / عبارت ژنراتور
- Nested comprehensions / کامپرهنشن‌های تو در تو
- Conditional comprehensions / کامپرهنشن‌های شرطی
"""

print("=" * 60)
print("LIST COMPREHENSION / کامپرهنشن لیست")
print("=" * 60)

# === BASIC LIST COMPREHENSION / کامپرهنشن لیست پایه ===

# Traditional vs Comprehension / سنتی در مقابل کامپرهنشن
print("\n--- Basic Example ---")

# Traditional way / روش سنتی
squares = []
for x in range(10):
    squares.append(x ** 2)
print(f"Traditional: {squares}")

# Comprehension / کامپرهنشن
squares_comp = [x ** 2 for x in range(10)]
print(f"Comprehension: {squares_comp}")

# === CONDITIONAL LIST COMPREHENSION / کامپرهنشن لیست شرطی ===
print("\n--- Conditional Comprehension ---")

# Even numbers / اعداد زوج
even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Numbers greater than 5 / اعداد بزرگتر از 5
greater_than_5 = [x for x in range(10) if x > 5]
print(f"Greater than 5: {greater_than_5}")

# Conditional expression / عبارت شرطی
parity = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(f"Parity: {parity}")

# === NESTED LIST COMPREHENSION / کامپرهنشن لیست تو در تو ===
print("\n--- Nested List Comprehension ---")

# Flatten a matrix / صاف کردن یک ماتریس
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# 2D list comprehension / کامپرهنشن لیست دو بعدی
grid = [[i * j for j in range(5)] for i in range(5)]
print("Grid (5x5):")
for row in grid:
    print(f"  {row}")

# === DICTIONARY COMPREHENSION / کامپرهنشن دیکشنری ===
print("\n" + "=" * 60)
print("DICTIONARY COMPREHENSION / کامپرهنشن دیکشنری")
print("=" * 60)

# Basic dictionary comprehension / کامپرهنشن دیکشنری پایه
print("\n--- Basic Dictionary Comprehension ---")

# Square numbers as dictionary / اعداد مربع به عنوان دیکشنری
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Squares: {squares_dict}")

# Dictionary from two lists / دیکشنری از دو لیست
keys = ['name', 'age', 'city']
values = ['Hasan', 25, 'Tehran']
person = {k: v for k, v in zip(keys, values)}
print(f"Person: {person}")

# Conditional dictionary / دیکشنری شرطی
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Swap keys and values / جابجایی کلید و مقدار
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")

# === SET COMPREHENSION / کامپرهنشن مجموعه ===
print("\n" + "=" * 60)
print("SET COMPREHENSION / کامپرهنشن مجموعه")
print("=" * 60)

# Basic set comprehension / کامپرهنشن مجموعه پایه
print("\n--- Basic Set Comprehension ---")

# Unique squares / مربع‌های یکتا
squares_set = {x ** 2 for x in range(10)}
print(f"Set of squares: {squares_set}")

# Set with condition / مجموعه با شرط
even_set = {x for x in range(20) if x % 2 == 0}
print(f"Even set: {even_set}")

# Set from string / مجموعه از رشته
vowels = {char for char in "hello world" if char in 'aeiou'}
print(f"Vowels in 'hello world': {vowels}")

# === GENERATOR EXPRESSION / عبارت ژنراتور ===
print("\n" + "=" * 60)
print("GENERATOR EXPRESSION / عبارت ژنراتور")
print("=" * 60)

# Generator expression uses () instead of [] / عبارت ژنراتور از () به جای [] استفاده می‌کند
print("\n--- Basic Generator ---")

# Generator / ژنراتور
squares_gen = (x ** 2 for x in range(5))
print(f"Generator: {squares_gen}")
print(f"Values from generator: {list(squares_gen)}")

# Memory efficiency / کارایی حافظه
print("\n--- Memory Efficiency ---")

import sys

# List comprehension / کامپرهنشن لیست
list_comp = [x ** 2 for x in range(1000)]
list_size = sys.getsizeof(list_comp)

# Generator expression / عبارت ژنراتور
gen_exp = (x ** 2 for x in range(1000))
gen_size = sys.getsizeof(gen_exp)

print(f"List comprehension size: {list_size} bytes")
print(f"Generator expression size: {gen_size} bytes")
print(f"Generator is {list_size / gen_size:.2f}x more memory efficient!")

# === NESTED COMPREHENSIONS / کامپرهنشن‌های تو در تو ===
print("\n" + "=" * 60)
print("NESTED COMPREHENSIONS / کامپرهنشن‌های تو در تو")
print("=" * 60)

print("\n--- Multiple Examples ---")

# List of lists / لیستی از لیست‌ها
matrix_3x3 = [[i * 3 + j for j in range(3)] for i in range(3)]
print("3x3 Matrix:")
for row in matrix_3x3:
    print(f"  {row}")

# Transpose matrix / ترانهاده ماتریس
transposed = [[row[i] for row in matrix_3x3] for i in range(3)]
print("Transposed:")
for row in transposed:
    print(f"  {row}")

# Find all pairs / پیدا کردن همه جفت‌ها
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"All pairs: {pairs}")

# Pairs with condition / جفت‌ها با شرط
pairs_condition = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"Pairs with x != y: {pairs_condition}")

# === PRACTICAL EXAMPLES / مثال‌های کاربردی ===
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES / مثال‌های کاربردی")
print("=" * 60)

print("\n--- Real-world Applications ---")

# 1. Data cleaning / پاک‌سازی داده
print("\n1. Data Cleaning:")
data = ["hello", "WORLD", "   Python  ", "   ", "DATA"]
cleaned = [word.strip().lower() for word in data if word.strip()]
print(f"Original: {data}")
print(f"Cleaned: {cleaned}")

# 2. Filtering with multiple conditions / فیلتر با چند شرط
print("\n2. Multiple Conditions:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x % 2 == 0 and x > 5]
print(f"Even numbers > 5: {result}")

# 3. Processing nested data / پردازش داده‌های تو در تو
print("\n3. Nested Data:")
students = [
    {"name": "Alice", "grades": [85, 90, 88]},
    {"name": "Bob", "grades": [70, 75, 80]},
    {"name": "Charlie", "grades": [95, 92, 98]},
]

averages = {
    student["name"]: sum(student["grades"]) / len(student["grades"])
    for student in students
}
print(f"Student averages: {averages}")

# 4. Creating dictionaries with transformations / ایجاد دیکشنری با تبدیل‌ها
print("\n4. Transformations:")
words = ["apple", "banana", "cherry", "date"]
word_dict = {
    word: (len(word), word.upper())
    for word in words
}
print(f"Word info: {word_dict}")

# 5. Prime numbers with comprehension / اعداد اول با کامپرهنشن
print("\n5. Prime Numbers:")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(50) if is_prime(x)]
print(f"Prime numbers < 50: {primes}")

# === COMPARISON / مقایسه ===
print("\n" + "=" * 60)
print("COMPARISON / مقایسه")
print("=" * 60)

print("""
┌─────────────────┬──────────────┬─────────────┬──────────────┬─────────────────┐
│ Type            │ Syntax       │ Result Type │ Memory Usage │ When to Use     │
├─────────────────┼──────────────┼─────────────┼──────────────┼─────────────────┤
│ List Comp       │ [...]        │ list        │ High         │ Need full list  │
│ Set Comp        │ {...}        │ set         │ Medium       │ Need unique     │
│ Dict Comp       │ {...}        │ dict        │ Medium       │ Need key-value  │
│ Generator Exp   │ (...)        │ generator   │ Low          │ Large datasets  │
└─────────────────┴──────────────┴─────────────┴──────────────┴─────────────────┘
""")

print("\n📝 Key Takeaway / نکته کلیدی:")
print("  " + "Comprehensions make your code more Pythonic, concise, and often faster.")
print("  " + "Use generators for large datasets to save memory.")
print("  " + "کامپرهنشن‌ها کد شما را پایتونیک‌تر، مختصرتر و اغلب سریع‌تر می‌کنند.")
print("  " + "برای دیتاست‌های بزرگ از ژنراتورها استفاده کنید تا حافظه را ذخیره کنید.")
