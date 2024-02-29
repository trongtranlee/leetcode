class Solution(object):
    def climbStairs(self, n:int) -> int:
        """
        :type n: int
        :rtype: int
        """
        fib = [1, 1]
        for i in range(n - 1):
            fib.append(fib[0] + fib[1])
            fib = fib[1:]

        return fib[1]