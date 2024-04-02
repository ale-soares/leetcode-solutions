# The last bracket that is opened must also be the first one to be closed
# use stack because of Last In, First Out (LIFO) principle

class Solution:
	def isValid(self, s: str) -> bool:
		pairs = {")": "(", "]": "[", "}": "{"}
		stack = []

		for char in s:
			if char in pairs:
				# if the bracket is a closing one, use the pairs dictionary to check if it's
					# the correct type of bracket
				# pop the last opening bracket encountered, find the corresponding closing bracket
					# and compare it with the current bracket in the loop
				if stack and stack[-1] == pairs[char]:
					stack.pop()
				# if the wrong type of closing bracket is found, exit early and return false
				else:
					return False
			else:
				# if the bracket is an opening one, push it on to the stack
				stack.append(char)
		
		# if we make it all the way to the end and all open brackets have been closed, 
			# the stack should be empty.
		return not stack
	
class Solution:
	def isValid(self, s: str) -> bool:
		open_from_closed = {')': '(', ']': '[', '}': '{'}
		opening = []

		for char in s:
			if char in open_from_closed:
				if opening and opening[-1] == open_from_closed[char]:
					opening.pop()
				else:
					return False
			else:
				opening.append(char)

		is_empty_stack = not opening
		return is_empty_stack