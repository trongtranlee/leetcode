# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root: TreeNode)-> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case: If the root is None, the depth is 0
        if not root:
            return 0

        # If the node is a leaf node (no children), return 1
        if not root.left and not root.right:
            return 1

        # If the left subtree is empty, recursively find the minimum depth of the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1

        # If the right subtree is empty, recursively find the minimum depth of the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1

        # If both subtrees are non-empty, recursively find the minimum depth of both subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
