from astroid import List


class Solution(object):
    def dominantIndex(self, nums:List[int])->int:
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        maxNumIndex = nums.index(maxNum)
        for i in range(len(nums)):
            if i != maxNumIndex and maxNum < 2 * nums[i]:
                return -1
        return maxNumIndex

