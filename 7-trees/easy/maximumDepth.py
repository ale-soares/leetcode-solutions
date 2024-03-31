from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive DFS solution using depth variable
# Time Complexity - O(n) where n is number of nodes
# Space Complexity: O(h) where h is height of the tree (recursive stack)
class Solution:
  def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
    if not root:
      return depth

    leftDepth = self.maxDepth(root.left, depth + 1)
    rightDepth = self.maxDepth(root.right, depth + 1)

    return max(leftDepth, rightDepth)
  
# Recursive DFS solution without depth variable
# Time Complexity - O(n) where n is number of nodes
# Space Complexity: O(h) where h is height of the tree (recursive stack)
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0

    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)

    return max(left_depth, right_depth) + 1
  
# Iterative BFS Solution
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0

    level = 0
    q = deque([root])

    while q:
      for _ in range(len(q)):
        node = q.popleft()
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)

      level += 1

    return level
  
# Iterative Pre Order DFS Solution
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    max_depth = 0

    while stack:
      node, depth = stack.pop()

      if node:
        max_depth = max(max_depth, depth)

        stack.append([node.left, depth + 1])
        stack.append([node.right, depth + 1])

    return max_depth