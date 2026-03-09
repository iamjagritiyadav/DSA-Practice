# Find All Possible Stable Binary Arrays I

## 1. Problem Statement

You are given three integers:

```
zero  → number of 0s that must appear
one   → number of 1s that must appear
limit → maximum allowed consecutive identical values
```

You must construct binary arrays such that:

1. The array contains exactly `zero` occurrences of `0`.
2. The array contains exactly `one` occurrences of `1`.
3. Every subarray whose size is greater than `limit` must contain **both 0 and 1**.

Return the number of such arrays.

Since the result can be very large, return it modulo:

```
10^9 + 7
```

Constraints:

```
1 ≤ zero, one, limit ≤ 200
```

---

# 2. Understanding the Problem Carefully

Before solving the problem, we must clearly understand each keyword.

## Binary Array

A binary array contains only two values:

```
0 and 1
```

Example:

```
[0,1,0,1]
```

---

## Exact Number of Zeros and Ones

The array must contain exactly:

```
zero zeros
one ones
```

Example:

```
zero = 2
one = 1
```

Possible permutations:

```
[0,0,1]
[0,1,0]
[1,0,0]
```

---

## Subarray

A subarray is a **continuous portion of the array**.

Example:

For array:

```
[0,1,0]
```

Subarrays:

```
[0]
[1]
[0]
[0,1]
[1,0]
[0,1,0]
```

---

## Stability Condition

The problem states:

```
Each subarray with length greater than limit must contain both 0 and 1
```

This means:

You cannot have a long block of identical values.

Because if we had:

```
0 0 0 0
```

then the subarray itself contains only `0`.

Therefore the condition simplifies to:

```
No more than 'limit' consecutive 0s
No more than 'limit' consecutive 1s
```

This is the **core idea of the problem**.

---

# 3. Restating the Problem in Simpler Terms

We must count binary arrays where:

```
number of 0s = zero
number of 1s = one
maximum consecutive 0s ≤ limit
maximum consecutive 1s ≤ limit
```

This becomes a **counting problem with constraints on consecutive elements**.

---

# 4. Example Walkthrough

## Example

```
zero = 1
one = 2
limit = 1
```

Limit = 1 means:

```
No two identical numbers can appear consecutively
```

Possible permutations of [1,1,0]:

```
1 1 0
0 1 1
1 0 1
```

Check stability:

```
1 1 0  → invalid (two consecutive 1s)
0 1 1  → invalid (two consecutive 1s)
1 0 1  → valid
```

Answer:

```
1
```

---

# 5. Brute Force Approach

## Idea

Generate **all permutations** of zeros and ones and check whether they satisfy the stability condition.

Steps:

1. Generate all sequences containing `zero` zeros and `one` ones.
2. For each sequence check the maximum consecutive identical values.
3. Count valid sequences.

Example generation:

```
zero = 2
one = 1

Sequences:

001
010
100
```

Then validate each.

---

## Complexity

Total permutations:

```
(zero + one)! / (zero! * one!)
```

Worst case:

```
400 choose 200
```

This number is astronomically large.

Therefore brute force is **impossible** for the given constraints.

---

# 6. Recursive Thinking

Instead of generating full permutations, we build the array step by step.

At each step we decide whether to place:

```
0
or
1
```

But we must ensure:

```
consecutive count ≤ limit
```

State parameters required:

```
zeros left
ones left
last element used
consecutive count
```

Recursive state:

```
dfs(z, o, last, count)
```

Example decision tree:

```
Start
 ├─ place 0
 │   ├─ place 0
 │   └─ place 1
 └─ place 1
     ├─ place 0
     └─ place 1
```

---

## Memoization

Many states repeat.

Example:

```
dfs(5,6,1,2)
```

If computed once we should reuse it.

Memoization reduces repeated computation.

State size roughly:

```
zero × one × limit × 2
```

Worst case:

```
200 × 200 × 200 × 2
≈ 16 million states
```

Memory usage becomes large.

Thus recursion may cause **Memory Limit Exceeded**.

---

# 7. Key Optimization Insight

Tracking `consecutive count` explicitly creates too many states.

Instead we can think differently.

Instead of placing elements one by one, we place **blocks**.

Example:

```
11100011
```

This can be viewed as blocks:

```
111 | 000 | 11
```

Each block size must satisfy:

```
1 ≤ block size ≤ limit
```

This observation removes the need to track consecutive counts.

---

# 8. Dynamic Programming Approach

We define two DP tables.

```
dp0[z][o]
```

Meaning:

```
number of valid arrays using
z zeros
and o ones
ending with 0
```

Similarly:

```
dp1[z][o]
```

Meaning arrays ending with `1`.

---

# 9. Transition Logic

## Ending with 0

The previous block must be ones.

We add a block of zeros of size `k`.

```
1 ≤ k ≤ limit
```

Transition:

```
dp0[z][o] += dp1[z-k][o]
```

---

## Ending with 1

Similarly:

```
dp1[z][o] += dp0[z][o-k]
```

---

# 10. Base Cases

Arrays containing only zeros:

```
dp0[i][0] = 1
if i ≤ limit
```

Arrays containing only ones:

```
dp1[0][j] = 1
if j ≤ limit
```

Because a single block is allowed.

---

# 11. Implementation

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

        for z in range(zero+1):
            for o in range(one+1):

                for k in range(1, min(limit, z)+1):
                    dp0[z][o] = (dp0[z][o] + dp1[z-k][o]) % MOD

                for k in range(1, min(limit, o)+1):
                    dp1[z][o] = (dp1[z][o] + dp0[z][o-k]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
```

---

# 12. Time Complexity

The loops run:

```
zero × one × limit
```

Worst case:

```
200 × 200 × 200
≈ 8 million operations
```

Which is efficient.

---

# 13. Space Complexity

We store two DP tables:

```
200 × 200
```

So:

```
O(zero × one)
```

---

# 14. Edge Cases

### Only zeros

```
one = 0
```

Valid only if:

```
zero ≤ limit
```

---

### Only ones

```
zero = 0
```

Valid only if:

```
one ≤ limit
```

---

### Very large limit

If:

```
limit ≥ zero + one
```

Then every permutation is valid.

Answer becomes:

```
C(zero + one, zero)
```

---

# 15. Pattern Recognition (Interview Insight)

This problem belongs to the category:

```
Dynamic Programming with bounded consecutive elements
```

Similar problems:

```
Paint Fence
Binary strings with no consecutive ones
LeetCode 3130 (Stable Binary Arrays II)
```

Key idea used in many problems:

```
Replace element-by-element construction
with block construction
```

This drastically reduces states.

---

# 16. Final Complexity

```
Time Complexity  : O(zero × one × limit)
Space Complexity : O(zero × one)
```

This solution comfortably works within the constraints.
