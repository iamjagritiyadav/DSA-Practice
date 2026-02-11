# Summary Ranges

## Problem Statement

Given a sorted unique integer array `nums`, return the smallest sorted list of ranges that cover all numbers exactly.

Range format:

* "a->b" if a != b
* "a" if a == b

---

# Core Idea of This Implementation

This solution uses a **single pointer with a nested while loop** to group consecutive numbers.

Because the array is:

* Sorted
* Unique

Consecutive numbers must satisfy:

nums[i] + 1 == nums[i + 1]

If this condition breaks, a range ends.

---

# Concepts Used

1. While loop traversal
2. Range compression
3. Two-pointer logic using single index movement
4. String construction

---

# Step-by-Step Explanation Based on the Code

## 1. Initialize Result and Pointer

```python
ans = []
i = 0
```

* `ans` stores final ranges.
* `i` is the main traversal pointer.

---

## 2. Outer While Loop

```python
while i < len(nums):
```

This ensures we process every number exactly once.

---

## 3. Mark Start of Range

```python
start = nums[i]
```

At the beginning of every iteration, we assume a new range starts here.

---

## 4. Expand the Range

```python
while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
    i += 1
```

This loop keeps moving `i` forward as long as numbers are consecutive.

When this loop stops:

* Either we reached the end of the array
* Or continuity broke

Now `nums[i]` is the end of the current range.

---

## 5. Add the Range to Result

```python
if start != nums[i]:
    ans.append(str(start) + '->' + str(nums[i]))
else:
    ans.append(str(nums[i]))
```

Two cases:

Case 1: Multiple numbers in range
Example: 2,3,4
Output: "2->4"

Case 2: Single number range
Example: 7
Output: "7"

---

## 6. Move to Next Range

```python
i += 1
```

After closing the range, move to next unprocessed number.

---

# Final Code

```python
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans
```

---

# Time and Space Complexity

Time Complexity:
O(n)

Each element is visited once.

Space Complexity:
O(1)

Ignoring output storage.

---

# Why This Approach Is Efficient

* Single pass
* No extra data structures
* Constant extra memory
* Clean range detection using pointer movement

