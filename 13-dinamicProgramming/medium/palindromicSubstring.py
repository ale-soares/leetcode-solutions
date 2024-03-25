class Solution:
  def countSubstrings(self, s: str) -> int:
    total_palindromes = 0

    for i in range(len(s)):
      total_palindromes += self.countPalindrome(s, i, i)
      total_palindromes += self.countPalindrome(s, i, i + 1)

    return total_palindromes

  def countPalindrome(self, s, l, r):
    total_palindromes = 0

    while l >= 0 and r < len(s) and s[l] == s[r]:
      total_palindromes += 1
      l -= 1
      r += 1

    return total_palindromes