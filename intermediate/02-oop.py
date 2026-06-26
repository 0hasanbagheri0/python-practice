"""
Object-Oriented Programming in Python / برنامه‌نویسی شی‌گرا در پایتون
--------------------------------------------------------------------
Learning objectives / اهداف یادگیری:
- Classes and objects / کلاس‌ها و اشیاء
- Constructor (__init__) / سازنده
- Methods and attributes / متدها و ویژگی‌ها
- Inheritance / وراثت
- Encapsulation / کپسوله‌سازی
- Polymorphism / چندشکلی
"""

# === BASIC CLASS / کلاس پایه ===
print("=" * 50)
print("BASIC CLASS / کلاس پایه")
print("=" * 50)

class Person:
    """A simple Person class / یک کلاس ساده شخص"""
    
    def __init__(self, name, age):
        """Constructor / سازنده"""
        self.name = name
        self.age = age
        self.greetings = 0
    
    def introduce(self):
        """Introduce the person / معرفی شخص"""
        self.greetings += 1
        return f"Hello, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Increase age by 1 / افزایش سن به مقدار ۱"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}!"

# Create objects / ایجاد اشیاء
person1 = Person("Hasan", 25)
person2 = Person("Sara", 22)

print(person1.introduce())
print(person2.introduce())
print(person1.have_birthday())
print(f"Greetings count: {person1.greetings}")

# === INHERITANCE / وراثت ===
print("\n" + "=" * 50)
print("INHERITANCE / وراثت")
print("=" * 50)

class Student(Person):
    """Student class inheriting from Person / کلاس دانشجو که از Person ارث‌بری می‌کند"""
    
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
        self.courses = []
    
    def enroll(self, course):
        """Enroll in a course / ثبت‌نام در یک دوره"""
        self.courses.append(course)
        return f"{self.name} enrolled in {course}."
    
    def introduce(self):
        """Overridden method / متد بازنویسی شده"""
        return f"Hello, I'm {self.name}, a {self.major} student (ID: {self.student_id})."

# Create student object / ایجاد شیء دانشجو
student1 = Student("Ali", 20, "2024001", "Computer Science")
print(student1.introduce())
print(student1.enroll("Python Programming"))
print(student1.enroll("Data Science"))
print(f"Courses: {student1.courses}")

# === ENCAPSULATION / کپسوله‌سازی ===
print("\n" + "=" * 50)
print("ENCAPSULATION / کپسوله‌سازی")
print("=" * 50)

class BankAccount:
    """Bank account with encapsulation / حساب بانکی با کپسوله‌سازی"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute / ویژگی خصوصی
        self.__transactions = []  # Private list / لیست خصوصی
    
    def deposit(self, amount):
        """Deposit money / واریز پول"""
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"+${amount}")
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount!"
    
    def withdraw(self, amount):
        """Withdraw money / برداشت پول"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"-${amount}")
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient balance or invalid amount!"
    
    def get_balance(self):
        """Get balance (getter) / دریافت موجودی"""
        return self.__balance
    
    def get_transactions(self):
        """Get transaction history / دریافت تاریخچه تراکنش‌ها"""
        return self.__transactions

# Create account / ایجاد حساب
account = BankAccount("Hasan", 1000)
print(f"Initial balance / موجودی اولیه: ${account.get_balance()}")

print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))  # Insufficient balance / موجودی ناکافی

print(f"Transaction history / تاریخچه تراکنش‌ها: {account.get_transactions()}")

# === POLYMORPHISM / چندشکلی ===
print("\n" + "=" * 50)
print("POLYMORPHISM / چندشکلی")
print("=" * 50)

class Animal:
    """Base animal class / کلاس پایه حیوان"""
    
    def sound(self):
        """Make sound / صدا درآوردن"""
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo! Moo!"

# Polymorphism in action / چندشکلی در عمل
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.sound()}")

# === DUNDER METHODS / متدهای ویژه (DUNDER) ===
print("\n" + "=" * 50)
print("DUNDER METHODS / متدهای ویژه")
print("=" * 50)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation / نمایش به صورت رشته"""
        return f"'{self.title}' by {self.author} ({self.pages} pages)"
    
    def __repr__(self):
        """Representation for developers / نمایش برای توسعه‌دهندگان"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of the book / تعداد صفحات کتاب"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison / مقایسه برابری"""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

# Using dunder methods / استفاده از متدهای ویژه
book1 = Book("Clean Code", "Robert C. Martin", 464)
book2 = Book("Python Crash Course", "Eric Matthes", 544)

print(f"str: {book1}")
print(f"repr: {repr(book1)}")
print(f"Length of book1: {len(book1)}")

# Check equality / بررسی برابری
book3 = Book("Clean Code", "Robert C. Martin", 464)
print(f"book1 == book3: {book1 == book3}")
