from typing import List


class Solution(object):
    def luckyNumbers(self, matrix:List[List[int]])->List[int]:
        """
        Input: matrix = [[3,7,8],
                        [9,11,13],
                        [15,16,17]]
        Output: [15]
        Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
        """
        min_row_nums = []
        max_col_nums = []
        res = []
        for row in matrix:
            min_row_nums.append(min(row))

        for col in range(len(matrix[0])):
            max_val = float('-inf')
            for row in range(len(matrix)):
                max_val = max(max_val, matrix[row][col])
            max_col_nums.append(max_val)
        for min_num in min_row_nums:
            for max_num in max_col_nums:
                if min_num == max_num:
                    res.append(min_num)
                    return res
