from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        

        def sumSide(root):
            if not root:
                return 0
            return sumSide(root.left) + sumSide(root.right) + root.val

        nodeValArray = []
        def calcTilt(root):
            nonlocal nodeValArray
            if not root:
                return
            
            nodeValArray.append(abs(sumSide(root.left) - sumSide(root.right)))
            calcTilt(root.left)
            calcTilt(root.right)
        
        calcTilt(root)
        return sum(nodeValArray)
            

            
            
            