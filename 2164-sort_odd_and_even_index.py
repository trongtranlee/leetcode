from typing import List


class Solution(object):
    def sortEvenOdd(self, nums:List[int])-> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_indices = nums[1::2]
        even_indices = nums[::2]

        odd_indices.sort(reverse=True)
        even_indices.sort()

        rearranged_nums = [0] * len(nums)
        rearranged_nums[1::2] = odd_indices
        rearranged_nums[::2] = even_indices

        return rearranged_nums