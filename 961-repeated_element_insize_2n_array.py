from collections import Counter

from astroid import List


class Solution(object):
    def repeatedNTimes(self, nums:List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        n = length/2
        numCounter = Counter(nums)
        for num, fre in numCounter.items():
            if numCounter[num] == n:
                return num
        return -1

