from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True

        def dfs(node):

            # (min, max)
            nonlocal ans
            if not node:
                return float('inf'), float('-inf')
            
            minLeft, maxLeft = dfs(node.left)
            minRight, maxRight = dfs(node.right)

            if maxLeft >= node.val or minRight <= node.val:
                ans = False

            return min(minLeft, node.val), max(maxRight, node.val)

        
        dfs(root)
        return ans