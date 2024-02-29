from astroid import List

class Solution(object):
    def isMonotonic(self, nums:List[int])->bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        sorted_nums_reversed = sorted(nums, reverse=True)

        return nums == sorted_nums or nums == sorted_nums_reversed
