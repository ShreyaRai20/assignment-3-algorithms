# Assignment 3: Understanding Algorithm Efficiency and Scalability

## Overview

This assignment explores the efficiency and scalability of two fundamental algorithms:

1. Randomized Quicksort
2. Hashing with Chaining

The goal is to analyze their theoretical performance and compare it with empirical results.

---

# Part 1: Randomized Quicksort Analysis

## 1. Implementation

Randomized Quicksort improves upon deterministic Quicksort by selecting the pivot randomly instead of choosing a fixed element (e.g., first element).

Key features of the implementation:

- Pivot is selected uniformly at random.
- Handles edge cases:
  - Empty arrays
  - Arrays with duplicate elements
  - Already sorted arrays
- Uses a 3-way partition:
  - Elements less than pivot
  - Elements equal to pivot
  - Elements greater than pivot

---

## 2. Theoretical Analysis

### Recurrence Relation

The expected running time of Randomized Quicksort is given by:

T(n) = (1/n) \* Σ [T(k) + T(n-k-1)] + O(n)

This represents all possible pivot choices.

---

### Average Case Time Complexity

Solving the recurrence:

T(n) = O(n log n)

### Explanation

- Each partition step takes O(n) time.
- On average, the pivot splits the array into reasonably balanced parts.
- The recursion depth is O(log n).
- Therefore, total work = O(n log n).

---

### Indicator Random Variable Analysis

Define:

- X_ij = 1 if elements i and j are compared
- X_ij = 0 otherwise

The probability that two elements are compared is:

P(X_ij = 1) = 2 / (j - i + 1)

Summing over all pairs:

Expected comparisons = O(n log n)

---

## 3. Empirical Comparison

### Experimental Setup

We compared:

- Randomized Quicksort
- Deterministic Quicksort (first element as pivot)

Across:

- Random arrays
- Sorted arrays
- Reverse sorted arrays
- Arrays with duplicates

---

### Sample Results

| Input Type     | Randomized QS | Deterministic QS |
| -------------- | ------------- | ---------------- |
| Random         | Fast          | Fast             |
| Sorted         | Fast          | Very Slow        |
| Reverse Sorted | Fast          | Very Slow        |
| Duplicates     | Fast          | Moderate         |

---

### Observations

1. Randomized Quicksort:
   - Performs consistently across all input types.
   - Avoids worst-case scenarios due to randomness.

2. Deterministic Quicksort:
   - Performs well on random data.
   - Degrades to O(n²) for sorted or reverse-sorted arrays.

3. Arrays with duplicates:
   - Randomized approach performs better due to balanced partitioning.

---

### Conclusion (Quicksort)

Randomized Quicksort is more robust and scalable because:

- It avoids predictable worst-case inputs.
- It maintains O(n log n) expected time complexity.

---

# Part 2: Hashing with Chaining

## 1. Implementation

We implemented a hash table using:

- Array of buckets
- Each bucket stores a list (chain)

Supported operations:

- Insert(key, value)
- Search(key)
- Delete(key)

---

## 2. Theoretical Analysis

### Assumption: Simple Uniform Hashing

Each key is equally likely to hash into any slot.

---

### Time Complexity

Let:

- n = number of elements
- m = number of slots
- α (load factor) = n / m

#### Insert:

- Average: O(1)

#### Search:

- Average: O(1 + α)

#### Delete:

- Average: O(1 + α)

---

## 3. Load Factor Analysis

### Definition

α = n / m

---

### Impact on Performance

- If α is small:
  - Fewer collisions
  - Faster operations

- If α is large:
  - More collisions
  - Longer chains
  - Slower operations

---

## 4. Collision Handling

We use **chaining**, where:

- Each slot contains a list of elements
- Collisions are handled by adding elements to the list

---

## 5. Optimization Strategies

### 1. Dynamic Resizing

- Resize table when α exceeds threshold (e.g., 0.75)
- Rehash all elements

### 2. Good Hash Functions

- Use built-in hash or universal hashing
- Distribute keys uniformly

### 3. Maintain Low Load Factor

- Increase table size when needed

---

## 6. Conclusion (Hashing)

Hashing with chaining provides:

- Efficient average-case performance
- Flexibility in handling collisions

However:

- Performance depends heavily on load factor
- Poor hash functions or high α degrade performance

---

# Final Conclusion

- Randomized Quicksort is preferred over deterministic Quicksort due to its stability and resistance to worst-case inputs.
- Hash tables with chaining provide near constant-time operations when the load factor is controlled.
- Both algorithms demonstrate the importance of balancing theoretical guarantees with practical implementation.

---

# Summary

| Algorithm               | Average Time Complexity | Worst Case |
| ----------------------- | ----------------------- | ---------- |
| Randomized Quicksort    | O(n log n)              | O(n²)      |
| Deterministic Quicksort | O(n log n)              | O(n²)      |
| Hash Table (Chaining)   | O(1 + α)                | O(n)       |

---

# End of Report
