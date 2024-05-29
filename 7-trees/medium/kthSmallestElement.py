from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive DFS solution
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    res = []

    # run dfs to traverse tree
    def dfs(node):
      if not node: return

      # add every value of node to an array
      dfs(node.left)
      res.append(node.val)
      dfs(node.right)

    dfs(root)
    # return kth smallest from array
    return res[k-1]
  
# Iterative DFS solution
class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    n = 0

    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      n += 1

      if n == k: return curr.val
      
      curr = curr.right