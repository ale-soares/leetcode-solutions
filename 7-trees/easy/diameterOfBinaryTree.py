from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive DFS solution | Time complexity: O(n), Space complexity: O(n)
class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(root):
      # at each node, calculate the length of the longest path passing through that node
      # which is the sum of the heights of its left and right subtrees
      # keep track of the maximum diameter encountered so far
      nonlocal diameter

      if not root: return 0

      left_height, right_height = dfs(root.left), dfs(root.right)
      diameter = max(diameter, left_height + right_height)

      return 1 + max(left_height, right_height)

    dfs(root)
    return diameter