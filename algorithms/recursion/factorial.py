"""
Factorial using Recursion / فاکتوریل با استفاده از بازگشت
---------------------------------------------------------
Factorial of n: n! = n * (n-1) * (n-2) * ... * 1
فاکتوریل n: n! = n * (n-1) * (n-2) * ... * 1

Recursive definition / تعریف بازگشتی:
- Base case: 0! = 1, 1! = 1 / حالت پایه
- Recursive case: n! = n * (n-1)! / حالت بازگشتی

Time Complexity: O(n)
Space Complexity: O(n) (due to recursion stack)
"""

def factorial_recursive(n):
    """
    Calculate factorial using recursion / محاسبه فاکتوریل با استفاده از بازگشت
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        int: Factorial of n / فاکتوریل n
        
    Raises:
        ValueError: If n is negative / اگر n منفی باشد
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    
    # Base case / حالت پایه
    if n <= 1:
        return 1
    
    # Recursive case / حالت بازگشتی
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Calculate factorial using iteration / محاسبه فاکتوریل با استفاده از تکرار
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        int: Factorial of n / فاکتوریل n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_tail_recursive(n, accumulator=1):
    """
    Calculate factorial using tail recursion / محاسبه فاکتوریل با بازگشت دنباله‌ای
    (More efficient - can be optimized by compiler) / (کارآمدتر - قابل بهینه‌سازی توسط کامپایلر)
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
        accumulator: Accumulator for tail recursion / انباشته‌کننده برای بازگشت دنباله‌ای
    
    Returns:
        int: Factorial of n / فاکتوریل n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    
    # Base case / حالت پایه
    if n <= 1:
        return accumulator
    
    # Tail recursive case / حالت بازگشتی دنباله‌ای
    return factorial_tail_recursive(n - 1, n * accumulator)

def factorial_memoized(n, memo={}):
    """
    Calculate factorial using memoization (caching) / محاسبه فاکتوریل با مموری‌سازی (کش)
    (Faster for repeated calculations) / (سریع‌تر برای محاسبات تکراری)
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
        memo: Dictionary for caching results / دیکشنری برای کش کردن نتایج
    
    Returns:
        int: Factorial of n / فاکتوریل n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    
    if n <= 1:
        return 1
    
    if n not in memo:
        memo[n] = n * factorial_memoized(n - 1, memo)
    
    return memo[n]


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("FACTORIAL DEMO / نمایش فاکتوریل")
    print("=" * 50)
    
    # Test with different methods / تست با روش‌های مختلف
    numbers = [0, 1, 5, 7, 10]
    
    print("\n--- Comparing Methods ---")
    print(f"{'n':<5} {'Recursive':<12} {'Iterative':<12} {'Tail':<12} {'Memoized':<12}")
    print("-" * 60)
    
    for n in numbers:
        rec = factorial_recursive(n)
        itr = factorial_iterative(n)
        tail = factorial_tail_recursive(n)
        mem = factorial_memoized(n)
        print(f"{n:<5} {rec:<12} {itr:<12} {tail:<12} {mem:<12}")
    
    # Calculate factorials for a range / محاسبه فاکتوریل برای یک بازه
    print("\n--- Factorials from 0 to 10 ---")
    for i in range(11):
        print(f"{i}! = {factorial_recursive(i)}")
    
    # Performance comparison / مقایسه عملکرد
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON / مقایسه عملکرد")
    print("=" * 50)
    
    import time
    
    n = 20
    
    # Recursive / بازگشتی
    start = time.time()
    result = factorial_recursive(n)
    rec_time = time.time() - start
    print(f"Recursive: {rec_time:.6f} seconds -> {n}! = {result}")
    
    # Iterative / تکراری
    start = time.time()
    result = factorial_iterative(n)
    itr_time = time.time() - start
    print(f"Iterative: {itr_time:.6f} seconds -> {n}! = {result}")
    
    # Tail recursive / بازگشتی دنباله‌ای
    start = time.time()
    result = factorial_tail_recursive(n)
    tail_time = time.time() - start
    print(f"Tail Recursive: {tail_time:.6f} seconds -> {n}! = {result}")
    
    # Error handling / مدیریت خطا
    print("\n--- Error Handling ---")
    try:
        factorial_recursive(-5)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Large factorial / فاکتوریل بزرگ
    print("\n--- Large Factorial ---")
    n = 100
    result = factorial_recursive(n)
    print(f"{n}! has {len(str(result))} digits")
    print(f"First 50 digits: {str(result)[:50]}...")
