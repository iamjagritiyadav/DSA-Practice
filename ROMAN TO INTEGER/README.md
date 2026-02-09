# Roman to Integer

## Problem
Given a Roman numeral string `s`, convert it into its corresponding integer value.

---

## Symbols Mapping

I  -> 1  
V  -> 5  
X  -> 10  
L  -> 50  
C  -> 100  
D  -> 500  
M  -> 1000  

---

## Special Subtraction Cases

- I before V or X → 4, 9
- X before L or C → 40, 90
- C before D or M → 400, 900

Rule:
If a smaller value comes before a larger value, subtract it.
Otherwise, add it.

---

## Method Used
- Hash Map (Dictionary)
- Single Pass Traversal
- Greedy Logic

---

## Core Logic (How It Works)

- Traverse the string from left to right
- For each character:
  - Compare its value with the next character
  - If current < next → subtract current value
  - Else → add current value
- Add the last character at the end

---

## Algorithm Steps

1. Create a dictionary for Roman → Integer values
2. Initialize `total = 0`
3. Loop from index `0` to `len(s) - 2`
4. If `value[s[i]] < value[s[i+1]]`:
   - subtract `value[s[i]]`
5. Else:
   - add `value[s[i]]`
6. Add value of last character
7. Return total

---
## Time Complexity
- Single traversal of string
- O(n)

## Space Complexity
- Constant extra space (fixed dictionary)
- O(1)

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        total += roman[s[-1]]
        return total
