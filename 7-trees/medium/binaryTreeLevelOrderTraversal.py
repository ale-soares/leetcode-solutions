import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = collections.deque()
    # add root to queue
    q.append(root)

    # run loop while queue is non empty
    while q:
      level = []
      # queue length guarantees looping through one level at a time
      for _ in range(len(q)):
        node = q.popleft()

        if node:
          level.append(node.val)
          # update queue to have left and right values
          q.append(node.left)
          q.append(node.right)
      
      if level:
        res.append(level)
    
    return res