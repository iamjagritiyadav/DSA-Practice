# Product of Array Except Self

## Overview

The "Product of Array Except Self" problem requires returning an output array such that each element at index `i` is equal to the product of all elements in the input array except `nums[i]`.

The key constraint is that the solution must run in **O(n) time** and must not use division.

This is a classic interview problem that tests prefix/suffix product logic and space optimization.

---

## Problem Statement

Given an integer array `nums`, return an array `answer` such that:

```
answer[i] = product of all elements of nums except nums[i]
```

### Constraints

* The solution must run in O(n) time.
* Division operation is not allowed.
* Use constant extra space (excluding output array).

---

## Example

Input:

```
nums = [1,2,3,4]
```

Output:

```
[24,12,8,6]
```

Explanation:

* For index 0 → 2×3×4 = 24
* For index 1 → 1×3×4 = 12
* For index 2 → 1×2×4 = 8
* For index 3 → 1×2×3 = 6

---

## Intuition

Instead of using division, we calculate:

1. Product of all elements to the **left** of each index.
2. Product of all elements to the **right** of each index.

Final result at index `i`:

```
left_product[i] × right_product[i]
```

To optimize space, we reuse the output array and calculate left and right products in two passes.

---

## Algorithm

1. Initialize `answer` array with 1s.
2. Traverse from left to right:

   * Store running left product in `answer[i]`.
3. Traverse from right to left:

   * Multiply running right product into `answer[i]`.
4. Return `answer`.

---

## Implementation (Python)

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Left products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        
        # Step 2: Right products
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer
```

---

## Complexity Analysis

### Time Complexity: O(n)

Two linear passes over the array.

### Space Complexity: O(1)

No extra arrays are used apart from the output array.

---

## Why This Approach Is Optimal

* Avoids division (handles zero correctly).
* Uses constant extra space.
* Linear time complexity.
* Clean and interview-standard solution.

---

## Edge Cases Considered

* Array containing zero(s)
* Array with negative numbers
* Minimum size array (length = 1)

The prefix–suffix technique naturally handles zero cases without special logic.

---

## Key Takeaways

* Prefix and suffix patterns are powerful for array product problems.
* Reusing the output array reduces space complexity.
* Two-pass solutions are often optimal for cumulative product problems.

---

## Suggested Extensions

* Implement version using extra prefix and suffix arrays for clarity.
* Analyze behavior when multiple zeros exist.
* Compare with division-based solution (and explain why it is
