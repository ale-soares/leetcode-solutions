from typing import List

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    rows, columns = len(grid), len(grid[0])
    visited = set()
    maxArea = 0

    def dfs(row, column):
      if (
        row < 0
        or row == rows
        or column < 0
        or column == columns
        or grid[row][column] == 0
        or (row, column) in visited
      ): return 0
      
      visited.add((row, column))

      return (1 + dfs(row + 1, column) + 
                  dfs(row - 1, column) + 
                  dfs(row, column + 1) + 
                  dfs(row, column - 1))

    for r in range(rows):
      for c in range(columns):
        maxArea = max(maxArea, dfs(r, c))

    return maxArea