import random
from quicksort import randomized_quicksort, deterministic_quicksort, measure_time

def generate_data(n, case_type):
    if case_type == "random":
        return [random.randint(0, 1000) for _ in range(n)]
    elif case_type == "sorted":
        return list(range(n))
    elif case_type == "reversed":
        return list(range(n, 0, -1))
    elif case_type == "duplicates":
        return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]


sizes = [100, 500, 1000, 2000]
cases = ["random", "sorted", "reversed", "duplicates"]

for case in cases:
    print(f"\nCase: {case}")
    for size in sizes:
        data = generate_data(size, case)

        t1 = measure_time(randomized_quicksort, data)
        t2 = measure_time(deterministic_quicksort, data)

        print(f"Size {size}: Randomized={t1:.6f}s, Deterministic={t2:.6f}s")