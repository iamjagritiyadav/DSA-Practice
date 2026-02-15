# Spiral Matrix

## Overview

The Spiral Matrix problem requires traversing a 2D matrix in spiral order and returning all elements in a single list. The traversal starts from the top-left corner and proceeds in a clockwise spiral pattern until all elements are visited.

This problem is commonly asked in coding interviews because it tests boundary control, simulation logic, and careful index management.

---

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in spiral order.

### Constraints

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`

---

## Example 1

Input:

```
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

Output:

```
[1,2,3,6,9,8,7,4,5]
```

---

## Example 2

Input:

```
[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]]
```

Output:

```
[1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## Intuition

A spiral traversal moves layer by layer. Each layer consists of:

1. Top row (left → right)
2. Right column (top → bottom)
3. Bottom row (right → left)
4. Left column (bottom → top)

After completing one layer, we shrink the boundaries inward and repeat until all elements are processed.

The key idea is to maintain four pointers representing the current boundaries of the matrix:

* `top` → starting row index
* `bottom` → ending row index
* `left` → starting column index
* `right` → ending column index

---

## Algorithm

1. Initialize an empty list `res` to store the result.
2. Define four boundary pointers: `top`, `bottom`, `left`, and `right`.
3. While `top <= bottom` and `left <= right`:

   * Traverse from left to right along the top row.
   * Increment `top`.
   * Traverse from top to bottom along the right column.
   * Decrement `right`.
   * If `top <= bottom`, traverse from right to left along the bottom row.
   * Decrement `bottom`.
   * If `left <= right`, traverse from bottom to top along the left column.
   * Increment `left`.
4. Return the result list.

---

## Implementation (Python)

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            
            # Traverse left → right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # Traverse top → bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            # Traverse right → left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # Traverse bottom → top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        
        return res
```

---

## Complexity Analysis

### Time Complexity: O(m × n)

Each element is visited exactly once during traversal. Therefore, the overall time complexity is linear with respect to the number of elements in the matrix.

### Space Complexity: O(1)

No additional data structures are used apart from boundary pointers. The output list does not count toward auxiliary space.

---

## Edge Cases Considered

* Single row matrix (e.g., `[[1,2,3]]`)
* Single column matrix (e.g., `[[1],[2],[3]]`)
* 1x1 matrix
* Non-square matrices

The boundary checks (`if top <= bottom` and `if left <= right`) ensure no element is processed twice.

---

## Key Takeaways

* Spiral traversal is a simulation problem.
* Careful boundary updates prevent duplicate visits.
* Always guard reverse traversals with boundary checks.
* This is a standard interview problem for practicing matrix traversal logic.

---

## Suggested Improvements

* Implement an anti-clockwise version as a variation.
* Solve without modifying input matrix.
* Extend to generate a spiral matrix instead of reading one (reverse problem).

---

## Author

Implemented as part of data structures and algorithms practice.
