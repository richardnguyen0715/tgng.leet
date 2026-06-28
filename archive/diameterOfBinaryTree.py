from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Diameter có thể đi qua Root hoặc không.
        # 1. Đi qua root
        # 2. Không đi qua root
        #  + Nằm hoàn toàn bên cây con trái tức là node trung gian nằm bên trái
        #  + Nằm hoàn toàn bên cây con phải

        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)


            # Lưu lại max hiện tại tính từ node trung gian là node hiện tại
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        depth(root)
        return self.diameter
