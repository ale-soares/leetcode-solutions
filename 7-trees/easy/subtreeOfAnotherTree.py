from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Shorter solution with two separate functions
# Time complexity: O(r * s) -> r is the number of nodes in the root tree and s is the number of nodes in the subRoot tree
# Space complexity: O(h) -> where h is the height of the root tree due to the recursive calls
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root: return False
    if self.isSameTree(root, subRoot): return True

    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

  def isSameTree(self, r: Optional[TreeNode], s: Optional[TreeNode]):
    if r and s:
      return r.val == s.val and self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right) 
    return r is s
  
# Longer solution with two separate functions
# Time complexity: O(r * s) -> r is the number of nodes in the root tree and s is the number of nodes in the subRoot tree
# Space complexity: O(h) -> where h is the height of the root tree due to the recursive calls
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot: return True
    if not root: return False

    if self.isSameTree(root, subRoot): return True
    return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)

  def isSameTree(self, r, s):
    if not r and not s: return True
    if not r or not s or r.val != s.val: return False

    same_right = self.isSameTree(r.right, s.right)
    same_left = self.isSameTree(r.left, s.left)

    return same_right and same_left
