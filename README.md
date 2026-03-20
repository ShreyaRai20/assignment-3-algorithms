# Assignment 3: Algorithm Efficiency and Scalability

## 📌 Overview

This project analyzes and compares the efficiency and scalability of two important algorithms:

- **Randomized Quicksort**
- **Hash Table with Chaining**

The goal is to evaluate their theoretical performance and validate it through empirical testing.

---

## 📂 Project Structure

assignment-3-algorithms/
│── quicksort.py # Sorting algorithms implementation  
│── hash_table.py # Hash table with chaining  
│── experiments.py # Performance comparison  
│── report.md # Detailed analysis  
│── README.md # Documentation

---

## ⚙️ Features

### 🔹 Randomized Quicksort

- Selects pivot randomly
- Avoids worst-case scenarios
- Handles:
  - Empty arrays
  - Sorted arrays
  - Duplicate values

### 🔹 Deterministic Quicksort

- Uses first element as pivot
- Demonstrates worst-case behavior on sorted inputs

### 🔹 Hash Table with Chaining

- Uses lists to handle collisions
- Supports:
  - Insert
  - Search
  - Delete
- Maintains load factor

---

## 🚀 How to Run

### 1. Clone Repository

```bash
git clone <your-repository-link>
cd assignment-3-algorithms
```

---

### 2. Run Quicksort Experiments

```bash
python experiments.py
```

This will:

- Generate multiple input types
- Compare execution times
- Display results in the console

---

### 3. Test Hash Table

Run the following in Python:

```python
from hash_table import HashTable

ht = HashTable()

# Insert values
ht.insert("apple", 10)
ht.insert("banana", 20)

# Search
print(ht.search("apple"))  # Output: 10

# Delete
ht.delete("apple")
print(ht.search("apple"))  # Output: None
```

---

## 📊 Key Findings

### 🔹 Quicksort

- Randomized Quicksort performs consistently well
- Deterministic Quicksort performs poorly on:
  - Sorted arrays
  - Reverse-sorted arrays

- Randomization ensures O(n log n) average performance

---

### 🔹 Hash Table

- Average time complexity: O(1)
- Performance depends on load factor (α)
- Higher load factor leads to more collisions

---

## 🧠 Concepts Covered

- Divide and Conquer
- Randomized Algorithms
- Time Complexity Analysis
- Recurrence Relations
- Hashing and Collision Resolution
- Load Factor

---

## 📈 Possible Improvements

- Implement dynamic resizing in hash table
- Add graphical analysis using matplotlib
- Compare with additional sorting algorithms

---

## 👩‍💻 Author

Shreya Rai

---

## 📎 Submission

GitHub Repository Link: https://github.com/ShreyaRai20/assignment-3-algorithms.git

---

## ✅ Conclusion

This project demonstrates:

- Randomization improves algorithm robustness
- Hashing provides efficient average-case performance
- Algorithm efficiency depends on input distribution and design choices
