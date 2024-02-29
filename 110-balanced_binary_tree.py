# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root: TreeNode)-> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Helper function to calculate the height of a subtree
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        # Helper function to check if the tree rooted at a node is height-balanced
        def is_balanced_helper(node):
            if not node:
                return True
            left_height = height(node.left)
            right_height = height(node.right)
            # Check if the difference in height between left and right subtrees is <= 1
            if abs(left_height - right_height) > 1:
                return False
            # Recursively check if both left and right subtrees are height-balanced
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)

        return is_balanced_helper(root)
