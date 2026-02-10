# Best Time to Buy and Sell Stock

## Problem
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.  
You want to maximize your profit by choosing **one day to buy** and **a later day to sell**.

Return the maximum profit possible.  
If no profit can be made, return `0`.

---

## Method Used
- Greedy Approach
- Single Pass Traversal

---

## Core Idea
- Buy at the **lowest price so far**
- Sell at the **current price**
- Track the maximum profit during traversal

---

## How It Works (Short & Clear)

- Maintain `min_price` → lowest stock price seen till now
- For each price:
  - Update `min_price` if current price is smaller
  - Calculate profit = `current price - min_price`
  - Update `max_profit` if profit is higher
- Return `max_profit`

---

## Algorithm Steps

1. Initialize `min_price = infinity`
2. Initialize `max_profit = 0`
3. Traverse each price in array:
   - Update minimum buying price
   - Calculate profit if sold today
   - Update maximum profit
4. Return maximum profit

---

## Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
