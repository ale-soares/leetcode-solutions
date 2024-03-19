from typing import List

# Solution using start and end
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    length = 0

    for start in nums:
      if start - 1 not in num_set:
        end = start + 1
        while end in num_set:
          end += 1
        length = max(length, end - start)
    
    return length
  
# Solution using length and longest
  class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      num_set = set(nums)
      longest = 0

      for n in nums:
        if (n - 1) not in num_set:
          length = 1
          while (n + length) in num_set:
            length += 1
          longest = max(length, longest)
      
      return longest