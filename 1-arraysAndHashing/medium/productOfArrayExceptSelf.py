from typing import List

# Solution using left and right pointers | Time: O(n) Space: O(n)
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # calculate the prefix product of all elements to the left of i
    # calculate the suffix product of all elements to the right of i
    # the product excluding the element at index i is simply the product of the prefix product and the suffix product

    # initialize two arrays left and right, each of size n, where n is the length of the input array nums
    n = len(nums)
    left = [1] * n
    right = [1] * n
    
    # initialize left[i] to store the product of all elements to the left of nums[i]
    # calculate left array by iterating from left to right and multiplying the previous element's value with the current element.
    for i in range(1, n):
      left[i] = left[i - 1] * nums[i - 1]

    # initialize right[i] to store the product of all elements to the right of nums[i]
    # calculate right array by iterating from right to left and multiplying the previous element's value with the current element
    for i in range(n - 2, -1, -1):
      right[i] = right[i + 1] * nums[i + 1]

    # calculate the result array by multiplying left[i] and right[i] for each index i
    return [left[i] * right[i] for i in range(n)]
  
# Solution using prefix and postfix | O(n)
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * (len(nums))

    for i in range(1, len(nums)):
      res[i] = res[i-1] * nums[i-1]

    postfix = 1

    for i in range(len(nums) - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]

    return res