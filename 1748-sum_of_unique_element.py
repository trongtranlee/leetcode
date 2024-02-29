class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        unique_sum = 0
        for num, freq in count.items():
            if freq == 1:
                unique_sum += num

        return unique_sum