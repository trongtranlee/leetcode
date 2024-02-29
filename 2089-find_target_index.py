from typing import List


class Solution(object):
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Input: nums = [1,2,5,2,3], target = 2
        Output: [1,2]
        Explanation: After sorting, nums is [1,2,2,3,5].
        The indices where nums[i] == 2 are 1 and 2
        """
        nums.sort()
        res = []
        for index, num in enumerate(nums):
            if num == target:
                res.append(index)
        return res

