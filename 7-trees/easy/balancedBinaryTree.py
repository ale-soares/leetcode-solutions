from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# 1: Using 0 and -1
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
      if not root:
        return 0

      left_height, right_height = dfs(root.left), dfs(root.right)
      if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
        return -1
      
      return 1 + max(left_height, right_height)

    return dfs(root) >= 0

# 2: Using array containing balance and tree height
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # dfs return array with 2 values, first is bool representation of balance and second is tree height
    def dfs(node):
      if not node: return [True, 0]

      l_height, r_height = dfs(node.left), dfs(node.right)

      sides_height_diff = abs(l_height[1] - r_height[1])

      is_balanced = (l_height[0] and r_height[0] and sides_height_diff <= 1)
      height_from_node = max(l_height[1], r_height[1])

      return [is_balanced, 1 + height_from_node]

    return dfs(root)[0]