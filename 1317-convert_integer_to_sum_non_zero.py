from typing import List


class Solution(object):
    def getNoZeroIntegers(self, n:int)-> List[int]:
        """
        Input: n = 2
        Output: [1,1]
        Explanation: Let a = 1 and b = 1.
        Both a and b are no-zero integers, and a + b = 2 = n.
        """
        res = []
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n - i):
                res.append(i)
                res.append(n - i)
                return res

