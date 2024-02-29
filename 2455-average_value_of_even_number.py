class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [a for a in nums if ((a % 2 == 0) and (a % 3 == 0))]
        return 0 if len(res) == 0 else sum(res) // len(res)