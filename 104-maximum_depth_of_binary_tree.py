# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root: TreeNode)-> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # Return the maximum depth of the left and right subtrees, plus 1 for the current node
        return max(left_depth, right_depth) + 1
