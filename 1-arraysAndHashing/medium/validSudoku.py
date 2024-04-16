import collections
from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Create dictionaries to keep track of numbers in rows, columns, and sub-boxes
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    # Iterate through each cell in the 9x9 Sudoku board
    for row in range(9):
      for col in range(9):
        num = board[row][col]

        # Skip empty cells represented by "."
        if num == ".": continue

        # Check if the current number violates Sudoku rules
        if (num in rows[row] or 
            num in columns[col] or 
            num in boxes[(row // 3, col // 3)]):
            return False

        # Update sets to keep track of encountered numbers
        rows[row].add(num)
        columns[col].add(num)
        boxes[(row // 3, col // 3)].add(num)

    # If all cells satisfy Sudoku rules, the board is valid
    return True

