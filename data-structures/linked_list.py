"""
Linked List Data Structure / ساختار داده لیست پیوندی
-----------------------------------------------------
A linear collection of nodes, where each node contains data and reference to next node
مجموعه‌ای خطی از گره‌ها که هر گره شامل داده و ارجاع به گره بعدی است

Operations / عملیات:
- append: Add to end / افزودن به انتها
- prepend: Add to beginning / افزودن به ابتدا
- insert: Insert at index / درج در ایندکس مشخص
- remove: Remove by value / حذف بر اساس مقدار
- search: Find by value / جستجو بر اساس مقدار
- reverse: Reverse the list / معکوس کردن لیست
"""

class Node:
    """
    Node class for linked list / کلاس گره برای لیست پیوندی
    """
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    Singly Linked List implementation / پیاده‌سازی لیست پیوندی ساده
    """
    
    def __init__(self):
        """Initialize empty linked list / مقداردهی اولیه لیست خالی"""
        self.head = None
        self._size = 0
    
    def append(self, data):
        """
        Add item to end of list / افزودن آیتم به انتهای لیست
        
        Args:
            data: Data to add / داده مورد نظر
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self._size += 1
        print(f"Appended: {data}")
    
    def prepend(self, data):
        """
        Add item to beginning of list / افزودن آیتم به ابتدای لیست
        
        Args:
            data: Data to add / داده مورد نظر
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        print(f"Prepended: {data}")
    
    def insert(self, data, index):
        """
        Insert data at specific index / درج داده در ایندکس مشخص
        
        Args:
            data: Data to insert / داده مورد نظر
            index: Position to insert / موقعیت درج
            
        Raises:
            IndexError: If index is out of bounds / اگر ایندکس خارج از محدوده باشد
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of bounds (size: {self._size})")
        
        if index == 0:
            self.prepend(data)
            return
        
        if index == self._size:
            self.append(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
        print(f"Inserted: {data} at index {index}")
    
    def remove(self, data):
        """
        Remove first occurrence of data / حذف اولین وقوع داده
        
        Args:
            data: Data to remove / داده مورد نظر
            
        Returns:
            bool: True if removed, False if not found / در صورت حذف True و در غیر این صورت False
        """
        if self.head is None:
            return False
        
        # If head is the target / اگر سر همان هدف باشد
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            print(f"Removed: {data}")
            return True
        
        # Search in rest of list / جستجو در بقیه لیست
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next is None:
            print(f"Data {data} not found!")
            return False
        
        current.next = current.next.next
        self._size -= 1
        print(f"Removed: {data}")
        return True
    
    def search(self, data):
        """
        Search for data in list / جستجوی داده در لیست
        
        Args:
            data: Data to search / داده مورد نظر
            
        Returns:
            int: Index of first occurrence, -1 if not found / ایندکس اولین وقوع، -1 در صورت عدم وجود
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, index):
        """
        Get data at specific index / دریافت داده در ایندکس مشخص
        
        Args:
            index: Index to get / ایندکس مورد نظر
            
        Returns:
            Data at index / داده در ایندکس
            
        Raises:
            IndexError: If index is out of bounds / اگر ایندکس خارج از محدوده باشد
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds (size: {self._size})")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """
        Reverse the linked list / معکوس کردن لیست پیوندی
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        print("List reversed!")
    
    def is_empty(self):
        """
        Check if list is empty / بررسی خالی بودن لیست
        
        Returns:
            bool: True if empty, False otherwise
        """
        return self.head is None
    
    def size(self):
        """
        Get number of nodes in list / دریافت تعداد گره‌های لیست
        
        Returns:
            int: Number of nodes / تعداد گره‌ها
        """
        return self._size
    
    def clear(self):
        """Clear all nodes / پاک کردن همه گره‌ها"""
        self.head = None
        self._size = 0
        print("List cleared!")
    
    def to_list(self):
        """
        Convert linked list to Python list / تبدیل لیست پیوندی به لیست پایتون
        
        Returns:
            list: List of all data / لیست همه داده‌ها
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        """String representation / نمایش به صورت رشته"""
        if self.head is None:
            return "LinkedList(empty)"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        return f"LinkedList({' -> '.join(result)})"
    
    def __len__(self):
        """Support len() function / پشتیبانی از تابع len()"""
        return self._size
    
    def __iter__(self):
        """Make linked list iterable / قابل پیمایش کردن لیست پیوندی"""
        current = self.head
        while current:
            yield current.data
            current = current.next


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("LINKED LIST DEMO / نمایش لیست پیوندی")
    print("=" * 50)
    
    # Create linked list / ایجاد لیست پیوندی
    ll = LinkedList()
    
    # Append items / افزودن به انتها
    print("\n--- Appending items ---")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    print(f"List: {ll}")
    print(f"Size: {len(ll)}")
    
    # Prepend items / افزودن به ابتدا
    print("\n--- Prepending items ---")
    ll.prepend(5)
    ll.prepend(1)
    print(f"List: {ll}")
    
    # Insert at index / درج در ایندکس
    print("\n--- Inserting at index ---")
    ll.insert(15, 3)
    print(f"List: {ll}")
    
    # Remove items / حذف آیتم‌ها
    print("\n--- Removing items ---")
    ll.remove(20)
    print(f"List: {ll}")
    
    # Search / جستجو
    print("\n--- Searching ---")
    index = ll.search(30)
    print(f"Index of 30: {index}")
    index = ll.search(100)
    print(f"Index of 100: {index}")
    
    # Get by index / دریافت با ایندکس
    print("\n--- Get by index ---")
    print(f"Element at index 2: {ll.get(2)}")
    
    # Reverse / معکوس کردن
    print("\n--- Reverse ---")
    ll.reverse()
    print(f"List after reverse: {ll}")
    
    # Convert to list / تبدیل به لیست
    print(f"\nAs Python list: {ll.to_list()}")
    
    # Iterate / پیمایش
    print("\n--- Iterating ---")
    for item in ll:
        print(f"Item: {item}")
    
    # List with strings / لیست با رشته‌ها
    print("\n" + "=" * 50)
    print("STRING LIST EXAMPLE / مثال لیست رشته‌ها")
    print("=" * 50)
    
    names = LinkedList()
    names.append("Alice")
    names.append("Bob")
    names.append("Charlie")
    names.append("Diana")
    
    print(f"Names: {names}")
    
    # Search for name / جستجوی نام
    print(f"\nIs 'Charlie' in list? {'Yes' if names.search('Charlie') != -1 else 'No'}")
