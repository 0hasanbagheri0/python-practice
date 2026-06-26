"""
Quick Sort Algorithm / الگوریتم مرتب‌سازی سریع
---------------------------------------------
Time Complexity: O(n log n) average, O(n²) worst-case
Space Complexity: O(log n) for recursion stack
"""

def quick_sort(arr):
    """
    Sort an array using quick sort algorithm
    مرتب‌سازی یک آرایه با استفاده از الگوریتم مرتب‌سازی سریع
    
    Args:
        arr: List of comparable elements / لیستی از عناصر قابل مقایسه
    
    Returns:
        Sorted list / لیست مرتب‌شده
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (last element) / انتخاب محور (آخرین عنصر)
    pivot = arr[-1]
    
    # Partition / تقسیم‌بندی
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursive sort / مرتب‌سازی بازگشتی
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place quick sort (more efficient) / مرتب‌سازی سریع درجا (کارآمدتر)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index / تقسیم‌بندی و گرفتن ایندکس محور
        pivot_index = partition(arr, low, high)
        
        # Recursively sort left and right / مرتب‌سازی بازگشتی چپ و راست
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """Partition function for in-place sort / تابع تقسیم‌بندی برای مرتب‌سازی درجا"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage / مثال استفاده
if __name__ == "__main__":
    # Test data / داده‌های تست
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    sorted_numbers = quick_sort(numbers)
    print(f"Sorted (functional): {sorted_numbers}")
    
    # In-place sort / مرتب‌سازی درجا
    numbers_copy = numbers.copy()
    quick_sort_inplace(numbers_copy)
    print(f"Sorted (in-place): {numbers_copy}")
    
    # Test with larger dataset / تست با دیتاست بزرگتر
    import random
    large_data = [random.randint(1, 100) for _ in range(20)]
    print(f"\nRandom data (20 items): {large_data}")
    sorted_large = quick_sort(large_data)
    print(f"Sorted: {sorted_large}")
