from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

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