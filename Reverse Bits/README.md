# Reverse Bits

## Problem Statement

Reverse the bits of a given 32-bit unsigned integer.

You are given an integer `n` and you must return the integer obtained by reversing its binary representation.

---

## Example

### Example 1

Input:

```
n = 43261596
```

Output:

```
964176192
```

Explanation:

```
43261596  -> 00000010100101000001111010011100
964176192 -> 00111001011110000010100101000000
```

---

## Approach (Bit Manipulation)

We reverse bits one by one using bitwise operations.

### Steps:

1. Initialize `result = 0`
2. Loop 32 times (since integer is 32-bit)
3. Extract last bit using `n & 1`
4. Shift result left
5. Add extracted bit
6. Shift `n` right
7. Return result

---

## Python Implementation

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
            
        return result
```

---

## Complexity Analysis

* Time Complexity: O(32) -> O(1)
* Space Complexity: O(1)

---

## Optimization (Follow-up)

If this function is called multiple times:

* Cache reversed values of all 256 possible bytes
* Process the number in 4 chunks (8 bits each)
* Improves performance for repeated calls

---

## Key Concepts Used

* Bitwise AND (`&`)
* Bitwise OR (`|`)
* Left Shift (`<<`)
* Right Shift (`>>`)

---

## Summary

This is a classic bit manipulation problem frequently asked in interviews. The optimal solution runs in constant time and uses no extra space.
