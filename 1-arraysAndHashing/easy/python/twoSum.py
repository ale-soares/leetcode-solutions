from typing import List

# Time complexity: O(n), Space complexity: O(n)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    indexes = {}

    for i, n in enumerate(nums):
      complement = target - n

      if (complement in indexes):
        return [indexes[complement], i]

      indexes[n] = i

# Time complexity: O(n), Space complexity: O(n)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
      numMap[nums[i]] = i

    for i in range(n):
      complement = target - nums[i]
      if complement in numMap and numMap[complement] != i:
        return [i, numMap[complement]]