# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


class Solution(object):
    def firstBadVersion(self, n:int)-> int:
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
