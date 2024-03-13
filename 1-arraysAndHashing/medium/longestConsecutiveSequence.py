from typing import List

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