from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root: return False
    if self.isSameTree(root, subRoot): return True

    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

  def isSameTree(self, r: Optional[TreeNode], s: Optional[TreeNode]):
    if r and s:
      return r.val == s.val and self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right) 
    return r is s