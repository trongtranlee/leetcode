# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

            # Find the middle element of the array
        mid = len(nums) // 2

        # Create a new TreeNode with the middle element as the root
        root = TreeNode(nums[mid])

        # Recursively build the left subtree with the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])

        # Recursively build the right subtree with the right half of the array
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
