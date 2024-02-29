# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root: TreeNode)-> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

            # Count nodes in the left subtree
        left_count = self.countNodes(root.left)

        # Count nodes in the right subtree
        right_count = self.countNodes(root.right)

        # Return total number of nodes
        return left_count + right_count + 1