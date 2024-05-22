# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# Iterative solution | Time complexity: O(h) or O(n) in worst case, Space complexity:  O(h) or O(n) in worst case 
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    cur = root
    
    while True:
      # if both p and q's values are bigger than current value, LCA of both is to the right subtree
      if p.val > cur.val and q.val > cur.val:
        cur = cur.right
      # if both p and q's values are less than current value, LCA of both is to the left subtree
      elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
      # If the values of p and q are on opposite sides of root (one is greater, and the other is smaller), root is the LCA
      else:
        return cur