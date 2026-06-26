"""
Day 2 Challenge: Conditions and Loops / چالش روز ۲: شرط و حلقه
--------------------------------------------------------------
Practice: If statements, loops, and flow control
تمرین: دستورات شرطی، حلقه‌ها و کنترل جریان
"""

# ===== CHALLENGE 1: FizzBuzz =====
print("=" * 50)
print("CHALLENGE 1: FizzBuzz")
print("=" * 50)

def fizzbuzz(n):
    """
    FizzBuzz challenge / چالش FizzBuzz
    - Print numbers 1 to n
    - For multiples of 3, print "Fizz"
    - For multiples of 5, print "Buzz"
    - For multiples of both 3 and 5, print "FizzBuzz"
    """
    # TODO: Implement FizzBuzz
    pass

# Test: fizzbuzz(15)

# ===== CHALLENGE 2: Prime Number Checker / بررسی عدد اول =====
print("\n" + "=" * 50)
print("CHALLENGE 2: Prime Number Checker")
print("=" * 50)

def is_prime(n):
    """
    Check if a number is prime / بررسی اول بودن عدد
    A prime number is only divisible by 1 and itself
    """
    # TODO: Implement prime checking
    pass

def find_primes(limit):
    """
    Find all prime numbers up to limit / پیدا کردن اعداد اول تا محدوده
    """
    # TODO: Implement prime finder
    pass

# Test / تست
# print(is_prime(7))   # True
# print(is_prime(10))  # False
# print(find_primes(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# ===== CHALLENGE 3: Number Guessing Game / بازی حدس عدد =====
print("\n" + "=" * 50)
print("CHALLENGE 3: Number Guessing Game")
print("=" * 50)

import random

def guess_the_number():
    """
    Number guessing game / بازی حدس عدد
    - Computer picks a random number between 1-100
    - User has to guess it
    - Give hints: Too high / Too low
    """
    # TODO: Implement guessing game
    pass

# Uncomment to play / برای بازی کردن کامنت را بردارید
# guess_the_number()
