from typing import List

# Hashset solution
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
      if n in hashset:
          return True
      hashset.add(n)
    return False
  
# Pure set solution
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    unique = set(nums)

    if len(unique) == len(nums):
      return False

    return True
        