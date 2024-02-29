class Solution(object):
    def isFascinating(self, n:int)-> bool:
        """
        Input: n = 192
        Output: true
        Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. The resulting number is 192384576.
        This number contains all the digits from 1 to 9 exactly once.
        """
        num = str(n) + str(2 * n) + str(3 * n)
        for i in num:
            if num.count(i) > 1 or '0' in num:
                return False
        return True
