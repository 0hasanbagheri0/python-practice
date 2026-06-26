"""
Day 5: Data Structures / ساختارهای داده
-----------------------------------------------
Learning objectives / اهداف یادگیری:
- Working with Lists / کار با لیست‌ها
- Working with Tuples / کار با تاپل‌ها
- Working with Dictionaries / کار با دیکشنری‌ها
- Working with Sets / کار با مجموعه‌ها
- Common operations and methods / عملیات و متدهای رایج
"""

# === LISTS / لیست‌ها ===
print("=" * 40)
print("LISTS / لیست‌ها")
print("=" * 40)

# Creating lists / ایجاد لیست
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")  # Indexing / ایندکس‌گذاری
print(f"Last fruit: {fruits[-1]}")  # Negative indexing / ایندکس منفی
print(f"Slice: {fruits[1:3]}")      # Slicing / برش

# List operations / عملیات روی لیست
fruits.append("mango")          # Add to end / اضافه به انتها
print(f"Appended: {fruits}")

fruits.insert(1, "kiwi")        # Insert at index / درج در ایندکس
print(f"Inserted: {fruits}")

fruits.remove("banana")         # Remove by value / حذف بر اساس مقدار
print(f"Removed banana: {fruits}")

popped = fruits.pop()           # Remove and return last / حذف و بازگشت آخرین
print(f"Popped: {popped}")
print(f"After pop: {fruits}")

fruits.reverse()                # Reverse the list / معکوس کردن لیست
print(f"Reversed: {fruits}")

fruits.sort()                   # Sort the list / مرتب‌سازی لیست
print(f"Sorted: {fruits}")

# List comprehension / کامپرهنشن لیست
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

even = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {even}")

# === TUPLES / تاپل‌ها (غیرقابل تغییر) ===
print("\n" + "=" * 40)
print("TUPLES / تاپل‌ها")
print("=" * 40)

# Creating tuples / ایجاد تاپل
colors = ("red", "green", "blue")
coordinates = (10, 20)

print(f"Colors: {colors}")
print(f"First color: {colors[0]}")

# Tuple unpacking / باز کردن تاپل
x, y = coordinates
print(f"Coordinates: x={x}, y={y}")

# Tuple with one element (needs comma) / تاپل با یک عنصر (نیاز به ویرگول)
single = (5,)  # Not (5) - that would be int / (5) عدد صحیح است نه تاپل
print(f"Single tuple: {single}")

# === DICTIONARIES / دیکشنری‌ها ===
print("\n" + "=" * 40)
print("DICTIONARIES / دیکشنری‌ها")
print("=" * 40)

# Creating dictionaries / ایجاد دیکشنری
person = {
    "name": "Hasan",
    "age": 25,
    "city": "Tehran",
    "skills": ["Python", "SQL", "Data Analysis"]
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")

# Adding/modifying keys / افزودن/تغییر کلیدها
person["email"] = "hasan@example.com"
print(f"Updated: {person}")

# Iterating over dictionary / پیمایش دیکشنری
print("\nDictionary items:")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension / کامپرهنشن دیکشنری
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# === SETS / مجموعه‌ها (بدون ترتیب، بدون تکراری) ===
print("\n" + "=" * 40)
print("SETS / مجموعه‌ها")
print("=" * 40)

# Creating sets / ایجاد مجموعه
unique_numbers = {1, 2, 3, 3, 4, 4, 5}  # Duplicates removed / تکراری‌ها حذف می‌شوند
print(f"Set: {unique_numbers}")

# Set operations / عملیات مجموعه
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A ∪ B): {set_a | set_b}")          # Union / اجتماع
print(f"Intersection (A ∩ B): {set_a & set_b}")    # Intersection / اشتراک
print(f"Difference (A - B): {set_a - set_b}")      # Difference / تفاضل
print(f"Symmetric Difference: {set_a ^ set_b}")    # Symmetric difference / تفاضل متقارن

# Adding to set / افزودن به مجموعه
set_a.add(10)
print(f"Added to A: {set_a}")

# === COMPARISON / مقایسه ===
print("\n" + "=" * 40)
print("COMPARISON / مقایسه")
print("=" * 40)

# List vs Tuple vs Set vs Dict
print("List: mutable, ordered, allows duplicates / قابل تغییر، مرتب، اجازه تکراری")
print("Tuple: immutable, ordered, allows duplicates / غیرقابل تغییر، مرتب، اجازه تکراری")
print("Set: mutable, unordered, no duplicates / قابل تغییر، نامرتب، بدون تکراری")
print("Dict: mutable, ordered (Python 3.7+), key-value pairs / قابل تغییر، مرتب، کلید-مقدار")
