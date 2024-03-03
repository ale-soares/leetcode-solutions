# Reversing
class Solution:
  def isPalindrome(self, s: str) -> bool:
    new = ''
    for a in s:
      if a.isalpha() or a.isdigit():
        new += a.lower()
    return (new == new[::-1])
  
# Two pointers
class Solution:
  def isPalindrome(self, s: str) -> bool:
    alphnum = "".join(filter(str.isalnum, s))
    clean = alphnum.lower()

    l, r = 0, len(clean) - 1

    while l < r:
      if (clean[l] != clean[r]):
        return False
      
      l += 1
      r -= 1

    return True