# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root:TreeNode)->int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_sum = 0

        # Kiểm tra nếu nút hiện tại là lá trái
        if root.left and not root.left.left and not root.left.right:
            left_sum += root.left.val

        # Đệ quy với cả hai nút con của nút hiện tại
        left_sum += self.sumOfLeftLeaves(root.left)
        left_sum += self.sumOfLeftLeaves(root.right)

        return left_sum
