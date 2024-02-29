from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] >= target:
                return i
        return n

