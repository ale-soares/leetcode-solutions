from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# 1: Solution using 0 and -1 | Time complexity: O(p + q)
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
      if not root:
        return 0

      left_height, right_height = dfs(root.left), dfs(root.right)
      if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
        return -1
      
      return 1 + max(left_height, right_height)

    return dfs(root) >= 0

# 2: Solution using array containing balance and tree height | Time complexity: O(p + q)
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # dfs return array with 2 values, first is bool representation of balance and second is tree height
    def dfs(node):
      if not node: return [True, 0]

      l_height, r_height = dfs(node.left), dfs(node.right)
      sides_height_diff = abs(l_height[1] - r_height[1])

      is_balanced_from_subtree = l_height[0] and r_height[0]
      is_balanced_from_root = sides_height_diff <= 1

      height_from_node = max(l_height[1], r_height[1])

      # to be balanced, right subtree needs to be balanced, left subtree needs to be balanced and
      # both need to be balanced from root
      return [(is_balanced_from_root and is_balanced_from_subtree), 1 + height_from_node]

    return dfs(root)[0]

# 3: Solution using dictionary to access values by key | Time complexity: O(p + q)
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # dfs return dict with 2 values, first is bool representation of balance and second is tree height
    def dfs(node):
      if not node: 
          return {"balanced": True, "height": 0}

      left, right = dfs(node.left), dfs(node.right)

      sides_height_diff = abs(left["height"] - right["height"])

      is_balanced = (left["balanced"] and right["balanced"] and sides_height_diff <= 1)
      height_from_node = max(left["height"], right["height"])

      return {"balanced": is_balanced, "height": 1 + height_from_node}

    return dfs(root)["balanced"]
  
# 4: Solution using separate helper function | Time complexity: O(p + q)
class Solution:
  def helper(self, root):
    if root is None: return 0

    left_height = self.helper(root.left)
    right_height = self.helper(root.right)

    if left_height == -1 or right_height == -1: return -1
    if abs(left_height - right_height) > 1: return -1

    return 1 + max(left_height, right_height)

  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    answer = self.helper(root)
    return answer != -1