from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive solution using depth variable
# Time Complexity - O(n) where n is number of nodes
# Space Complexity: O(h) where h is height of the tree (recursive stack)
class Solution:
  def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
    if not root:
      return depth

    leftDepth = self.maxDepth(root.left, depth + 1)
    rightDepth = self.maxDepth(root.right, depth + 1)

    return max(leftDepth, rightDepth)
  
# Recursive solution without depth variable
# Time Complexity - O(n) where n is number of nodes
# Space Complexity: O(h) where h is height of the tree (recursive stack)
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0

    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)

    return max(left_depth, right_depth) + 1