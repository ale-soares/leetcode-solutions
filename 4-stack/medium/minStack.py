class MinStack:
  # min stack allows for efficient retrieval of the minimum value in a stack
  # every operation in min stack is O(1)
  # achieved by maintaining two stacks: one for all elements, one for minimum elements
  # time complexity -> push O(1), pop O(1), top O(1), getMin O(1)
  # space complexity -> O(n), where n is the number of elements in the stack
  
  def __init__(self):
    # initialize two lists (stacks)
    self.stack = []
    self.min_stack = []

  def push(self, val: int) -> None:
    # append element to stack
    self.stack.append(val)
    # check if min stack is not empty
    # if it's not empty, calculate the minimum between the current element and the top element of min stack
    # append the minimum to min stack ensuring that minStack always contains the minimum value
    val = min(val , self.min_stack[-1] if self.min_stack else val)
    self.min_stack.append(val)

  def pop(self) -> None:
    # pop the element from both stack and min stack to maintain consistency of stacks
    self.stack.pop()
    self.min_stack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min_stack[-1]