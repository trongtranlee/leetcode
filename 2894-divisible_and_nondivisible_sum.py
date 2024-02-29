class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        ans = 0

        for i in range(1, n + 1):
            if i % m == 0:
                ans -= i
            else:
                ans += i
        return ans
