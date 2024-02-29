class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = []
        for i in range(len(nums)):
            prefix = len(set(nums[:i + 1]))
            surfix = len(set(nums[i + 1:]))
            diff.append(prefix - surfix)
        return diff
