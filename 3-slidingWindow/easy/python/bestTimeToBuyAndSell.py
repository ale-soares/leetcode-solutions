from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    res = 0
    
    lowest = prices[0]
    for price in prices:
      if price < lowest:
        lowest = price
      res = max(res, price - lowest)
    return res
  
# Two pointer solution
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    buy, sell, max_profit = 0, 1, 0

    while sell < len(prices):
      #if profitable
      if (prices[buy] < prices[sell]):
        profit = prices[sell] - prices[buy]
        max_profit = max(max_profit, profit)
      #if not profitable
      else:
        buy = sell
      sell += 1

    return max_profit