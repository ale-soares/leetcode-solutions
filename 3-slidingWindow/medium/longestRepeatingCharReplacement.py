# Solution with more variables to facilitate readability
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    # hashmap counts occurrences of each letter within the curr window -> BABBA ->  count = {a:1, b:3}
    count = {}
    l, longest = 0, 0

    for r in range(len(s)):
      win_right_char, win_left_char = s[r], s[l]
      # get returns default val of zero if the char doesn't exist in map
      count[win_right_char] = 1 + count.get(win_right_char, 0)

      most_common_char = max(count.values())
      
      # checks valid replacements
      # valid: window length - count of most common char is less or equal to num of replacements available
      # BABBA -> window len = 4, count of B = 3 -> 4 - 3 = 1 -> valid replacement
      while(r - l + 1) - most_common_char > k:
        # not a valid windows, so window changes and count updates
        count[win_left_char] -= 1
        l += 1

      # valid windows, update longest curr window size is as big as possible before becoming invalid
      longest = max(longest, r - l + 1)
    
    return longest

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    l, longest = 0, 0

    for r in range(len(s)):
      count[s[r]] = 1 + count.get(s[r], 0)

      while(r - l + 1) - max(count.values()) > k:
        count[s[l]] -= 1
        l += 1

      longest = max(longest, r - l + 1)
    
    return longest