from typing import List

# Solution doing binary search inside for loop | Time: O(n log n), Space: O(1)
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
      l, r = 0, len(row)-1

      while l <= r:
        mid = (l + r) // 2

        if row[mid] > target: r = mid - 1
        elif row[mid] < target: l = mid + 1
        else: return True

    return False
  
# Solution using for loop to extend each row into separate array | Time: O(n log n), Space: O(n)
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    extended = []

    for row in matrix:
      extended.extend(row)

    l, r = 0, len(extended)-1

    while l <= r:
      mid = (l + r) // 2

      if extended[mid] > target: r = mid - 1
      elif extended[mid] < target: l = mid + 1
      else: return True

    return False