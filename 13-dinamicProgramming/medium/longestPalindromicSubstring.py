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