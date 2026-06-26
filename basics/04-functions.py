"""
Day 4: Functions / توابع
-----------------------------------------------
Learning objectives / اهداف یادگیری:
- Defining functions / تعریف توابع
- Parameters and arguments / پارامترها و آرگومان‌ها
- Return values / مقادیر بازگشتی
- Default parameters / پارامترهای پیش‌فرض
- Variable scope / محدوده متغیرها
- Lambda functions / توابع لامبدا
"""

# Basic function / تابع ساده
def greet():
    """Function that says hello / تابعی که سلام می‌گوید"""
    print("Hello! / سلام!")

# Call function / فراخوانی تابع
greet()

# Function with parameters / تابع با پارامتر
def greet_person(name):
    """Greet a specific person / به یک شخص خاص سلام کن"""
    print(f"Hello, {name}! / سلام، {name}!")

greet_person("Hasan")

# Function with return value / تابع با مقدار بازگشتی
def add(a, b):
    """Add two numbers / دو عدد را جمع کن"""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple return values / تابع با چند مقدار بازگشتی
def get_min_max(numbers):
    """Return min and max of a list / کوچکترین و بزرگترین لیست را برگردان"""
    return min(numbers), max(numbers)

numbers = [10, 20, 5, 30, 15]
min_val, max_val = get_min_max(numbers)
print(f"Min: {min_val}, Max: {max_val}")

# Default parameters / پارامترهای پیش‌فرض
def power(base, exponent=2):
    """Raise base to the power of exponent (default 2) / عدد را به توان برسان (پیش‌فرض ۲)"""
    return base ** exponent

print(f"3^2 = {power(3)}")
print(f"3^3 = {power(3, 3)}")

# Keyword arguments / آرگومان‌های کلیدواژه‌ای
def introduce(name, age, city):
    """Introduce a person / یک شخص را معرفی کن"""
    print(f"I'm {name}, {age} years old from {city}")

introduce(name="Hasan", city="Tehran", age=25)

# Variable scope / محدوده متغیرها
global_var = "I'm global"  # Global variable / متغیر سراسری

def scope_example():
    local_var = "I'm local"  # Local variable / متغیر محلی
    print(global_var)  # Can access global / می‌تواند به متغیر سراسری دسترسی داشته باشد
    print(local_var)

scope_example()
# print(local_var)  # Error: local_var is not defined here / خطا: local_var در اینجا تعریف نشده است

# Using global keyword / استفاده از کلیدواژه global
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(f"Counter: {counter}")

# *args (arbitrary arguments) / آرگومان‌های دلخواه
def sum_all(*args):
    """Sum any number of arguments / هر تعداد آرگومان را جمع کن"""
    return sum(args)

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs (keyword arguments) / آرگومان‌های کلیدواژه‌ای دلخواه
def print_info(**kwargs):
    """Print all keyword arguments / همه آرگومان‌های کلیدواژه‌ای را چاپ کن"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Hasan", age=25, job="Developer")

# Lambda function (anonymous function) / تابع لامبدا (ناشناس)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments / لامبدا با چند آرگومان
add_lambda = lambda a, b: a + b
print(f"Lambda sum: {add_lambda(10, 20)}")

# Lambda with map / لامبدا با map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Lambda with filter / لامبدا با filter
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even}")
