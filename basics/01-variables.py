"""
Day 1: Variables and Data Types / متغیرها و انواع داده
-----------------------------------------------
Learning objectives / اهداف یادگیری:
- Understanding different data types in Python / آشنایی با انواع داده در پایتون
- Working with variables and assignment / کار با متغیرها و مقداردهی
- Type conversion / تبدیل نوع داده
"""

# Integer / عدد صحیح
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float / عدد اعشاری
price = 99.99
print(f"Price: ${price}, Type: {type(price)}")

# String / رشته
name = "Hasan"
print(f"Name: {name}, Type: {type(name)}")

# Boolean / بولین
is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# List / لیست
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}, Type: {type(fruits)}")

# Tuple / تاپل (غیرقابل تغییر)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")

# Dictionary / دیکشنری
person = {
    "name": "Hasan",
    "age": 25,
    "city": "Tehran"
}
print(f"Person: {person}, Type: {type(person)}")

# Type conversion / تبدیل نوع داده
num_str = "123"
num_int = int(num_str)
print(f"String to Int: {num_str} -> {num_int}, Type: {type(num_int)}")

num_float = float(num_int)
print(f"Int to Float: {num_int} -> {num_float}, Type: {type(num_float)}")

# Multiple assignment / تخصیص چندگانه
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Swap variables / جابجایی متغیرها
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")
