fib_cache = {}
def fibonacci(n):
    global fib_cache
    if n <= 1:
        return n
    if n not in fib_cache:
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_cache[n]