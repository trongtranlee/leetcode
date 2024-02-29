from typing import List


class Solution(object):
    def maxProduct(self, nums: List[int]) -> int:
        """
        Input: nums = [3,4,5,2]
        Output: 12
        Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is,
        (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
        """
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
