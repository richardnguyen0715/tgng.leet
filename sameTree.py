from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compareTree(p, q):
            if p is None and q is None:
                return True
            
            # Nếu chỉ 1 trong 2 là None
            if p is None or q is None:
                return False

            if q.val == p.val and compareTree(p.left, q.left) and compareTree(p.right, q.right):
                return True
            return False

        return compareTree(p, q)