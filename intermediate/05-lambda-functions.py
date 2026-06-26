"""
Lambda Functions in Python / توابع لامبدا در پایتون
---------------------------------------------------
Learning objectives / اهداف یادگیری:
- Understanding lambda functions / درک توابع لامبدا
- Using lambda with built-in functions / استفاده از لامبدا با توابع داخلی
- Lambda with map, filter, reduce / لامبدا با map، filter، reduce
- Sorting with lambda / مرتب‌سازی با لامبدا
- Practical applications / کاربردهای عملی
"""

from functools import reduce
import math

print("=" * 60)
print("LAMBDA FUNCTIONS / توابع لامبدا")
print("=" * 60)

# === BASIC LAMBDA / لامبدای پایه ===
print("\n--- Basic Lambda ---")

# Regular function vs lambda / تابع معمولی در مقابل لامبدا
def add_regular(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(f"Regular function: {add_regular(5, 3)}")
print(f"Lambda function: {add_lambda(5, 3)}")

# Lambda with no arguments / لامبدا بدون آرگومان
greet = lambda: "Hello, World!"
print(f"Greeting: {greet()}")

# Lambda with default arguments / لامبدا با آرگومان‌های پیش‌فرض
power = lambda x, y=2: x ** y
print(f"3^2 = {power(3)}")
print(f"3^3 = {power(3, 3)}")

# === LAMBDA WITH MAP / لامبدا با Map ===
print("\n" + "=" * 60)
print("LAMBDA WITH MAP / لامبدا با Map")
print("=" * 60)

print("\n--- Map Examples ---")

# Square all numbers / مربع همه اعداد
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Convert to string / تبدیل به رشته
str_nums = list(map(lambda x: f"Number: {x}", numbers))
print(f"Strings: {str_nums}")

# Multiple lists / چندین لیست
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"List1: {list1}, List2: {list2}")
print(f"Sum: {sums}")

# === LAMBDA WITH FILTER / لامبدا با Filter ===
print("\n" + "=" * 60)
print("LAMBDA WITH FILTER / لامبدا با Filter")
print("=" * 60)

print("\n--- Filter Examples ---")

# Filter even numbers / فیلتر اعداد زوج
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All numbers: {numbers}")
print(f"Even numbers: {even}")

# Filter strings > 3 characters / فیلتر رشته‌های > 3 کاراکتر
words = ["apple", "hi", "python", "ok", "lambda", "x"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(f"Words: {words}")
print(f"Words > 3 chars: {long_words}")

# Filter with multiple conditions / فیلتر با چند شرط
numbers = range(1, 21)
filtered = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(f"Numbers divisible by both 2 and 3: {filtered}")

# === LAMBDA WITH REDUCE / لامبدا با Reduce ===
print("\n" + "=" * 60)
print("LAMBDA WITH REDUCE / لامبدا با Reduce")
print("=" * 60)

print("\n--- Reduce Examples ---")

# Sum all numbers / جمع همه اعداد
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(f"Sum of {numbers}: {sum_all}")

# Find maximum / پیدا کردن بزرگترین
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum of {numbers}: {max_num}")

# Factorial using reduce / فاکتوریل با reduce
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"{n}! = {factorial}")

# List concatenation / اتصال لیست‌ها
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, list_of_lists)
print(f"Flattened: {flattened}")

# === LAMBDA WITH SORTING / لامبدا با مرتب‌سازی ===
print("\n" + "=" * 60)
print("LAMBDA WITH SORTING / لامبدا با مرتب‌سازی")
print("=" * 60)

print("\n--- Sorting Examples ---")

# Sort by absolute value / مرتب‌سازی بر اساس قدر مطلق
numbers = [3, -1, -4, 2, -2, 5]
sorted_abs = sorted(numbers, key=lambda x: abs(x))
print(f"Original: {numbers}")
print(f"Sorted by abs: {sorted_abs}")

# Sort strings by length / مرتب‌سازی رشته‌ها بر اساس طول
words = ["apple", "hi", "python", "ok", "lambda", "x"]
sorted_length = sorted(words, key=lambda x: len(x))
print(f"Original: {words}")
print(f"Sorted by length: {sorted_length}")

# Sort list of dictionaries / مرتب‌سازی لیست دیکشنری‌ها
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28}
]

sorted_by_age = sorted(people, key=lambda x: x["age"])
print("Sorted by age:")
for person in sorted_by_age:
    print(f"  {person['name']}: {person['age']}")

