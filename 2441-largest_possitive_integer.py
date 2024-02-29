from typing import List


class Solution(object):
    def findMaxK(self, nums:List[int])-> int:
        """
        Input: nums = [-1,2,-3,3]
        Output: 3
        Explanation: 3 is the only valid k we can find in the array.
        """
        max_num = None
        for num in nums:
            if -num in nums:
                max_num = max(max_num, abs(num)) if max_num is not None else abs(num)
        return int(max_num) if max_num is not None else -1

