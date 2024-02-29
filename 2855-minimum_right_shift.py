from typing import List


class Solution(object):
    def minimumRightShifts(self, nums:List[int])-> int:
        """
        Input: nums = [3,4,5,1,2]
        Output: 2
        Explanation:
        After the first right shift, nums = [2,3,4,5,1].
        After the second right shift, nums = [1,2,3,4,5].
        Now nums is sorted; therefore the answer is 2.
        """
        n = len(nums)
        sorted_nums = sorted(nums)

        for shift in range(n):
            if nums == sorted_nums:
                return shift
            nums = [nums[-1]] + nums[:-1]

        return -1


