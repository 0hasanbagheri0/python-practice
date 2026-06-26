"""
Binary Search Algorithm / الگوریتم جستجوی دودویی
------------------------------------------------
Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive

Binary search works on sorted arrays by repeatedly dividing the search interval in half.
جستجوی دودویی روی آرایه‌های مرتب‌شده کار می‌کند و بازه جستجو را به نصف تقسیم می‌کند.
"""

def binary_search_iterative(arr, target):
    """
    Binary search using iterative approach / جستجوی دودویی با روش تکرار
    (Iterative) / (تکراری)
    
    Args:
        arr: Sorted list / لیست مرتب‌شده
        target: Element to find / عنصر مورد جستجو
    
    Returns:
        int: Index of target, -1 if not found / ایندکس هدف، -1 در صورت عدم وجود
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=None, right=None):
    """
    Binary search using recursive approach / جستجوی دودویی با روش بازگشتی
    (Recursive) / (بازگشتی)
    
    Args:
        arr: Sorted list / لیست مرتب‌شده
        target: Element to find / عنصر مورد جستجو
        left: Left boundary (optional) / مرز چپ (اختیاری)
        right: Right boundary (optional) / مرز راست (اختیاری)
    
    Returns:
        int: Index of target, -1 if not found / ایندکس هدف، -1 در صورت عدم وجود
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def binary_search_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array (with duplicates)
    پیدا کردن اولین وقوع هدف در آرایه مرتب (با تکراری‌ها)
    
    Args:
        arr: Sorted list / لیست مرتب‌شده
        target: Element to find / عنصر مورد جستجو
    
    Returns:
        int: First index of target, -1 if not found / اولین ایندکس هدف، -1 در صورت عدم وجود
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left / ادامه جستجو در چپ
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_last_occurrence(arr, target):
    """
    Find last occurrence of target in sorted array (with duplicates)
    پیدا کردن آخرین وقوع هدف در آرایه مرتب (با تکراری‌ها)
    
    Args:
        arr: Sorted list / لیست مرتب‌شده
        target: Element to find / عنصر مورد جستجو
    
    Returns:
        int: Last index of target, -1 if not found / آخرین ایندکس هدف، -1 در صورت عدم وجود
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right / ادامه جستجو در راست
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_range(arr, target, find_first=True):
    """
    Generic binary search for first or last occurrence
    جستجوی دودویی عمومی برای اولین یا آخرین وقوع
    
    Args:
        arr: Sorted list / لیست مرتب‌شده
        target: Element to find / عنصر مورد جستجو
        find_first: True for first, False for last / True برای اولین، False برای آخرین
    
    Returns:
        int: Index of target, -1 if not found / ایندکس هدف، -1 در صورت عدم وجود
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("BINARY SEARCH DEMO / نمایش جستجوی دودویی")
    print("=" * 50)
    
    # Test data (sorted) / داده‌های تست (مرتب‌شده)
    numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(f"Array: {numbers}")
    
    # Iterative binary search / جستجوی دودویی تکراری
    print("\n--- Iterative Binary Search ---")
    target = 15
    result = binary_search_iterative(numbers, target)
    print(f"Searching for {target}: Index {result}")
    
    target = 100
    result = binary_search_iterative(numbers, target)
    print(f"Searching for {target}: Index {result}")
    
    # Recursive binary search / جستجوی دودویی بازگشتی
    print("\n--- Recursive Binary Search ---")
    target = 18
    result = binary_search_recursive(numbers, target)
    print(f"Searching for {target}: Index {result}")
    
    # Search with duplicates / جستجو با تکراری‌ها
    print("\n" + "=" * 50)
    print("SEARCH WITH DUPLICATES / جستجو با تکراری‌ها")
    print("=" * 50)
    
    duplicates = [1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9]
    print(f"Array with duplicates: {duplicates}")
    
    target = 3
    first = binary_search_first_occurrence(duplicates, target)
    last = binary_search_last_occurrence(duplicates, target)
    print(f"Target {target}: First at {first}, Last at {last}")
    
    target = 8
    first = binary_search_range(duplicates, target, find_first=True)
    last = binary_search_range(duplicates, target, find_first=False)
    print(f"Target {target}: First at {first}, Last at {last}")
    
    target = 5
    first = binary_search_range(duplicates, target, find_first=True)
    last = binary_search_range(duplicates, target, find_first=False)
    print(f"Target {target}: First at {first}, Last at {last}")
    
    # Performance comparison / مقایسه عملکرد
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON / مقایسه عملکرد")
    print("=" * 50)
    
    import time
    
    large_data = list(range(1000000))
    target = 999999
    
    # Linear search / جستجوی خطی
    start = time.time()
    for i, val in enumerate(large_data):
        if val == target:
            break
    linear_time = time.time() - start
    print(f"Linear search: {linear_time:.6f} seconds")
    
    # Binary search / جستجوی دودویی
    start = time.time()
    result = binary_search_iterative(large_data, target)
    binary_time = time.time() - start
    print(f"Binary search: {binary_time:.6f} seconds")
    
    print(f"\nBinary search is {(linear_time / binary_time):.2f}x faster!")
