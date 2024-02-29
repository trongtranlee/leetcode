from astroid import List


class Solution(object):
    def findLengthOfLCIS(self, nums: List[int])-> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maxLength = 1
        currentLength = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currentLength += 1
                maxLength = max(maxLength, currentLength)
            else:
                currentLength = 1

        return maxLength
