class Solution(object):
    def arrangeCoins(self, n:int)-> int:
        """
        :type n: int
        :rtype: int
        """
        count = 1
        result = 0
        while n >= count:
            n -= count
            count += 1
            result += 1
        return result

