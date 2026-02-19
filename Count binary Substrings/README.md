# Count Binary Substrings

## Problem Statement

Given a binary string `s`, return the number of **non-empty substrings** that:

1. Contain equal number of `0`s and `1`s.
2. All `0`s are grouped consecutively.
3. All `1`s are grouped consecutively.
4. Substrings that repeat are counted multiple times.

### Example 1

Input:

```
s = "00110011"
```

Output:

```
6
```

### Example 2

Input:

```
s = "10101"
```

Output:

```
4
```

---

# Understanding the Pattern

A valid substring always looks like:

```
000111
0011
01
1100
10
```

Notice something important:

Every valid substring consists of **exactly two consecutive groups**:

```
[000][111]
[11][00]
[0][1]
```

That means:

- Equal count of 0s and 1s
- Groups must be adjacent
- No mixing like 0101 inside a single substring

---

# Key Insight

Instead of generating all substrings (which would be O(n²)),
we only need to count consecutive groups.

Example:

```
"00110011"
```

Group lengths:

```
00 → 2
11 → 2
00 → 2
11 → 2
```

Now count valid substrings using:

```
min(previous_group, current_group)
```

Why?

If you have:

```
000 (length 3)
11  (length 2)
```

You can form:

```
01
0011
```

Total = min(3, 2) = 2

---

# Optimal Approach (O(n), O(1))

## Algorithm

1. Initialize:

   * `prev_group = 0`
   * `curr_group = 1`
   * `result = 0`

2. Traverse the string from index 1.

3. If current character equals previous:

   * Increase `curr_group`

4. If different:

   * Add `min(prev_group, curr_group)` to result
   * Set `prev_group = curr_group`
   * Reset `curr_group = 1`

5. After loop ends:

   * Add final `min(prev_group, curr_group)`

---

# Implementation (Python)

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_group = 0
        curr_group = 1
        result = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_group += 1
            else:
                result += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1
        
        result += min(prev_group, curr_group)
        return result
```

---

# Dry Run

## Example 1

```
s = "00110011"
```

Groups:

```
[2, 2, 2, 2]
```

Computation:

```
min(2,2) + min(2,2) + min(2,2)
= 2 + 2 + 2
= 6
```

---

## Example 2

```
s = "10101"
```

Groups:

```
[1,1,1,1,1]
```

Computation:

```
min(1,1) + min(1,1) + min(1,1) + min(1,1)
= 4
```

---

# Complexity Analysis

Time Complexity: **O(n)**
We traverse the string once.

Space Complexity: **O(1)**
Only constant variables are used.

---

# Brute Force Approach (Not Recommended)

* Generate all substrings
* Check each substring for validity

Time Complexity → O(n²)
Will fail for constraints up to 10⁵.

---

# Why This Problem Is Important

This problem teaches:

* Pattern recognition in strings
* Group counting technique
* Optimizing from brute force to linear time
* How local structure determines global count

It appears in variations in:

* String compression problems
* Run-length encoding logic
* Sliding window/group problems

---

# Final Takeaway

You don't need to generate substrings.

Just:

1. Count consecutive groups
2. Add `min(previous_group, current_group)` for each adjacent pair

That’s the entire trick.
