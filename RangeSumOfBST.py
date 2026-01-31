from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:


        ans = 0
        def dfs(node):
            nonlocal ans, low, high
            if not node:
                return

            if low <= node.val <= high:
                ans += node.val
            
            if node.val >= low:
                dfs(node.left)
            if node.val <= high:
                dfs(node.right)
        
        dfs(root)
        return ans
    
    
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = 0
        def dfs(node, small, big):
            nonlocal ans, low, high
            if not node:
                return
            
            if low > big or high < small:
                return

            if low <= node.val <= high:
                ans += node.val
            
            if node.val >= low:
                dfs(node.left, small, node.val)
            if node.val <= high:
                dfs(node.right, node.val, big)
        
        dfs(root, float('-inf'), float('-inf'))
        return ans