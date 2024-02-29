from collections import Counter
from typing import List


class Solution(object):
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Input: arr = [1,2,2,1,1,3]
        arrCounter = [1:3, 2:2, 3:1]
        Output: true
        Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
        """
        arrCounter = Counter(arr)
        res = []
        for value, freg in arrCounter.items():
            res.append(freg)
        return len(set(res)) == len(res)


