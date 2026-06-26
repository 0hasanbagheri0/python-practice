"""
Stack Data Structure / ساختار داده پشته (Stack)
-----------------------------------------------
LIFO (Last In, First Out) - آخرین ورودی، اولین خروجی

Operations / عملیات:
- push: Add item to top / اضافه کردن به بالای پشته
- pop: Remove and return top item / حذف و بازگشت آیتم بالایی
- peek: View top item without removing / مشاهده آیتم بالایی بدون حذف
- is_empty: Check if stack is empty / بررسی خالی بودن پشته
- size: Get number of items / دریافت تعداد آیتم‌ها
"""

class Stack:
    """
    Stack implementation using Python list
    پیاده‌سازی پشته با استفاده از لیست پایتون
    """
    
    def __init__(self):
        """Initialize empty stack / مقداردهی اولیه پشته خالی"""
        self._items = []
    
    def push(self, item):
        """
        Add item to top of stack / افزودن آیتم به بالای پشته
        
        Args:
            item: Item to add / آیتم مورد نظر
        """
        self._items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        """
        Remove and return top item / حذف و بازگشت آیتم بالایی
        
        Returns:
            Top item / آیتم بالایی
            
        Raises:
            IndexError: If stack is empty / اگر پشته خالی باشد
        """
        if self.is_empty():
            raise IndexError("Stack is empty! Cannot pop.")
        return self._items.pop()
    
    def peek(self):
        """
        View top item without removing / مشاهده آیتم بالایی بدون حذف
        
        Returns:
            Top item / آیتم بالایی
            
        Raises:
            IndexError: If stack is empty / اگر پشته خالی باشد
        """
        if self.is_empty():
            raise IndexError("Stack is empty! Cannot peek.")
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if stack is empty / بررسی خالی بودن پشته
        
        Returns:
            bool: True if empty, False otherwise
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get number of items in stack / دریافت تعداد آیتم‌های پشته
        
        Returns:
            int: Number of items / تعداد آیتم‌ها
        """
        return len(self._items)
    
    def clear(self):
        """Clear all items / پاک کردن همه آیتم‌ها"""
        self._items.clear()
        print("Stack cleared!")
    
    def __str__(self):
        """String representation / نمایش به صورت رشته"""
        return f"Stack({self._items})"
    
    def __len__(self):
        """Support len() function / پشتیبانی از تابع len()"""
        return self.size()


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("STACK DEMO / نمایش پشته")
    print("=" * 50)
    
    # Create stack / ایجاد پشته
    stack = Stack()
    
    # Push items / افزودن آیتم‌ها
    print("\n--- Pushing items ---")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Is empty? {stack.is_empty()}")
    
    # Peek / مشاهده بالایی
    print(f"\n--- Peek ---")
    print(f"Top item: {stack.peek()}")
    
    # Pop items / حذف آیتم‌ها
    print("\n--- Popping items ---")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped}")
        print(f"Remaining: {stack}")
    
    # Error handling / مدیریت خطا
    print("\n--- Error handling ---")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")
    
    # Example: Undo functionality / مثال: قابلیت Undo
    print("\n" + "=" * 50)
    print("UNDO EXAMPLE / مثال قابلیت Undo")
    print("=" * 50)
    
    undo_stack = Stack()
    actions = []
    
    def do_action(action):
        """Perform an action and save for undo / انجام عملیات و ذخیره برای Undo"""
        actions.append(action)
        undo_stack.push(action)
        print(f"Action done: {action}")
    
    def undo():
        """Undo last action / لغو آخرین عملیات"""
        if undo_stack.is_empty():
            print("Nothing to undo!")
            return
        action = undo_stack.pop()
        actions.remove(action)
        print(f"Undone: {action}")
    
    do_action("Add item X")
    do_action("Edit item Y")
    do_action("Delete item Z")
    
    print(f"\nAll actions: {actions}")
    print(f"Undo stack: {undo_stack}")
    
    undo()
    undo()
    
    print(f"\nAfter undo: {actions}")
