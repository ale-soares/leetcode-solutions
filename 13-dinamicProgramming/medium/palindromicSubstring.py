# Solution using "nested" count palindrome function | Time Complexity: O(n^2), Space Complexity: O(1)
class Solution:
  def countSubstrings(self, s: str) -> int:
    s_len, total_palindromes = len(s), 0

    def count_palindrome(l, r):
      count = 0

      while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1

      return count

    for i in range(s_len):
      odd = count_palindrome(i, i)
      even = count_palindrome(i, i + 1)

      total_palindromes += even + odd

    return total_palindromes

# Solution using separate count palindrome function
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