"""
Error Handling in Python / مدیریت خطا در پایتون
-----------------------------------------------
Learning objectives / اهداف یادگیری:
- Understanding exceptions / درک استثناها
- try-except blocks / بلوک‌های try-except
- Multiple exception handling / مدیریت چندین استثنا
- Finally clause / عبارت finally
- Raising exceptions / ایجاد استثنا
- Custom exceptions / استثناهای سفارشی
"""

import sys
import traceback

# === BASIC EXCEPTION HANDLING / مدیریت خطای پایه ===
print("=" * 60)
print("BASIC EXCEPTION HANDLING / مدیریت خطای پایه")
print("=" * 60)

def divide_numbers(a, b):
    """
    Divide two numbers with error handling
    تقسیم دو عدد با مدیریت خطا
    """
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print(f"❌ Error: Cannot divide {a} by zero!")
        return None
    except TypeError:
        print(f"❌ Error: Both arguments must be numbers!")
        return None

# Test cases / موارد تست
print("\n--- Test Cases ---")
divide_numbers(10, 2)      # Valid / معتبر
divide_numbers(10, 0)      # Zero division / تقسیم بر صفر
divide_numbers(10, "2")    # Type error / خطای نوع
divide_numbers("10", 2)    # Type error / خطای نوع

# === HANDLING MULTIPLE EXCEPTIONS / مدیریت چندین استثنا ===
print("\n" + "=" * 60)
print("HANDLING MULTIPLE EXCEPTIONS / مدیریت چندین استثنا")
print("=" * 60)

def process_user_data(data):
    """
    Process user data with multiple exception handling
    پردازش داده‌های کاربر با مدیریت چندین استثنا
    """
    try:
        # Try to convert to int / تلاش برای تبدیل به عدد صحیح
        age = int(data)
        
        if age < 0:
            raise ValueError("Age cannot be negative!")
        
        print(f"User age: {age}")
        return age
    
    except ValueError as e:
        print(f"❌ ValueError: {e}")
        print("   Please enter a valid integer!")
    
    except TypeError as e:
        print(f"❌ TypeError: {e}")
        print("   Data must be a string or number!")

# Test cases / موارد تست
print("\n--- Test Cases ---")
process_user_data("25")       # Valid / معتبر
process_user_data("abc")      # Invalid / نامعتبر
process_user_data("-5")       # Negative / منفی
process_user_data(3.14)       # Float / اعشاری

# === USING FINALLY / استفاده از Finally ===
print("\n" + "=" * 60)
print("USING FINALLY / استفاده از Finally")
print("=" * 60)

def read_file(filename):
    """
    Read file with finally clause for cleanup
    خواندن فایل با عبارت finally برای پاک‌سازی
    """
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content: {content[:100]}...")  # Show first 100 chars
        return content
    
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        return None
    
    except PermissionError:
        print(f"❌ Error: Permission denied to read '{filename}'!")
        return None
    
    finally:
        if file:
            file.close()
            print("✓ File closed successfully!")
        else:
            print("No file was opened.")

# Test cases / موارد تست
print("\n--- Test Cases ---")
# read_file("existing_file.txt")   # If file exists / اگر فایل وجود داشته باشد
read_file("non_existent.txt")     # File not found / فایل پیدا نشد

# === CATCHING ALL EXCEPTIONS / گرفتن همه استثناها ===
print("\n" + "=" * 60)
print("CATCHING ALL EXCEPTIONS / گرفتن همه استثناها")
print("=" * 60)

def safe_execute(func, *args):
    """
    Execute a function safely with generic exception handling
    اجرای ایمن یک تابع با مدیریت استثنای عمومی
    """
    try:
        result = func(*args)
        print(f"✓ Function executed successfully!")
        print(f"  Result: {result}")
        return result
    
    except Exception as e:
        print(f"❌ An error occurred: {type(e).__name__}")
        print(f"   Message: {e}")
        print(f"   Details: {traceback.format_exc()}")
        return None

# Test cases / موارد تست
print("\n--- Test Cases ---")
safe_execute(divide_numbers, 10, 2)
safe_execute(divide_numbers, 10, 0)
safe_execute(lambda x: x[0], [])  # Index error / خطای ایندکس

# === RAISING EXCEPTIONS / ایجاد استثنا ===
print("\n" + "=" * 60)
print("RAISING EXCEPTIONS / ایجاد استثنا")
print("=" * 60)

