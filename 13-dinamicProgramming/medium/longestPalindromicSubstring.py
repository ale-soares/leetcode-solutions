class Solution:
  def longestPalindrome(self, s: str) -> str:
    substr, substr_len = "", 0
    str_len = len(s)

    for i in range(str_len):
      if str_len % 2 != 0: l, r = i, i
      else: l, r = i, i + 1
      
      while l >= 0 and r < str_len and s[l] == s[r]:
        if (r - l + 1) > substr_len:
          substr = s[l : r + 1]
          substr_len = r - l + 1
        l -= 1
        r += 1

    return substr
  
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