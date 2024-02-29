from typing import List


class Solution(object):
    def countElements(self, nums:List[int])-> int:
        """
        Input: nums = [11,7,2,15]
        Output: 2
        """
        count = 0
        for i in range(len(nums)):
            smaller, greater = False, False
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        smaller = True
                    elif nums[j] > nums[i]:
                        greater = True
            if smaller and greater:
                count += 1
        return count
