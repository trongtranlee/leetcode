from typing import List


class Solution(object):
    def getCommon(self, nums1:List[int], nums2:List[int])-> int:
        """
        Input: nums1 = [1,2,3], nums2 = [2,4]
        Output: 2
        Explanation: The smallest element common to both arrays is 2, so we return 2.
        """
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            num1, num2 = nums1[i], nums2[j]
            if num1 == num2:
                return num1
            if num1 < num2:
                i += 1
            else:
                j += 1
        return -1


