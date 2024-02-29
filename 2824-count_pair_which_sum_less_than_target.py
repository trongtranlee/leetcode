class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for j in range(1, len(nums)):
            for i in range(0, j):
                if nums[i] + nums[j] < target:
                    res += 1
        return res
