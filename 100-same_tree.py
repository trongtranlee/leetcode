# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode)-> bool:
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case: If both nodes are None, they are equal
        if not p and not q:
            return True
            # If one of the nodes is None or their values are different, they are not equal
        if not p or not q or p.val != q.val:
            return False
            # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)