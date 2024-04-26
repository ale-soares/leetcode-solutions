import collections
from typing import List

# Time complexity: O(1) - size of the Sudoku board is fixed
# Space complexity: O(1) - size of the sets used for tracking elements in rows, columns, and subgrids is fixed

# Solution using 3 hashsets for rows, columns and squares
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Create dictionaries to keep track of numbers in rows, columns, and sub-boxes
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    # Iterate through each cell in the 9x9 Sudoku board
    for row in range(9):
      for col in range(9):
        num = board[row][col]

        # Skip empty cells represented by "."
        if num == ".": continue

        # Check if the current number is already in current row, column or square
        # If it is, this is not a valid Sudoku
        if (num in rows[row] or 
            num in columns[col] or 
            num in squares[(row // 3, col // 3)]):
            return False

        # Update sets to keep track of encountered numbers
        rows[row].add(num)
        columns[col].add(num)
        squares[(row // 3, col // 3)].add(num)

    # If all cells satisfy Sudoku rules, the board is valid
    return True

# Solution using a single hashset to store tuples for row column and square
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    res = set()

    for i in range(9):
      for j in range(9):
        element = board[i][j]

        if element != '.':
          if (i, element) in res or (element, j) in res or (i // 3, j // 3, element) in res :
            return False
          
          res.add((i, element))
          res.add((element, j))
          res.add((i // 3, j // 3, element))

    return True
  
# Solution using an array to store tuples for row column and square
# Uses a set and compares length of array and set to see if there are duplicate tuples
class Solution(object):
  def isValidSudoku(self, board):
    res = []

    for i in range(9):
      for j in range(9):
        element = board[i][j]

        if element != '.':
          res += [(i, element), (element, j), (i // 3, j // 3, element)]

    return len(res) == len(set(res))