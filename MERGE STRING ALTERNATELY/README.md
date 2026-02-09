# Merge Strings Alternately

## Method Used
- Two Pointer Technique
- Alternating Merge

---

## How It Works (Short & Clear)

- Use two pointers:
  - `a` → index for `word1`
  - `b` → index for `word2`
- Pick characters alternately:
  - first from `word1`
  - then from `word2`
- Continue until one string ends
- Append remaining characters of the longer string
- Join the list to form final string

---

## Algorithm Steps

1. Initialize pointers `a = 0`, `b = 0`
2. While `a < len(word1)` and `b < len(word2)`:
   - append `word1[a]`
   - append `word2[b]`
3. Append leftover characters (if any)
4. Return merged string

---
## Time Complexity
- Each character visited once
- O(n + m)
  - n = len(word1), m = len(word2)

## Space Complexity
- Extra list used to store result
- O(n + m)

## Code

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []

        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1

        while a < A:
            s.append(word1[a])
            a += 1

        while b < B:
            s.append(word2[b])
            b += 1

        return ''.join(s)
