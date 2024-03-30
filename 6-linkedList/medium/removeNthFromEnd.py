from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Solution finding length and removing from beginning using list length - n
# Time complexity: O(n), Space complexity: O(1)
class Solution:
  def find_list_length(self, head: ListNode) -> int:
    length = 0
    temp = head

    while temp:
      temp = temp.next
      length += 1

    return length

  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    list_length = self.find_list_length(head)
    node = dummy = ListNode(0)
    dummy.next = head
    traversed = 0

    while traversed < list_length - n:
      node = node.next
      traversed += 1

    node.next = node.next.next
    return dummy.next
  
# Solution using slow and fast pointers | Time complexity: O(n), Space complexity: O(1)
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = head

    for i in range(n):
        fast = fast.next

    if not fast: return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head