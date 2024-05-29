import collections
from typing import List

# Time complexity: O(n * m) | Space complexity: O(n * m)
class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    # initialize bfs queue
    q = collections.deque()
    fresh, time = 0, 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
      for c in range(cols):
        # if a grid has a value of 1, it contains a fresh orange
        # increase freshAmount variable
        if grid[r][c] == 1: fresh += 1
        # if a grid has a value of 2, it contains a rotten orange
        # add coordinates for all rotten oranges into bfs queue
        if grid[r][c] == 2: q.append((r, c))

    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    
    while q and fresh > 0:
      length = len(q)
      
      for i in range(length):
        # pop coordinates of rotten orange
        r, c = q.popleft()

        for dr, dc in directions:
          row, col = r + dr, c + dc
          # if is in bounds and fresh, make rotten, add to queue and decrease fresh amount
          if (
            row in range(len(grid))
            and col in range(len(grid[0]))
            and grid[row][col] == 1
          ):
            grid[row][col] = 2
            q.append((row, col))
            fresh -= 1
            
      time += 1

    return time if fresh == 0 else -1