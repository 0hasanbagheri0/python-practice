"""
Day 6 Challenge: Error Handling / چالش روز ۶: مدیریت خطا
-------------------------------------------------------
Practice: Try-except, custom exceptions
تمرین: try-except، استثناهای سفارشی
"""

# ===== CHALLENGE 1: Safe Division / تقسیم ایمن =====
print("=" * 50)
print("CHALLENGE 1: Safe Division")
print("=" * 50)

def safe_divide(a, b):
    """
    Safely divide two numbers / تقسیم ایمن دو عدد
    Handle ZeroDivisionError and TypeError
    """
    # TODO: Implement safe division with error handling
    pass

def safe_divide_list(numbers):
    """
    Safely divide all numbers by 2 / تقسیم ایمن همه اعداد بر ۲
    Skip non-numeric values / رد کردن مقادیر غیرعددی
    """
    # TODO: Implement safe division for list
    pass

# Test / تست
# print(safe_divide(10, 2))    # 5.0
# print(safe_divide(10, 0))    # "Error: Cannot divide by zero"
# print(safe_divide(10, "2"))  # "Error: Both arguments must be numbers"
# print(safe_divide_list([10, "5", 20, None, 0, 30]))

# ===== CHALLENGE 2: Input Validation / اعتبارسنجی ورودی =====
print("\n" + "=" * 50)
print("CHALLENGE 2: Input Validation")
print("=" * 50)

class ValidationError(Exception):
    """Custom validation error / خطای اعتبارسنجی سفارشی"""
    pass

def validate_age(age):
    """
    Validate age / اعتبارسنجی سن
    Must be between 0 and 120
    Raise ValidationError for invalid input
    """
    # TODO: Implement age validation
    pass

def validate_email(email):
    """
    Validate email / اعتبارسنجی ایمیل
    Must contain @ and .
    Raise ValidationError for invalid input
    """
    # TODO: Implement email validation
    pass

def get_user_input():
    """Get user input with validation / دریافت ورودی کاربر با اعتبارسنجی"""
    # TODO: Implement user input with validation
    pass

# Test / تست
# try:
#     validate_age(25)   # Valid
#     validate_age(-5)   # Raises ValidationError
# except ValidationError as e:
#     print(f"Error: {e}")

# ===== CHALLENGE 3: Retry Logic / منطق تکرار =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Retry Logic")
print("=" * 50)

import time

def retry_on_error(func, max_retries=3, delay=1):
    """
    Retry function on error / تکرار تابع در صورت خطا
    """
    # TODO: Implement retry logic
    pass

def unstable_operation():
    """Simulates an operation that sometimes fails / شبیه‌سازی عملیاتی که گاهی خطا می‌دهد"""
    # TODO: Create function that fails randomly
    pass

# Test / تست
# result = retry_on_error(unstable_operation, max_retries=5)
# print(f"Result: {result}")
