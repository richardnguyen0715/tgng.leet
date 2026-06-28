from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        val = root.val
        def findUnValied(root):

            nonlocal val, ans
            if not root:
                return
            
            if root.val != val:
                ans = False
                return
            
            findUnValied(root.left)
            findUnValied(root.right)
        
        findUnValied(root)
        return ans
            
            