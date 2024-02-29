class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resutl = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                maxi = max(str(nums[i]))
                maxj = max(str(nums[j]))
                if maxi == maxj:
                    max_digit = nums[i] + nums[j]
                    resutl = max(resutl, max_digit)
        return resutl
