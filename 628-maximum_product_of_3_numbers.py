from functools import reduce

from astroid import List


class Solution(object):
    def maximumProduct(self, nums:List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_product = nums[-1] * nums[-2] * nums[-3]
        alt_product = nums[0] * nums[1] * nums[-1]

        return max(max_product, alt_product)




