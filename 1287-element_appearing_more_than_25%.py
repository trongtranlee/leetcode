from collections import Counter
from typing import List


class Solution(object):
    def findSpecialInteger(self, arr:List[int])-> int:
        """
        Input: arr = [1,2,2,6,6,6,6,7,10]
        Output: 6
        """
        arrCounter = Counter(arr)
        threshold = len(arr) // 4
        for value, freg in arrCounter.items():
            if freg > threshold:
                return value
        return 0
