from typing import Optional

# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    oldToNew = {}

    def cloneNode(node):
      if not node:
          return None
          
      # clone already exists
      if node in oldToNew:
          return oldToNew[node]
      
      # create copy of old node and add it to HM
      copy = Node(node.val)
      oldToNew[node] = copy

      # create copy of every neighbor
      # add neighbors to node copy
      for neighbor in node.neighbors:
        neighborCopy = cloneNode(neighbor)
        copy.neighbors.append(neighborCopy)

      return copy

    return cloneNode(node)