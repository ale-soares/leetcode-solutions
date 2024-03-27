from typing import List

# Iterative solution using memoization (non bottom-up)
class Solution:
  def rob(self, nums: List[int]) -> int:
    nums_len = len(nums)
    # if there is only one element, return it
    if nums_len < 2: return nums[0]

    # create array to store memoized max loot at each index
    memo = [0] * nums_len
    # memoize max loot at first 2 indexes
    memo[0], memo[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, nums_len):
      # fill the rest of the memoized array and use previous values to calculate new ones
      memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])

    return memo[-1]

# Solution using recursion and memoization
class Solution:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [-1] * (n + 1)

    return self.solveDP(nums, 0, n - 1, dp)
  
  def solveDP(self, nums, s, e, dp):
    if s > e:
      return 0

    if s == e:
      return nums[s]

    if dp[s] != -1:
      return dp[s]

    dp[s] = max(nums[s] + self.solveDP(nums, s + 2, e, dp), self.solveDP(nums, s + 1, e, dp))
    return dp[s]
  
# Solution using iterative bottom-up
class Solution:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    return self.helper(nums, n)

  def helper(self, nums, n):
    memo = [0] * (n + 2)

    for i in range(n - 1, -1, -1):
      memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])

    return memo[0]

# Shorter iterative solution
class Solution:
  def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
      temp = max(n + rob1, rob2)
      rob1 = rob2
      rob2 = temp
    return rob2