from typing import List

# Time complexity: O(log n), Space complexity: O(1)
class Solution:
  def findMin(self, nums: List[int]) -> int:
    start , end = 0, len(nums) - 1 
    curr_min = nums[0]
    
    while start  <  end :
      mid = start + (end - start ) // 2
      curr_min = min(curr_min, nums[mid])
      
      # right has the min 
      if nums[mid] > nums[end]: start = mid + 1
      # left has the min 
      else: end = mid - 1 
            
    return min(curr_min, nums[start])

# Time complexity: O(log n), Space complexity: O(1)
class Solution:
  def findMin(self, nums: List[int]) -> int:
    left, right = 0 , len(nums) - 1
    result = nums[0]

    while left <= right:
      # if array is already sorted, return min value
      if nums[left] < nums[right]:
        result = min(result, nums[left])
        break
      
      mid = (left + right) // 2
      result = min(result, nums[mid])

      # mid is in left sorted portion, so search to the right
      if nums[mid] >= nums[left]: left = mid + 1
      # mid is in right sorted portion, so search to the left
      else: right = mid - 1

    return result