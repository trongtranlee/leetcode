from typing import List


class Solution(object):
    def differenceOfSum(self, nums:List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = 0
        digit_sum = 0
        for i in nums:
            element_sum += i
            while i > 0:
                digit_sum += (i % 10)
                i //= 10
        return abs(element_sum - digit_sum)
