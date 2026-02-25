# Sort Integers by Number of 1 Bits

##  Problem Statement

Given an integer array `arr`, sort the array in ascending order based on:

1. The number of `1`s in the binary representation of each number.
2. If two numbers have the same number of `1`s, sort them in ascending numerical order.

---

##  Example

### Example 1

**Input:**

```
arr = [0,1,2,3,4,5,6,7,8]
```

**Output:**

```
[0,1,2,4,8,3,5,6,7]
```

**Explanation:**

* 0 → 0 bits
* 1, 2, 4, 8 → 1 bit
* 3, 5, 6 → 2 bits
* 7 → 3 bits

Sorted first by bit count, then by number.

---

### Example 2

**Input:**

```
arr = [1024,512,256,128,64,32,16,8,4,2,1]
```

**Output:**

```
[1,2,4,8,16,32,64,128,256,512,1024]
```

All numbers contain exactly one `1` in binary form, so they are sorted normally in ascending order.

---

##  Approach

We sort using a custom key:

* Primary key → Number of `1`s in binary representation
* Secondary key → Integer value

Python allows tuple-based sorting, making this straightforward.

---

##  Implementation

### Using Built-in bit_count() (Recommended)

```python
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (x.bit_count(), x))
```

### Alternative Method

```python
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```

---

##  Time Complexity

* Sorting takes **O(n log n)**
* Bit counting takes **O(1)** for fixed integer size

Overall complexity: **O(n log n)**

---

## Space Complexity

* O(n) for sorting result

---

##  Edge Cases Considered

* Single element array
* All elements identical
* All elements having same number of 1 bits
* Array containing 0

---

##  Constraints

* 1 <= arr.length <= 500
* 0 <= arr[i] <= 10^4

---

## Key Takeaways

* Tuple-based sorting is powerful.
* Python's `bit_count()` is efficient and clean.
* Always define clear sorting priorities when multiple conditions are involved.

---

## Final Thoughts

This problem tests understanding of:

* Binary representation
* Custom sorting using keys
* Clean and optimized Python coding practices

A simple but important DSA pattern.
