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

    for _ in range(n):
        fast = fast.next

    if not fast: return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
  
# Solution using two pointers nth nodes apart | Time complexity: O(n), Space complexity: O(1)
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # add dummy node to beginning of list to have left pointer point to it
    dummy = ListNode(0, head)
    left, right = dummy, head

    # shift right until it has exactly n distance from left
    while n > 0 and right:
      right = right.next
      n -= 1

    # shift pointers until right reaches the end of the list
    # at this point, left will point to the node before the one that needs to be deleted
    while right:
      left = left.next
      right = right.next

    # delete the node at nth from the end and return head of new list
    left.next = left.next.next
    return dummy.next