class BankAccount:
    """
    Bank account with custom exceptions
    حساب بانکی با استثناهای سفارشی
    """
    
    class InsufficientFundsError(Exception):
        """Raised when trying to withdraw more than balance"""
        pass
    
    class InvalidAmountError(Exception):
        """Raised when amount is not positive"""
        pass
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """
        Deposit money / واریز پول
        
        Raises:
            InvalidAmountError: If amount is not positive
        """
        if amount <= 0:
            raise self.InvalidAmountError(f"Invalid amount: {amount}. Must be > 0!")
        
        self.balance += amount
        print(f"✓ Deposited ${amount} to {self.owner}'s account")
        print(f"  New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """
        Withdraw money / برداشت پول
        
        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If balance is insufficient
        """
        if amount <= 0:
            raise self.InvalidAmountError(f"Invalid amount: {amount}. Must be > 0!")
        
        if amount > self.balance:
            raise self.InsufficientFundsError(
                f"Insufficient funds! Balance: ${self.balance}, Withdrawal: ${amount}"
            )
        
        self.balance -= amount
        print(f"✓ Withdrew ${amount} from {self.owner}'s account")
        print(f"  New balance: ${self.balance}")

# Using the class with error handling / استفاده از کلاس با مدیریت خطا
print("\n--- Bank Account Demo ---")
account = BankAccount("Hasan", 1000)

try:
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  # This will raise an error / این خطا ایجاد می‌کند
    
except (BankAccount.InvalidAmountError, BankAccount.InsufficientFundsError) as e:
    print(f"❌ Transaction failed: {e}")

# === CUSTOM EXCEPTION / استثنای سفارشی ===
print("\n" + "=" * 60)
print("CUSTOM EXCEPTION / استثنای سفارشی")
print("=" * 60)

class ValidationError(Exception):
    """Custom exception for data validation"""
    def __init__(self, message, field=None, value=None):
        self.message = message
        self.field = field
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        if self.field:
            return f"ValidationError in '{self.field}': {self.message} (Value: {self.value})"
        return f"ValidationError: {self.message}"

def validate_user(name, age, email):
    """
    Validate user data with custom exception
    اعتبارسنجی داده‌های کاربر با استثنای سفارشی
    """
    if not name or len(name) < 2:
        raise ValidationError("Name must have at least 2 characters", "name", name)
    
    if not isinstance(age, int) or age < 0 or age > 150:
        raise ValidationError("Age must be between 0 and 150", "age", age)
    
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email format", "email", email)
    
    return {"name": name, "age": age, "email": email}

# Test validation / تست اعتبارسنجی
print("\n--- User Validation ---")

test_users = [
    ("Hasan", 25, "hasan@email.com"),    # Valid / معتبر
    ("A", 30, "ali@email.com"),          # Invalid name / نام نامعتبر
    ("Sara", -5, "sara@email.com"),      # Invalid age / سن نامعتبر
    ("Reza", 25, "reza-email.com"),      # Invalid email / ایمیل نامعتبر
]

for name, age, email in test_users:
    try:
        result = validate_user(name, age, email)
        print(f"✓ Valid user: {result}")
    
    except ValidationError as e:
        print(f"❌ {e}")

# === TRACE AND LOGGING / ردیابی و لاگ‌گیری ===
print("\n" + "=" * 60)
print("TRACE AND LOGGING / ردیابی و لاگ‌گیری")
print("=" * 60)

def divide_with_trace(a, b):
    """
    Division with detailed error logging
    تقسیم با لاگ‌گیری دقیق خطا
    """
    try:
        result = a / b
    
    except ZeroDivisionError:
        print(f"❌ Error dividing {a} by zero!")
        print(f"   Traceback:")
        traceback.print_exc(file=sys.stdout)
        return None
    
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}")
        print(f"   Message: {e}")
        return None
    
    else:
        print(f"✓ {a} / {b} = {result}")
        return result
    
    finally:
        print("   --- Operation completed ---")

print("\n--- Trace Demo ---")
divide_with_trace(10, 2)
divide_with_trace(10, 0)

# === SUMMARY / خلاصه ===
print("\n" + "=" * 60)
print("SUMMARY OF ERROR HANDLING / خلاصه مدیریت خطا")
print("=" * 60)

print("""
✅ try: Block where errors might occur / بلوکی که ممکن است خطا رخ دهد
✅ except: Catch specific exceptions / گرفتن استثناهای خاص
✅ else: Code to run if no exception occurred / کدی که در صورت عدم خطا اجرا شود
✅ finally: Code that always runs (cleanup) / کدی که همیشه اجرا می‌شود (پاک‌سازی)
✅ raise: Manually raise an exception / ایجاد دستی یک استثنا
✅ Custom exceptions: Create specific error types / ایجاد انواع خطای خاص
✅ Exception hierarchy: Understand the inheritance tree / درک درخت ارث‌بری
""")

print("\n📝 Key Takeaway / نکته کلیدی:")
print("  " + "The best error handling is the one that anticipates problems and")
print("  " + "provides clear, actionable error messages to the user.")
print("  " + "بهترین مدیریت خطا آن است که مشکلات را پیش‌بینی کند و پیام‌های")
print("  " + "روشن و قابل اجرا به کاربر ارائه دهد.")
