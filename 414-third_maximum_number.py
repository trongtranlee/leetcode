from typing import List


class Solution(object):
    def thirdMax(self, nums: List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums), reverse=True)
        return nums[2] if len(nums) >= 3 else nums[0]






