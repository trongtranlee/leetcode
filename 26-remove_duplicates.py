# Definition for singly-linked list.
from typing import Optional


class List(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        k = 1  # Initialize unique_index to 1 since the first element is always unique
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k