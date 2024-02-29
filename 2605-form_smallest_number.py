from typing import List


class Solution(object):
    def minNumber(self, nums1:List[int], nums2:List[int])-> int:
        """
        Input: nums1 = [4,1,3], nums2 = [5,7]
        Output: 15
        Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15
        is the smallest number we can have.
        """
        intersection = list(set(nums1) & set(nums2))

        if len(intersection):
            return min(intersection)
        else:
            return min(int(str(min(nums1)) + str(min(nums2))), int(str(min(nums2)) + str(min(nums1))))
