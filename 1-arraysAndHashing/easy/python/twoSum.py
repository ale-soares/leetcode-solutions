from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    indexes = {}

    for i, n in enumerate(nums):
      complement = target - n

      if (complement in indexes):
        return [indexes[complement], i]
      indexes[n] = i