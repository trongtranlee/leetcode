from typing import List


class Solution(object):
    def countKDifference(self, nums:List[int], k:int)-> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
