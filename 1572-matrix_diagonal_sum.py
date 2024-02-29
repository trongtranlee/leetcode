from typing import List


class Solution(object):
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Input: mat = [[1,2,3],
                      [4,5,6],
                      [7,8,9]]
        Output: 25
        Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
        Notice that element mat[1][1] = 5 is counted only once.
        """
        length = len(mat)
        total = 0
        for row in range(len(mat)):
            for col in range(len(mat)):
                if row == col or row + col == length-1:
                    total += mat[row][col]
        return total
