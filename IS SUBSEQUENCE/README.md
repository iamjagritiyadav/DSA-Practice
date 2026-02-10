# Is Subsequence

## Problem
Given two strings `s` and `t`, return `True` if `s` is a subsequence of `t`.  
Otherwise, return `False`.

A subsequence keeps relative order but characters do not need to be contiguous.

---

## Method Used
- Two Pointer Technique
- Linear Scan

---

## Core Idea
- Traverse string `t`
- Try to match characters of `s` in order
- If all characters of `s` are found in sequence → return `True`

---

## How It Works (Short & Clear)

- `j` pointer tracks current index of string `s`
- Loop through string `t`
- If `t[i] == s[j]`, move `j` forward
- When `j` reaches length of `s`, subsequence is complete
- If loop ends and `j` never reaches end → not a subsequence

---

## Algorithm Steps

1. If `s` is empty → return `True`
2. If `len(s) > len(t)` → return `False`
3. Initialize pointer `j = 0`
4. Traverse `t` using index `i`
5. If characters match, increment `j`
6. If `j == len(s)` → return `True`
7. After loop, return `False`

---

## Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = len(s), len(t)

        if S == 0:
            return True
        if S > T:
            return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                j += 1
                if j == S:
                    return True

        return False
