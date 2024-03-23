# Solution using while
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # set to keep track of unique characters in the current substring
    charSet = set()
    # left and right represent the boundaries of the current substring
    # longest variable keeps track of the length of the longest substring encountered
    l, longest = 0, 0

    for r in range(len(s)):
      # if the curr character is present in the set, there are repeating character in substring
      while s[r] in charSet:
        # move the left pointer forward, removing repeating characters from the set
        charSet.remove(s[l])
        l += 1

      # if the current character is not in the set, it is a new unique character
      # insert the character into the set and update the longest if necessary
      charSet.add(s[r])
      longest = max(longest, r - l + 1)

    return longest
  
# Solution using if and while
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    maxLength, left = 0, 0
    charSet = set()
    
    for right in range(n):
      if s[right] not in charSet:
        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)
      else:
        while s[right] in charSet:
          charSet.remove(s[left])
          left += 1
        charSet.add(s[right])
    
    return maxLength