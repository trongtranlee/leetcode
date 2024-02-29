class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        target = list(range(1, n + 1))
        target.append(n)
        return sorted(nums) == target