from typing import List

# Time Complexity: O(N * M), Space Complexity: O(M)
# where N is the number of coins and M is the target amount

# More readable solution with more descriptive variable names
class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    default_val = amount + 1 # from 0 to amount
    # array will store the minimum number of coins needed for each amount from 0 to amount
    memo = [default_val] * (amount + 1)
    # requires 0 coins to make up an amount of 0
    memo[0] = 0

    # for each "curr_amount", if the current "coin_val" can be used to make up the amount
    # it updates memo[curr_amount] to the minimum of its current value 
    # and 1 + memo[curr_amount - coin_val], where coin_val is the value of the coin being considered
    for curr_amount in range(1, amount + 1):
      for coin_val in coins:
        if curr_amount - coin_val >= 0:
          memo[curr_amount] = min(memo[curr_amount], 1 + memo[curr_amount - coin_val])

    return memo[amount] if memo[amount] != default_val else -1

# Solution using inf as default value
class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [0] + ([float('inf')] * amount)

    for i in range(1, amount + 1):
      for coin in coins:
        if coin <= i:
          dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == float('inf'):
      return -1
    
    return dp[-1]
    
class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
      for c in coins:
        if a - c >= 0:
          dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1