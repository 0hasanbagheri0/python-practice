"""
Fibonacci Sequence using Recursion / دنباله فیبوناچی با استفاده از بازگشت
----------------------------------------------------------------------------
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
دنباله فیبوناچی: ۰, ۱, ۱, ۲, ۳, ۵, ۸, ۱۳, ۲۱, ۳۴, ...

Recursive definition / تعریف بازگشتی:
- Base cases: F(0) = 0, F(1) = 1 / حالت‌های پایه
- Recursive case: F(n) = F(n-1) + F(n-2) / حالت بازگشتی

Time Complexity: O(2^n) for naive recursion / برای بازگشت ساده
Space Complexity: O(n) (due to recursion stack)
"""

def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursion (naive)
    محاسبه عدد فیبوناچی nام با استفاده از بازگشت (ساده)
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        int: nth Fibonacci number / عدد فیبوناچی nام
    
    Note: This is very slow for large n! / بسیار کند برای n بزرگ!
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers!")
    
    # Base cases / حالت‌های پایه
    if n <= 1:
        return n
    
    # Recursive case / حالت بازگشتی
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo={}):
    """
    Calculate nth Fibonacci number using memoization (caching)
    محاسبه عدد فیبوناچی nام با استفاده از مموری‌سازی (کش)
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
        memo: Dictionary for caching results / دیکشنری برای کش کردن نتایج
    
    Returns:
        int: nth Fibonacci number / عدد فیبوناچی nام
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers!")
    
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    
    return memo[n]

def fibonacci_iterative(n):
    """
    Calculate nth Fibonacci number using iteration (most efficient)
    محاسبه عدد فیبوناچی nام با استفاده از تکرار (کارآمدترین)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        int: nth Fibonacci number / عدد فیبوناچی nام
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers!")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fibonacci_tail_recursive(n, a=0, b=1):
    """
    Calculate nth Fibonacci number using tail recursion
    محاسبه عدد فیبوناچی nام با استفاده از بازگشت دنباله‌ای
    
    Time Complexity: O(n)
    Space Complexity: O(n) (can be optimized by compiler)
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
        a: First accumulator / انباشته‌کننده اول
        b: Second accumulator / انباشته‌کننده دوم
    
    Returns:
        int: nth Fibonacci number / عدد فیبوناچی nام
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers!")
    
    if n == 0:
        return a
    if n == 1:
        return b
    
    return fibonacci_tail_recursive(n - 1, b, a + b)

def fibonacci_generator(n):
    """
    Generate Fibonacci sequence up to nth number using generator
    تولید دنباله فیبوناچی تا عدد nام با استفاده از ژنراتور
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
    
    Yields:
        Fibonacci numbers one by one / اعداد فیبوناچی یکی یکی
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers!")
    
    a, b = 0, 1
    for i in range(n + 1):
        if i == 0:
            yield a
        elif i == 1:
            yield b
        else:
            a, b = b, a + b
            yield b

def fibonacci_sequence(n):
    """
    Return full Fibonacci sequence up to nth number
    بازگرداندن دنباله کامل فیبوناچی تا عدد nام
    
    Args:
        n: Non-negative integer / عدد صحیح غیرمنفی
    
    Returns:
        list: Fibonacci sequence / دنباله فیبوناچی
    """
    return list(fibonacci_generator(n))


# === مثال‌های استفاده / Usage Examples ===
if __name__ == "__main__":
    print("=" * 50)
    print("FIBONACCI DEMO / نمایش فیبوناچی")
    print("=" * 50)
    
    # Test with different methods / تست با روش‌های مختلف
    numbers = [0, 1, 2, 5, 10, 15]
    
    print("\n--- Comparing Methods ---")
    print(f"{'n':<5} {'Recursive':<12} {'Iterative':<12} {'Memoized':<12} {'Tail':<12}")
    print("-" * 60)
    
    for n in numbers:
        try:
            rec = fibonacci_recursive(n)
        except RecursionError:
            rec = "Too slow!"
        
        itr = fibonacci_iterative(n)
        mem = fibonacci_memoized(n)
        tail = fibonacci_tail_recursive(n)
        
        print(f"{n:<5} {str(rec):<12} {itr:<12} {mem:<12} {tail:<12}")
    
    # Generate full sequence / تولید دنباله کامل
    print("\n--- Fibonacci Sequence (0 to 15) ---")
    sequence = fibonacci_sequence(15)
    for i, fib in enumerate(sequence):
        print(f"F({i}) = {fib}")
    
    # Fibonacci numbers list / لیست اعداد فیبوناچی
    print("\n--- First 20 Fibonacci Numbers ---")
    fibs = fibonacci_sequence(20)
    print(fibs)
    
    # Performance comparison / مقایسه عملکرد
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON / مقایسه عملکرد")
    print("=" * 50)
    
    import time
    
    n = 35
    
    # Recursive (naive) / بازگشتی (ساده)
    print(f"\nCalculating F({n})...")
    start = time.time()
    try:
        result = fibonacci_recursive(n)
        rec_time = time.time() - start
        print(f"Recursive: {rec_time:.6f} seconds -> F({n}) = {result}")
    except RecursionError:
        print("Recursive: Too slow! (Recursion depth exceeded)")
    
    # Memoized / مموری‌شده
    start = time.time()
    result = fibonacci_memoized(n)
    mem_time = time.time() - start
    print(f"Memoized: {mem_time:.6f} seconds -> F({n}) = {result}")
    
    # Iterative / تکراری
    start = time.time()
    result = fibonacci_iterative(n)
    itr_time = time.time() - start
    print(f"Iterative: {itr_time:.6f} seconds -> F({n}) = {result}")
    
    # Tail recursive / بازگشتی دنباله‌ای
    start = time.time()
    result = fibonacci_tail_recursive(n)
    tail_time = time.time() - start
    print(f"Tail Recursive: {tail_time:.6f} seconds -> F({n}) = {result}")
    
    # Golden ratio / نسبت طلایی
    print("\n" + "=" * 50)
    print("GOLDEN RATIO / نسبت طلایی")
    print("=" * 50)
    
    n = 20
    fib_n = fibonacci_iterative(n)
    fib_n_1 = fibonacci_iterative(n - 1)
    ratio = fib_n / fib_n_1
    
    print(f"F({n}) / F({n-1}) = {fib_n} / {fib_n_1} = {ratio:.10f}")
    print(f"Golden ratio (φ) ≈ 1.6180339887")
    print(f"Difference: {abs(ratio - 1.6180339887):.10f}")
    
    # Find index of a Fibonacci number / پیدا کردن ایندکس یک عدد فیبوناچی
    print("\n" + "=" * 50)
    print("FINDING INDEX / پیدا کردن ایندکس")
    print("=" * 50)
    
    target = 55
    index = None
    for i, fib in enumerate(fibonacci_sequence(20)):
        if fib == target:
            index = i
            break
    
    print(f"{target} is F({index})")
