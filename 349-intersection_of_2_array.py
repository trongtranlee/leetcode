from typing import List


class Solution(object):
    def intersection(self, nums1:List[int], nums2:List[int])->List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert the lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        # Find the intersection of the two sets
        intersection_set = set1.intersection(set2)
        # Convert the intersection set back to a list and return it
        return list(intersection_set)
