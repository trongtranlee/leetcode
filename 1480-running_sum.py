from typing import List


class Solution(object):
    def runningSum(self, nums:List[int])->List[int]:
        """
        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
        """
        res = []
        for i in range(1,len(nums)+1):
            res.append(sum(nums[:i]))
        return res

