# Find All Possible Stable Binary Arrays II

## Problem Summary

Given three integers:

* `zero` → number of 0s
* `one` → number of 1s
* `limit` → maximum allowed consecutive identical values

A binary array is **stable** if:

1. It contains exactly `zero` number of `0`s.
2. It contains exactly `one` number of `1`s.
3. No subarray longer than `limit` contains only one type of element.

This means we cannot have **more than `limit` consecutive 0s or 1s**.

We must return the **total number of such arrays** modulo `1e9 + 7`.

---

# Key Insight

The restriction essentially means:

```
max consecutive 0 <= limit
max consecutive 1 <= limit
```

This is a **counting problem with constraints**, which naturally leads to **Dynamic Programming**.

---

# Dynamic Programming Approach

We track:

```
dp0[i][j] → number of arrays using i zeros and j ones ending with 0
dp1[i][j] → number of arrays using i zeros and j ones ending with 1
```

### Transition

If we place `0` at the end:

```
dp0[i][j] = dp0[i-1][j] + dp1[i-1][j]
```

But this allows unlimited zeros, so we must subtract invalid sequences that create
`limit + 1` consecutive zeros.

```
if i > limit:
    dp0[i][j] -= dp1[i-limit-1][j]
```

Similarly for placing `1`:

```
dp1[i][j] = dp0[i][j-1] + dp1[i][j-1]

if j > limit:
    dp1[i][j] -= dp0[i][j-limit-1]
```

---

# Base Cases

If the array contains only zeros:

```
dp0[i][0] = 1 (only if i <= limit)
```

If the array contains only ones:

```
dp1[0][j] = 1 (only if j <= limit)
```

---

# Final Answer

```
(dp0[zero][one] + dp1[zero][one]) % MOD
```

---

# Python Implementation

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1

        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1

        for i in range(zero+1):
            for j in range(one+1):

                if i > 0 and j > 0:
                    dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD

                    if i > limit:
                        dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j]) % MOD

                    dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD

                    if j > limit:
                        dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
```

---

# Complexity Analysis

Time Complexity

```
O(zero × one)
```

Maximum ≈ `10^6` states.

Space Complexity

```
O(zero × one)
```

---

# Interview Takeaway

Whenever you see a constraint like:

```
maximum consecutive elements ≤ k
```

Think of:

* **DP with last element state**
* **Sliding window / prefix subtraction** to remove invalid runs.

This pattern appears in problems related to:

* run length constraints
* bounded consecutive elements
* sequence counting with restrictions.
