"""
Bubble Sort Algorithm / الگوریتم مرتب‌سازی حبابی
-----------------------------------------------
Time Complexity: O(n²)
Space Complexity: O(1)
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm
    مرتب‌سازی یک آرایه با استفاده از الگوریتم مرتب‌سازی حبابی
    
    Args:
        arr: List of comparable elements / لیستی از عناصر قابل مقایسه
    
    Returns:
        Sorted list / لیست مرتب‌شده
    """
    n = len(arr)
    arr = arr.copy()  # Create a copy to avoid modifying original
    
    for i in range(n - 1):
        # Flag to optimize - if no swaps, array is sorted
        swapped = False
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps, break early
        if not swapped:
            break
            
        print(f"After pass {i + 1}: {arr}")
    
    return arr

def bubble_sort_descending(arr):
    """Sort in descending order / مرتب‌سازی نزولی"""
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

# Example usage / مثال استفاده
if __name__ == "__main__":
    # Test data / داده‌های تست
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    
    sorted_numbers = bubble_sort(numbers)
    print(f"Sorted ascending: {sorted_numbers}")
    
    sorted_desc = bubble_sort_descending(numbers)
    print(f"Sorted descending: {sorted_desc}")
    
    # Test with strings / تست با رشته‌ها
    words = ["banana", "apple", "cherry", "date", "fig"]
    print(f"\nOriginal words: {words}")
    sorted_words = bubble_sort(words)
    print(f"Sorted words: {sorted_words}")
