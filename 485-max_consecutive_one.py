from collections import Counter
from typing import List


class Solution(object):
    def findMaxConsecutiveOnes(self, nums:List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0

        return max_ones
