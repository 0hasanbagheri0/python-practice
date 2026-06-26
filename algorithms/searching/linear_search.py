"""
Linear Search Algorithm / الگوریتم جستجوی خطی
---------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)

Linear search checks each element sequentially until finding the target.
جستجوی خطی هر عنصر را به ترتیب بررسی می‌کند تا هدف را پیدا کند.
"""

def linear_search(arr, target):
    """
    Search for target in array using linear search
    جستجوی هدف در آرایه با استفاده از جستجوی خطی
    
    Args:
        arr: List of elements / لیستی از عناصر
        target: Element to find / عنصر مورد جستجو
    
    Returns:
        int: Index of target, -1 if not found / ایندکس هدف، -1 در صورت عدم وجود
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def linear_search_all(arr, target):
    """
    Find all occurrences of target / پیدا کردن همه وقوع‌های هدف
    
    Args:
        arr: List of elements / لیستی از عناصر
        target: Element to find / عنصر مورد جستجو
    
    Returns:
        list: List of all indices where target appears / لیست همه ایندکس‌هایی که هدف در آنها ظاهر شده
    """
    indices = []
    for i, element in enumerate(arr):
        if element == target:
            indices.append(i)
    return indices

def linear_search_with_key(arr, target, key=None):
    """
    Search with custom key function / جستجو با تابع کلید سفارشی
    
    Args:
        arr: List of elements / لیستی از عناصر
        target: Target value / مقدار هدف
        key: Function to extract comparison value / تابع برای استخراج مقدار مقایسه
    
    Returns:
        int: Index of target, -1 if not found / ایندکس هدف، -1 در صورت عدم وجود
    """
    if key is None:
        key = lambda x: x
    
    for i, element in enumerate(arr):
        if key(element) == target:
            return i
    return -1

def linear_search_with_sentinel(arr, target):
    """
    Linear search with sentinel (faster) / جستجوی خطی با سنتینل (سریع‌تر)
    Adds target to end of list to avoid boundary check
    هدف را به انتهای لیست اضافه می‌کند تا از بررسی مرز جلوگیری کند
    
    Args:
        arr: List of elements / لیستی از عناصر
        target: Element to find / عنصر مورد جستجو
    
    Returns:
        int: Index of target, -1 if not found / ایندکس هدف، -1 در صورت عدم وجود
    """
    # Create a copy with sentinel / ایجاد کپی با سنتینل
    arr_copy = arr.copy()
    arr_copy.append(target)
    
    i = 0
    while arr_copy[i] != target:
        i += 1
    
    # If i is the sentinel position, target not found
    if i == len(arr):
        return -1
    return i


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("LINEAR SEARCH DEMO / نمایش جستجوی خطی")
    print("=" * 50)
    
    # Test data / داده‌های تست
    numbers = [10, 23, 45, 70, 11, 15, 23, 50, 23, 90]
    print(f"Array: {numbers}")
    
    # Basic search / جستجوی پایه
    print("\n--- Basic Search ---")
    target = 23
    result = linear_search(numbers, target)
    print(f"Searching for {target}: Index {result}")
    
    target = 100
    result = linear_search(numbers, target)
    print(f"Searching for {target}: Index {result}")
    
    # Find all occurrences / پیدا کردن همه وقوع‌ها
    print("\n--- Find All Occurrences ---")
    target = 23
    indices = linear_search_all(numbers, target)
    print(f"All indices of {target}: {indices}")
    
    # Search with custom key / جستجو با کلید سفارشی
    print("\n--- Search with Custom Key ---")
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35},
        {"name": "Diana", "age": 28}
    ]
    
    target_age = 35
    result = linear_search_with_key(data, target_age, key=lambda x: x["age"])
    print(f"Person with age {target_age}: {data[result] if result != -1 else 'Not found'}")
    
    # Search with sentinel / جستجو با سنتینل
    print("\n--- Search with Sentinel ---")
    target = 50
    result = linear_search_with_sentinel(numbers, target)
    print(f"Searching for {target} with sentinel: Index {result}")
    
    # Performance comparison / مقایسه عملکرد
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON / مقایسه عملکرد")
    print("=" * 50)
    
    import time
    large_data = list(range(1000000))
    target = 999999
    
    # Regular linear search / جستجوی خطی معمولی
    start = time.time()
    result = linear_search(large_data, target)
    end = time.time()
    print(f"Regular linear search: {end - start:.6f} seconds")
    
    # Sentinel linear search / جستجوی خطی با سنتینل
    start = time.time()
    result = linear_search_with_sentinel(large_data, target)
    end = time.time()
    print(f"Sentinel linear search: {end - start:.6f} seconds")
