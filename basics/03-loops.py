"""
Day 3: Loops / حلقه‌ها
-----------------------------------------------
Learning objectives / اهداف یادگیری:
- Using for loops / استفاده از حلقه‌های for
- Using while loops / استفاده از حلقه‌های while
- Loop control: break, continue, pass / کنترل حلقه
- Nested loops / حلقه‌های تو در تو
"""

# For loop with range / حلقه for با range
print("Numbers 0 to 4:")

for i in range(5):
    print(i)

# For loop with start and stop / حلقه for با شروع و پایان
print("\nNumbers 5 to 9:")
for i in range(5, 10):
    print(i)

# For loop with step / حلقه for با گام
print("\nEven numbers 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# For loop through a list / حلقه for روی لیست
print("\nFruits:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)

# For loop with enumerate / حلقه for با شماره‌گذاری
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# For loop through a dictionary / حلقه for روی دیکشنری
print("\nPerson information:")
person = {
    "name": "Hasan",
    "age": 25,
    "city": "Tehran"
}

for key, value in person.items():
    print(f"{key}: {value}")

# While loop / حلقه while
print("\nCounting down:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off! 🚀")

# Break statement / دستور break (خروج از حلقه)
print("\nBreak at 5:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement / دستور continue (ادامه حلقه)
print("\nSkip even numbers:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Pass statement / دستور pass (هیچ کاری نکن)
print("\nPass example:")
for i in range(5):
    if i == 2:
        pass  # Do nothing / هیچ کاری نکن
    print(i)

# Nested loops / حلقه‌های تو در تو
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)

# List comprehension / کامپرهنشن لیست (ساخت لیست با حلقه)
squares = [x**2 for x in range(10)]
print(f"\nSquares: {squares}")

even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")