sorted_by_name = sorted(people, key=lambda x: x["name"])
print("\nSorted by name:")
for person in sorted_by_name:
    print(f"  {person['name']}: {person['age']}")

# Sort tuples / مرتب‌سازی تاپل‌ها
points = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_by_x = sorted(points, key=lambda x: x[0])
sorted_by_y = sorted(points, key=lambda x: x[1])
print(f"Original points: {points}")
print(f"Sorted by x: {sorted_by_x}")
print(f"Sorted by y: {sorted_by_y}")

# === LAMBDA WITH MAX/MIN / لامبدا با Max/Min ===
print("\n" + "=" * 60)
print("LAMBDA WITH MAX/MIN / لامبدا با Max/Min")
print("=" * 60)

# Find person with max age / پیدا کردن شخص با بیشترین سن
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
]
oldest = max(people, key=lambda x: x["age"])
youngest = min(people, key=lambda x: x["age"])
print(f"Oldest: {oldest['name']} ({oldest['age']})")
print(f"Youngest: {youngest['name']} ({youngest['age']})")

# === PRACTICAL APPLICATIONS / کاربردهای عملی ===
print("\n" + "=" * 60)
print("PRACTICAL APPLICATIONS / کاربردهای عملی")
print("=" * 60)

print("\n--- Real-world Examples ---")

# 1. Data transformation / تبدیل داده
print("\n1. Data Transformation:")
temperatures = [32, 0, 15, -5, 25]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperatures))
print(f"Celsius: {temperatures}")
print(f"Fahrenheit: {fahrenheit}")

# 2. Email validation / اعتبارسنجی ایمیل
print("\n2. Email Validation:")
emails = ["test@email.com", "invalid", "user@domain.com", "no-at.com"]
valid = list(filter(lambda x: "@" in x and "." in x, emails))
print(f"Emails: {emails}")
print(f"Valid emails: {valid}")

# 3. User authentication / احراز هویت کاربر
print("\n3. User Authentication:")
users = [
    {"username": "admin", "password": "1234"},
    {"username": "user1", "password": "pass"},
    {"username": "guest", "password": "guest"}
]

credentials = {"username": "admin", "password": "1234"}
authenticated = any(
    user["username"] == credentials["username"] and 
    user["password"] == credentials["password"] 
    for user in users
)
print(f"Authentication result: {authenticated}")

# 4. Processing nested data / پردازش داده‌های تو در تو
print("\n4. Processing Nested Data:")
orders = [
    {"items": [{"name": "Book", "price": 15}, {"name": "Pen", "price": 2}]},
    {"items": [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 25}]},
]

total_values = list(map(
    lambda order: sum(item["price"] for item in order["items"]),
    orders
))
print(f"Order totals: {total_values}")

# 5. Data cleaning / پاک‌سازی داده
print("\n5. Data Cleaning:")
raw_data = ["  hello  ", "WORLD", "   python   ", "DATA  "]
cleaned = list(map(lambda x: x.strip().title(), raw_data))
print(f"Raw: {raw_data}")
print(f"Cleaned: {cleaned}")

# 6. Creating functions on the fly / ایجاد توابع در لحظه
print("\n6. Dynamic Functions:")
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# === WHEN TO USE LAMBDA / چه زمانی از لامبدا استفاده کنیم ===
print("\n" + "=" * 60)
print("WHEN TO USE LAMBDA / چه زمانی از لامبدا استفاده کنیم")
print("=" * 60)

print("""
✅ Use Lambda when:
   • Function is simple (single expression) / تابع ساده است (یک عبارت)
   • You need a function for a short time / به تابع برای مدت کوتاه نیاز دارید
   • Using with map, filter, reduce, sorted / استفاده با map، filter، reduce، sorted
   • Making code more readable / خواناتر کردن کد

❌ Don't Use Lambda when:
   • Function needs multiple lines / تابع نیاز به چند خط دارد
   • Function will be reused many times / تابع بارها استفاده می‌شود
   • Need docstrings or annotations / به docstring یا annotation نیاز دارید
   • Complex logic involved / منطق پیچیده درگیر است
""")

print("\n📝 Key Takeaway / نکته کلیدی:")
print("  " + "Lambda functions are powerful tools for functional programming in Python.")
print("  " + "They shine when used with map, filter, reduce, and sorting functions.")
print("  " + "توابع لامبدا ابزارهای قدرتمندی برای برنامه‌نویسی تابعی در پایتون هستند.")
print("  " + "آنها زمانی درخشان هستند که با توابع map، filter، reduce و مرتب‌سازی استفاده شوند.")
