from typing import List


class Solution(object):
    def checkXMatrix(self, grid:List[List[int]])-> bool:
        """
        All the elements in the diagonals of the matrix are non-zero.
        All other elements are 0.
        Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
        Output: true
        Explanation: Refer to the diagram above.
        An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
        Thus, grid is an X-Matrix.
        """
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or (i + j) == n - 1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
        return True
