import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
        
class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return None
    
    res = []
    q = collections.deque()
    q.append(root)

    while q:
      rightMost = None
      qLen = len(q)

      for _ in range(qLen):
        node = q.popleft()

        if node:
          rightMost = node
          q.append(node.left)
          q.append(node.right)
      
      if rightMost:
        res.append(rightMost.val)

    return res