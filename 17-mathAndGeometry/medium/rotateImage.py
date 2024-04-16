from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """ Do not return anything, modify matrix in-place instead."""

    l, r = 0, len(matrix) - 1

    while l < r:
      for i in range(r - l):
        t, b = l, r

        # save the top left
        topLeft = matrix[t][l + i]

        # move bottom left into top left
        matrix[t][l + i] = matrix[b - i][l]
        # move bottom right into bottom left
        matrix[b - i][l] = matrix[b][r - i]
        # move top right into bottom right
        matrix[b][r - i] = matrix[t + i][r]
        # move top left into top right
        matrix[t + i][r] = topLeft
          
      r -= 1
      l += 1
        