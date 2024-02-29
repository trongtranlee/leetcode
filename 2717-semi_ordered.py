class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        return i + n - 1 - j - (i > j)
