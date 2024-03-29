class Solution:
  def longestPalindrome(self, s: str) -> str:
    max_substr = ""
    input_len = len(s)

    def expand_from_center(l, r):
      while l >= 0 and r < input_len and s[l] == s[r]:
        l -= 1
        r += 1

      return s[l + 1 : r]

    for i in range(input_len):
      odd = expand_from_center(i, i)
      even = expand_from_center(i, i + 1)
      
      if len(odd) > len(max_substr):
        max_substr = odd
      if len(even) > len(max_substr):
        max_substr = even

    return max_substr
  
# Solution using dynamic programming
class Solution:
  def longestPalindrome(self, s: str) -> str:
    n = len(s)
    start = 0
    max_len = 1
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
      dp[i][i] = True

    # Check substrings of length 2
    for i in range(n - 1):
      if s[i] == s[i + 1]:
        dp[i][i + 1] = True
        start = i
        max_len = 2

    # Check substrings of length 3 or more
    for length in range(3, n + 1):
      for i in range(n - length + 1):
        j = i + length - 1
        if dp[i + 1][j - 1] and s[i] == s[j]:
            dp[i][j] = True
            start = i
            max_len = length

    return s[start:start + max_len]