from typing import List

# Brute force solution | Time complexity: O(n2), Space complexity: O(1)
class Solution:
  def maxArea(self, height: List[int]) -> int:
    max_area = 0

    for l in range(len(height)):
      for r in range(l + 1, len(height)):
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)

    return max_area
  
# More efficient two pointer solution | Time complexity: O(n), Space complexity: O(1)
class Solution:
  def maxArea(self, height: List[int]) -> int:
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
      area = (r - l) * min(height[l], height[r])
      max_area = max(max_area, area)

      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return max_area