class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        temp = [0]*(len(nums) + 1)
        for i in range(len(nums)):
            if not temp[i] and not nums[i]%2 and nums[i] <= threshold:
                temp[i+1] = 1
            elif temp[i] and nums[i] <= threshold and nums[i-1]%2 != nums[i]%2:
                temp[i+1] = temp[i] + 1
            elif temp[i] and nums[i] <= threshold and not nums[i]%2:
                temp[i+1] = 1
        return max(temp)