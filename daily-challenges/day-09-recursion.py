"""
Day 9 Challenge: Recursion / چالش روز ۹: بازگشت
-----------------------------------------------
Practice: Recursive functions, base cases, recursion depth
تمرین: توابع بازگشتی، حالت‌های پایه، عمق بازگشت
"""

# ===== CHALLENGE 1: Sum of List / مجموع لیست =====
print("=" * 50)
print("CHALLENGE 1: Sum of List")
print("=" * 50)

def sum_recursive(numbers):
    """
    Calculate sum of list using recursion / محاسبه مجموع لیست با بازگشت
    Base case: empty list returns 0
    """
    # TODO: Implement recursive sum
    pass

# Test / تست
# numbers = [1, 2, 3, 4, 5]
# print(sum_recursive(numbers))  # 15

# ===== CHALLENGE 2: String Reversal / معکوس کردن رشته =====
print("\n" + "=" * 50)
print("CHALLENGE 2: String Reversal")
print("=" * 50)

def reverse_recursive(text):
    """
    Reverse string using recursion / معکوس کردن رشته با بازگشت
    Base case: empty string returns empty string
    """
    # TODO: Implement recursive string reversal
    pass

# Test / تست
# print(reverse_recursive("python"))  # "nohtyp"
# print(reverse_recursive("hello"))   # "olleh"

# ===== CHALLENGE 3: Power Function / تابع توان =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Power Function")
print("=" * 50)

def power_recursive(base, exponent):
    """
    Calculate power using recursion / محاسبه توان با بازگشت
    Base case: exponent 0 returns 1
    """
    # TODO: Implement recursive power
    pass

# Test / تست
# print(power_recursive(2, 3))   # 8
# print(power_recursive(5, 0))   # 1
# print(power_recursive(3, 4))   # 81

# ===== CHALLENGE 4: Counting Items in List / شمارش آیتم‌ها =====
print("\n" + "=" * 50)
print("CHALLENGE 4: Counting Items")
print("=" * 50)

def count_recursive(items, target):
    """
    Count occurrences of target in list using recursion
    شمارش وقوع هدف در لیست با بازگشت
    """
    # TODO: Implement recursive counting
    pass

# Test / تست
# items = [1, 2, 3, 2, 4, 2, 5]
# print(count_recursive(items, 2))  # 3
# print(count_recursive(items, 6))  # 0

# ===== CHALLENGE 5: Factorial (Review) / فاکتوریل (مرور) =====
print("\n" + "=" * 50)
print("CHALLENGE 5: Factorial")
print("=" * 50)

def factorial_recursive(n):
    """
    Calculate factorial using recursion / محاسبه فاکتوریل با بازگشت
    Base case: n <= 1 returns 1
    """
    # TODO: Implement recursive factorial
    pass

# Test / تست
# print(factorial_recursive(5))  # 120
# print(factorial_recursive(0))  # 1
# print(factorial_recursive(1))  # 1

# ===== BONUS: Fibonacci / فیبوناچی =====
print("\n" + "=" * 50)
print("BONUS: Fibonacci")
print("=" * 50)

def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursion
    محاسبه عدد فیبوناچی nام با بازگشت
    Base cases: n=0 -> 0, n=1 -> 1
    """
    # TODO: Implement recursive fibonacci
    pass

# Test / تست
# for i in range(10):
#     print(f"F({i}) = {fibonacci_recursive(i)}")
