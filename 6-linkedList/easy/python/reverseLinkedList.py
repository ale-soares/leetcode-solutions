# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# Two pointer iterative solution | Time complexity: O(n), Space Complexity: O(1)
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
      # save curr.next before link break
      nxt = curr.next
      # invert pointer
      curr.next = prev

      # update prev and curr
      prev = curr
      curr = nxt

    return prev
  
# Recursive solution | Time complexity: O(n), Space Complexity: O(n)
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    # subproblem: reverse only one node

    # base case, if head is null
    if not head: return None
    
    newHead = head

    # if reversing is still possible
    if head.next:
      newHead = self.reverseList(head.next)
      # reverse link between next node and head
      head.next.next = head

    # if head is the first node in the list
    head.next = None
    return newHead
  
# Recursive solution | Time complexity: O(n), Space Complexity: O(n)
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    def reverse(cur, prev):
      if cur is None: return prev
      else:
        next = cur.next
        cur.next = prev
        
        return reverse(next, cur)

    return reverse(head, None)