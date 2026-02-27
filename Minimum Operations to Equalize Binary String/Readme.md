# Minimum Operations to Equalize Binary String

## Problem Summary

Given a binary string `s` and an integer `k`, in one operation exactly `k` distinct indices must be selected and flipped (0 ↔ 1). The goal is to determine the minimum number of operations required to make the string consist entirely of '1'. If it is impossible, return -1.

---

## Key Observations

1. The operation is independent of index positions. Only the **count of zeros** matters.

2. Let:

   * `n = len(s)`
   * `m = current number of zeros`

3. In one operation, if we flip `c` zeros and `k - c` ones, the new zero count becomes:

   m' = m + k - 2c

4. The value of `c` must satisfy:

   max(k - (n - m), 0) ≤ c ≤ min(m, k)

5. The resulting values of `m'` form a continuous interval with fixed parity.

This transforms the problem into a **state transition problem over zero counts**.

---

## Issues Faced During Problem Solving

### 1. Incorrect Mathematical Shortcuts

Initial attempts relied on simplified formulas such as:

* ceil(z / k)
* Parity-based direct conditions

These approaches failed because:

* Zero count does not strictly decrease.
* The number of zeros can increase in intermediate states.
* Transitions depend on how many zeros are selected in each operation.

Conclusion: A direct greedy or closed-form formula is insufficient.

---

### 2. Incorrect Parity Assumptions

Several attempts assumed:

* If k is even, zero count parity must match.
* If k is odd, solution always exists.

These conditions are necessary in some cases but not sufficient. They do not capture full transition behavior.

Conclusion: Parity alone does not determine reachability.

---

### 3. Naive BFS Causing Time Limit Exceeded

A direct BFS over zero counts with linear scanning of ranges resulted in O(n^2) behavior.

Problem:

* For each state, scanning entire candidate set to find valid transitions.

Why it fails:

* n can be up to 10^5.
* Repeated scanning causes excessive time complexity.

---

## Final Correct Approach

### State Modeling

Each possible zero count from 0 to n is treated as a node.

We perform BFS starting from the initial zero count.

For a state `m`, the reachable next states form an interval:

* Lower bound: lnode = m + k - 2 * c2
* Upper bound: rnode = m + k - 2 * c1

Where:

* c1 = max(k - (n - m), 0)
* c2 = min(m, k)

All values in [lnode, rnode] share the same parity.

---

### Optimization Strategy

To avoid scanning all states repeatedly:

* Maintain two ordered collections:

  * One for even zero counts
  * One for odd zero counts
* Use binary search to extract only values within the valid interval.
* Remove visited states immediately to ensure each state is processed once.

This ensures:

* Each state is inserted once
* Each state is removed once
* Each removal costs O(log n)

---

## Complexity Analysis

Time Complexity: O(n log n)

Space Complexity: O(n)

This satisfies constraints up to n = 10^5.

---

## Important Lessons from This Problem

1. When operations depend only on counts, reduce dimensionality of state.
2. Avoid premature mathematical generalization without full transition analysis.
3. If transitions form intervals, combine BFS with ordered structures.
4. Always analyze worst-case complexity before finalizing approach.
5. Necessary conditions (like parity) are not always sufficient conditions.

---

## Implementation Strategy Summary

1. Count initial zeros.
2. Perform BFS over zero counts.
3. For each state, compute reachable interval.
4. Use parity-separated ordered sets.
5. Remove visited states immediately.
6. Return distance when zero count reaches 0.
7. If unreachable, return -1.

---

This problem demonstrates how a seemingly combinatorial string problem reduces to graph traversal with interval transitions and parity constraints.
