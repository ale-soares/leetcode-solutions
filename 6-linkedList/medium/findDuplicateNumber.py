from typing import List

# Best runtime tortoise and hare solution | Time complexity: O(n), Space complexity: O(1)
class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    slow = 0
    fast = 0
    slow2 = 0

    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]

      if slow == fast: break

    while True:
      slow = nums[slow]
      slow2 = nums[slow2]
      
      if slow == slow2: return slow

# Tortoise and hare solution | Time complexity: O(n), Space complexity: O(1)
class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    
    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]

      if slow == fast: break
    
    slow2 = nums[0]

    while slow != slow2:
      slow = nums[slow]
      slow2 = nums[slow2]

    return slow

# Hashmap solution (incorrect for the problem, not constant space) | Time Complexity: O(n), Space Complexity: O(n)
class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    seen = {}

    for n in nums:
      if n in seen: return n
      seen[n] = True
