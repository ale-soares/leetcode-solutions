from typing import List

# Two pointer solution using left and right pointers | Time: O(n) Space: O(1)
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    currentSum = numbers[left] + numbers[right]

    while currentSum != target:
      if currentSum > target:
        right -= 1
      else:
        left += 1

      currentSum = numbers[left] + numbers[right]

    return [left + 1, right + 1]
  
# Two pointer solution using left and right pointers (simplified) | Time: O(n) Space: O(1)
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
      curSum = numbers[l] + numbers[r]

      if curSum > target: r -= 1
      elif curSum < target: l += 1
      else: return [l + 1, r + 1]

# Solution using hashmap to store value and index
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    hashmap = {}

    for i in range(0, len(numbers)):
      complement = target - numbers[i]

      if complement in hashmap:
        return [hashmap[complement] + 1, i + 1]
      hashmap[numbers[i]] = i