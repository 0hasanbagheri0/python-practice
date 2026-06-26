"""
Day 2: Conditional Statements / ساختارهای شرطی
-----------------------------------------------
Learning objectives / اهداف یادگیری:
- Using if, elif, else statements / استفاده از دستورات شرطی
- Comparison operators / عملگرهای مقایسه‌ای
- Logical operators / عملگرهای منطقی
- Nested conditions / شرط‌های تو در تو
"""

# Simple if statement / دستور شرطی ساده
age = 18

if age >= 18:
    print("You are eligible to vote / شما می‌توانید رای دهید")
else:
    print("You are not eligible to vote / شما نمی‌توانید رای دهید")

# if-elif-else / شرط چندگانه
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Comparison operators / عملگرهای مقایسه‌ای
x, y = 10, 20
print(f"x={x}, y={y}")
print(f"x == y: {x == y}")  # Equal / مساوی
print(f"x != y: {x != y}")  # Not equal / نامساوی
print(f"x < y: {x < y}")    # Less than / کوچکتر
print(f"x > y: {x > y}")    # Greater than / بزرگتر
print(f"x <= y: {x <= y}")  # Less than or equal / کوچکتر یا مساوی
print(f"x >= y: {x >= y}")  # Greater than or equal / بزرگتر یا مساوی

# Logical operators / عملگرهای منطقی
is_weekend = True
is_sunny = False

# AND - both must be True / هر دو باید درست باشند
can_go_out = is_weekend and is_sunny
print(f"Can go out (AND): {can_go_out}")

# OR - at least one must be True / حداقل یکی باید درست باشد
can_go_out = is_weekend or is_sunny
print(f"Can go out (OR): {can_go_out}")

# NOT - reverses the value / مقدار را معکوس می‌کند
can_go_out = not is_weekend
print(f"Can go out (NOT): {can_go_out}")

# Nested conditions / شرط‌های تو در تو
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive / می‌توانید رانندگی کنید")
    else:
        print("You need a license / نیاز به گواهینامه دارید")
else:
    print("You are too young to drive / برای رانندگی خیلی جوان هستید")

# Ternary operator / عملگر سه‌تایی (شرطی یک خطی)
result = "Adult" if age >= 18 else "Minor"
print(f"Result: {result}")

# Membership check with 'in' / بررسی عضویت با 'in'
fruits = ["apple", "banana", "orange"]
fruit = "banana"

if fruit in fruits:
    print(f"{fruit} is in the list / در لیست وجود دارد")
else:
    print(f"{fruit} is not in the list / در لیست وجود ندارد")
