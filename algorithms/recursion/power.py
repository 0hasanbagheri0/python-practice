"""
Power Function using Recursion / تابع توان با استفاده از بازگشت
----------------------------------------------------------------
Calculate x^n (x raised to power n) using different approaches
محاسبه x^n (x به توان n) با استفاده از روش‌های مختلف

Time Complexity: 
- Naive: O(n)
- Fast (Exponentiation by squaring): O(log n)
"""

def power_naive(base, exponent):
    """
    Calculate power using naive recursion (multiply base repeatedly)
    محاسبه توان با بازگشت ساده (ضرب پایه به تعداد توان)
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        base: Base number / عدد پایه
        exponent: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        base ** exponent / پایه به توان نما
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative!")
    
    # Base case / حالت پایه
    if exponent == 0:
        return 1
    
    # Recursive case / حالت بازگشتی
    return base * power_naive(base, exponent - 1)

def power_fast(base, exponent):
    """
    Calculate power using fast exponentiation (exponentiation by squaring)
    محاسبه توان با توان‌سازی سریع (به توان رساندن با مربع‌سازی)
    
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    
    Args:
        base: Base number / عدد پایه
        exponent: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        base ** exponent / پایه به توان نما
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative!")
    
    # Base case / حالت پایه
    if exponent == 0:
        return 1
    
    # If exponent is even / اگر نما زوج باشد
    if exponent % 2 == 0:
        half = power_fast(base, exponent // 2)
        return half * half
    
    # If exponent is odd / اگر نما فرد باشد
    return base * power_fast(base, exponent - 1)

def power_iterative(base, exponent):
    """
    Calculate power using iteration
    محاسبه توان با استفاده از تکرار
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        base: Base number / عدد پایه
        exponent: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        base ** exponent / پایه به توان نما
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative!")
    
    result = 1
    for _ in range(exponent):
        result *= base
    
    return result

def power_fast_iterative(base, exponent):
    """
    Calculate power using fast exponentiation iteratively
    محاسبه توان با توان‌سازی سریع به صورت تکراری
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        base: Base number / عدد پایه
        exponent: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        base ** exponent / پایه به توان نما
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative!")
    
    result = 1
    current_base = base
    current_exp = exponent
    
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    
    return result

def power_with_negative(base, exponent):
    """
    Calculate power with negative exponent (returns float)
    محاسبه توان با نما منفی (عدد اعشاری برمی‌گرداند)
    
    Args:
        base: Base number / عدد پایه
        exponent: Integer (can be negative) / عدد صحیح (می‌تواند منفی باشد)
    
    Returns:
        base ** exponent (float) / پایه به توان نما (اعشاری)
    """
    if exponent == 0:
        return 1
    
    if exponent < 0:
        return 1 / power_fast(base, -exponent)
    
    return power_fast(base, exponent)


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("POWER FUNCTION DEMO / نمایش تابع توان")
    print("=" * 50)
    
    # Test with different methods / تست با روش‌های مختلف
    print("\n--- Comparing Methods ---")
    print(f"{'Base':<8} {'Exp':<6} {'Naive':<12} {'Fast':<12} {'Iterative':<12} {'Fast Iter':<12}")
    print("-" * 70)
    
    test_cases = [
        (2, 0), (2, 1), (2, 5), (3, 4), (5, 3), (10, 6)
    ]
    
    for base, exp in test_cases:
        naive = power_naive(base, exp)
        fast = power_fast(base, exp)
        itr = power_iterative(base, exp)
        fast_itr = power_fast_iterative(base, exp)
        print(f"{base:<8} {exp:<6} {naive:<12} {fast:<12} {itr:<12} {fast_itr:<12}")
    
    # Negative exponent / نما منفی
    print("\n--- Negative Exponent ---")
    base = 2
    exp = -3
    result = power_with_negative(base, exp)
    print(f"{base} ^ {exp} = {result}")
    print(f"2 ^ -3 = 1 / 8 = {1/8}")
    
    # Large numbers / اعداد بزرگ
    print("\n--- Large Numbers ---")
    base = 2
    exp = 20
    result = power_fast(base, exp)
    print(f"{base} ^ {exp} = {result}")
    
    # Performance comparison / مقایسه عملکرد
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON / مقایسه عملکرد")
    print("=" * 50)
    
    import time
    
    base = 2
    exponent = 1000000
    
    # Fast recursive / سریع بازگشتی
    start = time.time()
    result = power_fast(base, exponent)
    fast_time = time.time() - start
    print(f"Fast recursive: {fast_time:.6f} seconds")
    
    # Fast iterative / سریع تکراری
    start = time.time()
    result = power_fast_iterative(base, exponent)
    fast_itr_time = time.time() - start
    print(f"Fast iterative: {fast_itr_time:.6f} seconds")
    
    print(f"\nResult has {len(str(result))} digits")
