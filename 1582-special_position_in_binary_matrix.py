from typing import List


class Solution(object):
    def numSpecial(self, matList:[List[int]])-> int:
        """
        Input: mat = [[1,0,0],
                      [0,0,1],
                      [1,0,0]]
        Output: 1
        Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
        """
        m, n = len(matList), len(matList[0])
        special_count = 0
        for i in range(m):
            for j in range(n):
                if matList[i][j] == 1:
                    row_zeroes = all(matList[i][col] == 0 for col in range(n) if col != j)
                    col_zeroes = all(matList[row][j] == 0 for row in range(m) if row != i)
                    if row_zeroes and col_zeroes:
                        special_count += 1
        return special_count

