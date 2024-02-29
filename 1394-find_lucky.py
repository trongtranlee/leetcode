from collections import Counter
from typing import List


class Solution(object):
    def findLucky(self, arr:List[int])-> int:
        """
        Input: arr = [1,2,2,3,3,3]
        Output: 3
        Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
        """
        arrCounter = Counter(arr)
        res = []

        for num, freg in arrCounter.items():
            if num == freg:
                res.append(num)
        if not res:
            return -1
        return max(res)
