import timeit
import matplotlib.pyplot as plt

# Original implementation
def fibonacci(n):
  if n ==0 or n ==1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Memorization implementation
fib_cache = {}
def fibonacci_mem(n):
    global fib_cache
    if n <= 1:
        return n
    if n not in fib_cache:
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_cache[n]

# Measure the execution time of the original implementation
original_times = []
print("Execution time of original implementation:")
for i in range(36):
    time = timeit.timeit(lambda: fibonacci(i), number=100)
    print(f"fibonacci({i}): {time:.8f} seconds")
    original_times.append(time)

# Measure the execution time of the memorization implementation
memorization_times = []
print("Execution time of memorization implementation:")
for i in range(36):
    time = timeit.timeit(lambda: fibonacci_mem(i), number=100)
    print(f"fibonacci_mem({i}): {time:.8f} seconds")
    memorization_times.append(time)

# Plot the results
plt.plot(range(36), original_times, label="Original")
plt.plot(range(36), memorization_times, label="Memorization")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Execution Time of Fibonacci Implementations")
plt.legend()
plt.show()