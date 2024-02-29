from typing import List


class Solution(object):
    def intersect(self, nums1:List[int], nums2:List[int])-> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Dictionary to store the frequency of elements in nums1
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        # List to store the intersection
        intersection = []

        # Iterate through nums2 to find common elements and their frequencies
        for num in nums2:
            if num in freq and freq[num] > 0:
                intersection.append(num)
                freq[num] -= 1

        return intersection
