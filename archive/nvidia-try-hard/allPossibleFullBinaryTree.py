from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int):

        if n % 2 == 0:
            return []

        @lru_cache(None)
        def buildTree(n):
            
            if n == 1:
                return [TreeNode(0)]
        
            res = []
            
            for left in range(1, n, 2):
                right = n - left - 1
                
                leftTrees = buildTree(left)
                rightTrees = buildTree(right)
                
                for l in leftTrees:
                    for r in rightTrees:
                        
                        root = TreeNode(0, l, r)
                        res.append(root)
                
            return res
    
        return buildTree(n)