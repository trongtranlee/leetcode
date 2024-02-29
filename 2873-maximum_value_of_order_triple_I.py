class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_v = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    v = (nums[i] - nums[j]) * nums[k]
                    max_v = max(v, max_v)
        return max_v
