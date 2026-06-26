"""
Day 1 Challenge: Basic Operations / چالش روز ۱: عملیات پایه
-----------------------------------------------------------
Practice: Variables, data types, and basic operations
تمرین: متغیرها، انواع داده و عملیات پایه
"""

# ===== CHALLENGE 1: Temperature Converter / تبدیل دما =====
print("=" * 50)
print("CHALLENGE 1: Temperature Converter")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit / تبدیل سلسیوس به فارنهایت"""
    # TODO: Implement conversion formula / پیاده‌سازی فرمول تبدیل
    # Formula: (°C × 9/5) + 32 = °F
    pass

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius / تبدیل فارنهایت به سلسیوس"""
    # TODO: Implement conversion formula / پیاده‌سازی فرمول تبدیل
    # Formula: (°F − 32) × 5/9 = °C
    pass

# Test your functions / تست توابع خود
# print(celsius_to_fahrenheit(0))   # Should print 32.0
# print(fahrenheit_to_celsius(32))  # Should print 0.0

# ===== CHALLENGE 2: BMI Calculator / محاسبه BMI =====
print("\n" + "=" * 50)
print("CHALLENGE 2: BMI Calculator")
print("=" * 50)

def calculate_bmi(weight, height):
    """
    Calculate BMI / محاسبه BMI
    Formula: weight(kg) / height(m)²
    """
    # TODO: Implement BMI calculation
    pass

def get_bmi_category(bmi):
    """
    Get BMI category / دریافت دسته‌بندی BMI
    - Underweight: < 18.5
    - Normal: 18.5 - 24.9
    - Overweight: 25 - 29.9
    - Obese: >= 30
    """
    # TODO: Implement category logic
    pass

# Test / تست
# bmi = calculate_bmi(70, 1.75)
# print(f"BMI: {bmi:.2f}")
# print(f"Category: {get_bmi_category(bmi)}")

# ===== CHALLENGE 3: Simple Calculator / ماشین حساب ساده =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Simple Calculator")
print("=" * 50)

def calculator(num1, num2, operation):
    """
    Simple calculator / ماشین حساب ساده
    Supports: +, -, *, /
    """
    # TODO: Implement calculator logic
    pass

# Test / تست
# print(calculator(10, 5, '+'))  # 15
# print(calculator(10, 5, '-'))  # 5
# print(calculator(10, 5, '*'))  # 50
# print(calculator(10, 5, '/'))  # 2.0
