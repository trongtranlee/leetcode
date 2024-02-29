from astroid import List


class Solution(object):
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        oddList = []
        evenList = []
        for num in nums:
            if num % 2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evenList[i // 2]
            else:
                nums[i] = oddList[i // 2]

        return nums


