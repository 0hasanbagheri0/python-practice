"""
Queue Data Structure / ساختار داده صف (Queue)
-----------------------------------------------
FIFO (First In, First Out) - اولین ورودی، اولین خروجی

Operations / عملیات:
- enqueue: Add item to back / اضافه کردن به انتهای صف
- dequeue: Remove and return front item / حذف و بازگشت آیتم جلویی
- front: View front item without removing / مشاهده آیتم جلویی بدون حذف
- is_empty: Check if queue is empty / بررسی خالی بودن صف
- size: Get number of items / دریافت تعداد آیتم‌ها
"""

class Queue:
    """
    Queue implementation using Python list
    پیاده‌سازی صف با استفاده از لیست پایتون
    """
    
    def __init__(self):
        """Initialize empty queue / مقداردهی اولیه صف خالی"""
        self._items = []
    
    def enqueue(self, item):
        """
        Add item to back of queue / افزودن آیتم به انتهای صف
        
        Args:
            item: Item to add / آیتم مورد نظر
        """
        self._items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        """
        Remove and return front item / حذف و بازگشت آیتم جلویی
        
        Returns:
            Front item / آیتم جلویی
            
        Raises:
            IndexError: If queue is empty / اگر صف خالی باشد
        """
        if self.is_empty():
            raise IndexError("Queue is empty! Cannot dequeue.")
        return self._items.pop(0)
    
    def front(self):
        """
        View front item without removing / مشاهده آیتم جلویی بدون حذف
        
        Returns:
            Front item / آیتم جلویی
            
        Raises:
            IndexError: If queue is empty / اگر صف خالی باشد
        """
        if self.is_empty():
            raise IndexError("Queue is empty! Cannot view front.")
        return self._items[0]
    
    def is_empty(self):
        """
        Check if queue is empty / بررسی خالی بودن صف
        
        Returns:
            bool: True if empty, False otherwise
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get number of items in queue / دریافت تعداد آیتم‌های صف
        
        Returns:
            int: Number of items / تعداد آیتم‌ها
        """
        return len(self._items)
    
    def clear(self):
        """Clear all items / پاک کردن همه آیتم‌ها"""
        self._items.clear()
        print("Queue cleared!")
    
    def __str__(self):
        """String representation / نمایش به صورت رشته"""
        return f"Queue({self._items})"
    
    def __len__(self):
        """Support len() function / پشتیبانی از تابع len()"""
        return self.size()


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("QUEUE DEMO / نمایش صف")
    print("=" * 50)
    
    # Create queue / ایجاد صف
    queue = Queue()
    
    # Enqueue items / افزودن آیتم‌ها
    print("\n--- Enqueuing items ---")
    queue.enqueue("Task 1")
    queue.enqueue("Task 2")
    queue.enqueue("Task 3")
    queue.enqueue("Task 4")
    
    print(f"Queue: {queue}")
    print(f"Size: {queue.size()}")
    print(f"Is empty? {queue.is_empty()}")
    
    # Front / مشاهده جلویی
    print(f"\n--- Front ---")
    print(f"Front item: {queue.front()}")
    
    # Dequeue items / حذف آیتم‌ها
    print("\n--- Dequeuing items ---")
    while not queue.is_empty():
        dequeued = queue.dequeue()
        print(f"Dequeued: {dequeued}")
        print(f"Remaining: {queue}")
    
    # Error handling / مدیریت خطا
    print("\n--- Error handling ---")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error: {e}")
    
    # Example: Print Queue (Printer) / مثال: صف چاپ
    print("\n" + "=" * 50)
    print("PRINTER QUEUE EXAMPLE / مثال صف چاپ")
    print("=" * 50)
    
    printer_queue = Queue()
    
    # Add print jobs / اضافه کردن کارهای چاپ
    print("\n--- Adding print jobs ---")
    printer_queue.enqueue("Document1.pdf")
    printer_queue.enqueue("Document2.docx")
    printer_queue.enqueue("Image.png")
    printer_queue.enqueue("Report.xlsx")
    
    print(f"\nPrint queue: {printer_queue}")
    
    # Process print jobs / پردازش کارهای چاپ
    print("\n--- Processing print jobs ---")
    while not printer_queue.is_empty():
        job = printer_queue.dequeue()
        print(f"Printing: {job}...")
        import time
        time.sleep(0.5)  # Simulate printing / شبیه‌سازی چاپ
        print(f"✓ {job} printed successfully!")
    
    print("\nAll print jobs completed!")
