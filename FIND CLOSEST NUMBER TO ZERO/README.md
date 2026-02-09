# Find Closest Number to Zero

## Problem Statement
Given an integer array `nums`, return the number that is closest to `0`.
If there are two numbers equally close to `0`, return the positive number.

---

## Approach / Logic (Layman Explanation)

1. Assume the first element of the array is the closest to zero.
2. Traverse the array one element at a time.
3. Compare the absolute value of the current element with the absolute value of the stored closest number.
4. If the current number is closer to zero, update `closest`.
5. After traversal, check:
   - If the closest number is negative
   - And its positive counterpart exists in the array
   - Then return the positive number.
6. Otherwise, return the closest number.

---

## Code
```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
