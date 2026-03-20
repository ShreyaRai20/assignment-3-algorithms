import random
import time

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


# Deterministic Quicksort (first element as pivot)
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)


# Utility to measure time
def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start