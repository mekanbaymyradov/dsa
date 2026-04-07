# 1) Naive Recursive Algorithm 
def fibonacci_recursive(n):
    if n <= 1:
        return n
    new_fib = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return new_fib


print([fibonacci_recursive(n) for n in range(5)])


