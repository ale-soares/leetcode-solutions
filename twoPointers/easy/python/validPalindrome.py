import re

# reversing
class Solution:
  def isPalindrome(self, s: str) -> bool:
    new = ''
    for a in s:
      if a.isalpha() or a.isdigit():
        new += a.lower()
    return (new == new[::-1])
  
#two pointers
class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    pattern = re.compile('[\W_]')
    s = re.sub(pattern, '', s)

    if len(s) == 0:
      return True

    left, right = 0, len(s)-1

    while left < right:
      if s[left] != s[right]:
        return False
      left += 1
      right -= 1

    return True