from typing import List


class Solution(object):
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [2,1,2]
        Output: 5
        Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
        """
        perimeter = 0
        if len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums)):
            if i + 2 < len(nums):
                if nums[i] + nums[i+1] > nums[i+2] and nums[i] + nums[i+2] > nums[i+1] and nums[i+1] + nums[i+2] > nums[i]:
                    sumNum = nums[i] + nums[i+1] + nums[i+2]
                    perimeter = max(perimeter, sumNum)
        return perimeter





