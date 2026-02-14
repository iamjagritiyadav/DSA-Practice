# Merge Intervals 
## Final Optimal Code

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
```

---

# Part 1: Understanding the Problem Clearly

Each interval is written as:

[start, end]

Example:
[1,3] means interval starts at 1 and ends at 3.

Two intervals overlap if:

second_start <= first_end

Example:
[1,3] and [2,6]

Since 2 <= 3, they overlap.

Goal:
Merge all overlapping intervals and return only non-overlapping ones.

---

# Part 2: Why Sorting Is Necessary

Key idea:
Overlapping can only be checked correctly if intervals are sorted by starting time.

Example (unsorted):
[[4,7],[1,4]]

If we don't sort, we cannot detect overlap correctly.

After sorting:
[[1,4],[4,7]]

Now checking becomes easy.

---

# Line by Line Explanation

## 1. intervals.sort(key=lambda x: x[0])

Break this fully:

* sort() modifies the list in-place.
* key= tells Python how to compare elements.
* lambda x: x[0] means:
  take each interval x and use its first value (start time) for sorting.

If intervals = [[4,7],[1,4]]
After sorting:
[[1,4],[4,7]]

Time complexity of sorting = O(n log n)

---

## 2. merged = []

Create empty list.

This will store final merged intervals.

---

## 3. for interval in intervals:

Loop through every interval in sorted list.

interval is a list like [start, end]

---

## 4. if not merged or merged[-1][1] < interval[0]:

Break this condition carefully.

Part 1: not merged

Means merged list is empty.

If empty, we must add first interval.

Part 2: merged[-1][1] < interval[0]

* merged[-1] means last interval in merged list.
* [1] means its end value.
* interval[0] means current interval's start.

So condition means:

If last_end < current_start

That means NO overlap.

Example:
Last interval = [1,3]
Current = [5,8]

3 < 5 → no overlap

So we append it.

---

## 5. merged.append(interval)

Add interval as it is.

append() adds element at end of list.

---

## 6. else:

This block runs when there IS overlap.

Overlap condition:

merged[-1][1] >= interval[0]

---

## 7. merged[-1][1] = max(merged[-1][1], interval[1])

This is the merge step.

We update the ending time of last interval.

Example:
Last interval = [1,3]
Current = [2,6]

New merged interval should be:
[1,6]

So:
max(3,6) = 6

We modify the end value directly.

Important:
We are not creating new interval.
We are modifying the last one in merged list.

---

## 8. return merged

Return final list of merged intervals.

---

# Full Dry Run Example

Input:
[[1,3],[2,6],[8,10],[15,18]]

After sorting:
[[1,3],[2,6],[8,10],[15,18]]

Step 1:
merged = [[1,3]]

Step 2:
Check [2,6]
3 >= 2 → overlap
Merge → [1,6]
merged = [[1,6]]

Step 3:
Check [8,10]
6 < 8 → no overlap
merged = [[1,6],[8,10]]

Step 4:
Check [15,18]
10 < 15 → no overlap
merged = [[1,6],[8,10],[15,18]]

Return result.

---

# Why This Works

Sorting ensures:
If overlap exists, it will always be with previous interval only.

We never need to check earlier intervals.

That is why algorithm works in single pass after sorting.

---

# Time Complexity

Sorting: O(n log n)
Loop: O(n)

Total: O(n log n)

---

# Space Complexity

merged list stores at most n intervals.

So space complexity = O(n)

---

# Core Concept Summary

1. Sort intervals by start time.
2. Compare with last merged interval.
3. If no overlap → append.
4. If overlap → update end.

This greedy approach guarantees correct merging with minimal checks.
