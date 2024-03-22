from typing import List

# Bottom-up solution appending 0 to the end of the array | O(n)
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    cost.append(0)

    for i in range(len(cost) - 3, -1, -1):
      cost[i] += min(cost[i + 1], cost[i + 2])
    
    return min(cost[0], cost[1])
  
# Solution creating n variable with cost length | O(n)
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)

    for i in range(2, len(cost)):
      cost[i] += min(cost[i - 1], cost[i - 2])

    return min(cost[n - 1], cost[n - 2])
  
# Solution using recursion and memoization
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    cost.append(0)
    steps = len(cost) - 1
    memo = {}

    def helper(step, memo):
      if step <= 1: return cost[step]

      if step not in memo: 
        min_step = min(helper(step - 1, memo), helper(step - 2, memo))
        memo[step] = cost[step] + min_step
      
      return memo[step]

    return helper(steps, memo)