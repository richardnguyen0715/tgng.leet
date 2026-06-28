from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        flag = False

        def isLeaf(node):
            return node.left is None and node.right is None

        def pathSum(node, target):

            nonlocal targetSum, flag
            if not node:
                return

            target += node.val
            if target == targetSum and isLeaf(node):
                flag = True
                return

            pathSum(node.left, target)
            pathSum(node.right, target)
        
        pathSum(root, 0)

        return flag
