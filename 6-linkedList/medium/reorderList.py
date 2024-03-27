# Rearrange the linked list using three steps: 
  # Finding the middle node
  # Reversing the second half
  # Merging the two halves in an alternating pattern

# Time Complexity: Finding middle: O(n), Reversing: O(n), Merging: O(n), Total: O(n)
# Space Complexity: Extra pointers: O(1), Recursive reverse call stack: O(n) in worst-case

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverse(self, head):
    if not head:
      return None
    
    # Keep a prev pointer to set prev->next to NULL later
    prev = None
    curr = head
    nextNode = None

    while curr:
      nextNode = curr.next
      curr.next = prev
      prev = curr
      curr = nextNode
      
    return prev

  def merge(self, list1, list2):
    # Store list1.next as nextNode
    # Connect list1.next to list2
    # Move list1 to nextNode
    # Move list2 to list2.next

    while list2:
      nextNode = list1.next
      list1.next = list2
      list1 = list2
      list2 = nextNode

  def reorderList(self, head):
    if not head or not head.next:
      return

    # Initialize slow and fast pointers to head
    slow = head
    fast = head
    prev = head

    # While fast and fast.next exist, move slow one step and fast two steps
    while fast and fast.next:
      prev = slow
      fast = fast.next.next
      slow = slow.next
    
    # Slow will now point to the middle node
    # Prev next to null marks the end of the first half
    prev.next = None

    # Call reverse(slow) to reverse the list starting from slow
    # This returns the new head of the reversed portion (list2)
    list1, list2 = head, self.reverse(slow)

    self.merge(list1, list2)