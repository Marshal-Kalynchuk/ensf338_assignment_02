import sys
import json
import timeit
import matplotlib.pyplot as plt
import threading
threading.stack_size(135544320)

sys.setrecursionlimit(20000)

def quicksort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quicksort(arr, low, pi-1)
    quicksort(arr, pi + 1, high)
    
def partition(array, start, end):
  mid = (start + end) // 2
  pivot = sorted([array[start], array[mid], array[end]])[1]
  if pivot == array[start]:
    p = start
  elif pivot == array[mid]:
    p = mid
    array[start], array[mid] = array[mid], array[start]
  else:
    p = end
    array[start], array[end] = array[end], array[start]
  low = start + 1
  high = end
  while True:
    while low <= high and array[high] >= pivot:
      high = high - 1
    while low <= high and array[low] <= pivot:
      low = low + 1
    if low <= high:
      array[low], array[high] = array[high], array[low]
    else:
      break
  array[start], array[high] = array[high], array[start]
  return high

with open("ex2.json", "r") as f:
  data = f.read()
  data = json.loads(data)

sorting_times = []
for arr in data:
  time = timeit.timeit(lambda: quicksort(arr, 0, len(arr)-1), number=10)
  sorting_times.append(time)
  print(f"Sorting time for array of length {len(arr)}: {time}")

# Get the array lengths
array_lengths = [len(arr) for arr in data]

# Plot the bar graph
plt.plot(array_lengths, sorting_times)
plt.xlabel("Array length")
plt.ylabel("Sorting time (s)")
plt.title("Sorting time vs. array length")
plt.show()