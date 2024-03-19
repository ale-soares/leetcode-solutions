# Recursive solution using memoization and fibonacci
class Solution:
  def climbStairs(self, n: int) -> int:
    memo = {}
    return self.helper(n, memo)

  def helper(self, n: int, memo:dict[int, int]):
    if n == 0 or n == 1: return 1

    if n not in memo:
      memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
    return memo[n]
  
# Bottom-up iterative solution
class Solution:
  def climbStairs(self, n: int) -> int:
    if n <= 3:
      return n
    n1, n2 = 2, 3

    for i in range(4, n + 1):
      temp = n1 + n2
      n1 = n2
      n2 = temp
    return n2