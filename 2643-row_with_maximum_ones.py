from typing import List


class Solution(object):
    def rowAndMaximumOnes(self, mat:List[List[int]])-> List[int]:
        """
        Input: mat = [[0,0,0],[0,1,1]]
        Output: [1,2]
        Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count.
        So, the answer is [1,2]
        """
        list_max = []
        max_num_one = 0
        res = []

        for row in mat:
            max_num_one = max(max_num_one, row.count(1))
            list_max.append(max_num_one)

        max_value = max(list_max)
        max_index = list_max.index(max_value)

        res.append(max_index)
        res.append(max_value)
        return res

