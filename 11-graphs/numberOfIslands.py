from collections import deque
from typing import List

# DFS Solution 
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    islandCount = 0
    gridLen = len(grid)

    def dfs(row , column):
      if (row < 0 or column < 0 or row >= gridLen or 
          column >= len(grid[0]) or grid[row][column] != "1"):
        return 

      grid[row][column] = "#"

      dfs(row - 1 , column)
      dfs(row + 1 , column)
      dfs(row , column - 1)
      dfs(row , column + 1)
    
    rows, cols = gridLen, len(grid[0])

    for row in range(rows):
      for column in range(cols):
        if grid[row][column] == "1":
          dfs(row , column)
          islandCount += 1

    return islandCount
  
# BFS Solution
class SolutionBFS:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid: return 0

    rows, cols = len(grid), len(grid[0])
    visited=set()
    islands=0

    def bfs(r,c):
      q = deque()
      visited.add((r,c))
      q.append((r,c))
    
      while q:
        row,col = q.popleft()
        directions= [[1,0],[-1,0],[0,1],[0,-1]]
      
        for dr,dc in directions:
          r,c = row + dr, col + dc
          if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
            q.append((r , c ))
            visited.add((r, c ))

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "1" and (r,c) not in visited:
          bfs(r,c)
          islands +=1

    return islands