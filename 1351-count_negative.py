from typing import List


class Solution(object):
    def countNegatives(self, grid:List[List[int]])-> int:
        """
        Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        Output: 8
        Explanation: There are 8 negatives number in the matrix.
        """
        count = 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += len(row) - left
        return count

