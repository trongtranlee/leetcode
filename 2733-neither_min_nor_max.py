from typing import List


class Solution(object):
    def findNonMinOrMax(self, nums:List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal, maxVal = min(nums), max(nums)
        for n in nums:
            if n != minVal and n != maxVal:
                return n
        return -1
