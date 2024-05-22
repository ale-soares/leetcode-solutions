from typing import Optional

# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random

# Solution using hashmap to map old with new | Time complexity: O(n), Space complexity: O(n)
class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = { None : None }

    cur = head
    while cur:
      # create copy of current node with its value
      copy = Node(cur.val)
      # add copy to HM 
      oldToCopy[cur] = copy
      # move to next iteration
      cur = cur.next

    cur = head
    while cur:
      copy = oldToCopy[cur]
      # add next and random pointers of old node to copy
      copy.next = oldToCopy[cur.next]
      copy.random = oldToCopy[cur.random]
      # move to next iteration
      cur = cur.next

    return oldToCopy[head]