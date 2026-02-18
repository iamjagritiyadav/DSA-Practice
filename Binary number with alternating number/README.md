# Binary Number with Alternating Bits

## Problem Statement

Given a positive integer `n`, determine whether its binary representation contains alternating bits.

Alternating bits means:

* No two adjacent bits are the same
* Pattern must look like 101010... or 010101...

---

## Understanding Binary Representation

Every integer is stored in binary (base-2 format).

Example conversions:

5  -> 101
7  -> 111
11 -> 1011

Alternating means:

* 101 -> Valid
* 111 -> Invalid (1 and 1 adjacent)
* 1011 -> Invalid (last two bits same)

---

## Core Concept Behind Optimal Solution

We use a mathematical bit manipulation trick.

### Step 1: Right Shift Operator ( >> )

`n >> 1`

Meaning:

* Shifts all bits of n one position to the right
* Drops the last bit
* Adds 0 at the left

Example:

n = 5 (101)

n >> 1 = 010

---

### Step 2: XOR Operator ( ^ )

`^` means Exclusive OR.

Rules of XOR:

0 ^ 0 = 0
1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1

Important property:

* XOR gives 1 when bits are different
* XOR gives 0 when bits are same

If number has alternating bits:

n       = 101010
n >> 1  = 010101

XOR     = 111111

Result becomes all 1s.

---

### Step 3: Property of Numbers with All 1s

A number like:

1      -> 1
3      -> 11
7      -> 111
15     -> 1111

These are numbers of form:

2^k - 1

Such numbers satisfy:

x & (x + 1) == 0

---

### Step 4: AND Operator ( & )

`&` means Bitwise AND.

Rules:

1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

If x = 111 (7)

x + 1 = 1000 (8)

x & (x + 1)

0111
& 1000
------

0000

Result is 0.

---

## Final Logic

1. Compute: x = n ^ (n >> 1)
2. Check if x is of form (2^k - 1)
3. That is verified using: (x & (x + 1)) == 0

If true → alternating bits
If false → not alternating

---

## Python Implementation

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
```

---

## Step-by-Step Example

Example: n = 5

Binary:
5      = 101
5 >> 1 = 010

XOR:
101
010
---

111

Now check:

111 & 1000 = 0

Therefore, True

---

## Complexity Analysis

Time Complexity: O(1)

* Only constant bit operations used

Space Complexity: O(1)

* No extra memory used

---

## Why This Is Optimal

* No loops
* No string conversion
* Pure bit manipulation
* Constant time

This is the most efficient and interview-expected solution.
