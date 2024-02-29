class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maximum = max(nums)
        ans = 0

        while k:
            ans += maximum
            maximum += 1
            k -= 1

        return ans
