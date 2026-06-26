"""
Day 4 Challenge: Data Structures / چالش روز ۴: ساختارهای داده
-------------------------------------------------------------
Practice: Lists, tuples, dictionaries, sets
تمرین: لیست‌ها، تاپل‌ها، دیکشنری‌ها، مجموعه‌ها
"""

# ===== CHALLENGE 1: Student Grades / نمرات دانشجویان =====
print("=" * 50)
print("CHALLENGE 1: Student Grades")
print("=" * 50)

def add_grade(student_grades, student, grade):
    """Add grade for a student / اضافه کردن نمره برای دانشجو"""
    # TODO: Implement adding grade
    pass

def get_average(student_grades, student):
    """Get average grade for a student / دریافت میانگین نمرات دانشجو"""
    # TODO: Implement average calculation
    pass

def get_top_students(student_grades, n=3):
    """Get top n students by average / دریافت n دانشجوی برتر"""
    # TODO: Implement top students
    pass

# Test / تست
# grades = {}
# add_grade(grades, "Alice", 85)
# add_grade(grades, "Alice", 90)
# add_grade(grades, "Bob", 75)
# add_grade(grades, "Bob", 80)
# add_grade(grades, "Charlie", 95)
# print(get_average(grades, "Alice"))  # 87.5
# print(get_top_students(grades, 2))   # [("Charlie", 95), ("Alice", 87.5)]

# ===== CHALLENGE 2: Word Frequency / تعداد کلمات =====
print("\n" + "=" * 50)
print("CHALLENGE 2: Word Frequency")
print("=" * 50)

def word_frequency(text):
    """Count frequency of each word / شمارش تعداد هر کلمه"""
    # TODO: Implement word frequency
    # Hint: Use split() and dictionary
    pass

def most_common_words(text, n=3):
    """Get n most common words / دریافت n کلمه پرتکرار"""
    # TODO: Implement most common words
    pass

# Test / تست
# text = "hello world hello python world hello"
# print(word_frequency(text))
# # {'hello': 3, 'world': 2, 'python': 1}
# print(most_common_words(text, 2))  # [('hello', 3), ('world', 2)]

# ===== CHALLENGE 3: To-Do List / لیست کارها =====
print("\n" + "=" * 50)
print("CHALLENGE 3: To-Do List")
print("=" * 50)

class ToDoList:
    """Simple To-Do List / لیست کارهای ساده"""
    
    def __init__(self):
        self.tasks = []
        self.completed = []
    
    def add_task(self, task):
        """Add a new task / اضافه کردن کار جدید"""
        # TODO: Implement add task
        pass
    
    def complete_task(self, task_index):
        """Mark task as completed / علامت‌گذاری کار به عنوان انجام شده"""
        # TODO: Implement complete task
        pass
    
    def delete_task(self, task_index):
        """Delete a task / حذف کار"""
        # TODO: Implement delete task
        pass
    
    def show_tasks(self):
        """Show all tasks / نمایش همه کارها"""
        # TODO: Implement show tasks
        pass

# Test / تست
# todo = ToDoList()
# todo.add_task("Learn Python")
# todo.add_task("Practice Pandas")
# todo.add_task("Complete project")
# todo.show_tasks()
# todo.complete_task(0)
# todo.show_tasks()
