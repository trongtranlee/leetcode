from typing import List


class Solution(object):
    def sumZero(self, n:int)-> List[int]:
        """
        Input: n = 5
        Output: [-7,-1,1,3,4]
        Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
        """
        res = []
        if n % 2 == 0:
            for i in range(1,(n/2)+1):
                res.append(-i)
                res.append(i)
        else:
            res.append(0)
            for i in range(1,((n-1)/2)+1):
                res.append(-i)
                res.append(i)
        return res


