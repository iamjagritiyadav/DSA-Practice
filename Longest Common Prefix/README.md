
# Longest Common Prefix

## Problem Statement

Given an array of strings `strs`, return the longest common prefix among all strings.
If there is no common prefix, return an empty string `""`.

Example:

```
Input: ["flower", "flow", "flight"]
Output: "fl"
```

---

# Concept Used in This Solution

This solution is based on:

1. Finding Minimum Length String
2. Character-by-Character Comparison
3. Nested Loop Traversal
4. Early Return Optimization

---

# Step-by-Step Concept Explanation

## 1. Why Find Minimum Length?

The longest possible prefix can never be longer than the shortest string.

So first we compute:

```python
min_length = float("inf")
for s in strs:
    if len(s) < min_length:
        min_length = len(s)
```

`float("inf")` ensures any string length will be smaller initially.
We store the smallest string length.

---

## 2. Character-by-Character Checking

Now we check each index position `i` from `0` to `min_length - 1`.

```python
i = 0
while i < min_length:
```

At each index `i`, we compare characters of all strings.

---

## 3. Nested Loop Comparison

```python
for s in strs:
    if s[i] != strs[0][i]:
        return strs[0][:i]
```

We compare every string’s `i`th character with the first string.
If mismatch occurs, return prefix till index `i`.

This is called horizontal scanning approach.

---

## 4. If No Mismatch Found

If loop completes without mismatch:

```python
return strs[0][:i]
```

That means all characters matched till `min_length`.

---

# Final Code

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1

        return strs[0][:i]
```

---

# Time and Space Complexity

Time Complexity:
O(n * m)

Where:

* `n` = number of strings
* `m` = minimum length among strings

Because for each character position, we compare all strings.

---

Space Complexity:
O(1)

