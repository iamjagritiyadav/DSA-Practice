# Binary Watch

## Problem Summary

A binary watch uses:

* 4 LEDs to represent hours (0–11)
* 6 LEDs to represent minutes (0–59)

Each LED represents a binary digit (0 or 1).

Given an integer `turnedOn`, return all possible valid times the watch could represent such that the total number of LEDs that are ON equals `turnedOn`.

### Constraints

* Hour must be between 0 and 11.
* Minute must be between 0 and 59.
* Hour must NOT contain leading zero (e.g., "01:00" invalid → "1:00").
* Minute must always contain two digits (e.g., "10:02" valid, not "10:2").

---

## Approach

Since the total possible combinations are small:

* Hours → 12 possibilities (0–11)
* Minutes → 60 possibilities (0–59)
* Total combinations → 12 × 60 = 720

We can brute-force all combinations.

### Steps

1. Iterate through all hours (0–11).
2. Iterate through all minutes (0–59).
3. Count number of set bits in hour and minute.
4. If total set bits equals `turnedOn`, format the time correctly and add to result.

We use:

```
bin(number).count('1')
```

to count set bits.

---

## Python Implementation

```python
class Solution:
    def readBinaryWatch(self, turnedOn: int):
        result = []
        
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        
        return result
```

---

## Example

### Input

```
turnedOn = 1
```

### Output

```
["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
```

---

## Complexity Analysis

* Time Complexity: O(720) → constant time
* Space Complexity: O(n) → depends on number of valid results

---

## Key Insight

The problem looks like bit manipulation, but brute-force is sufficient because the search space is very small.

No advanced optimization is required.
