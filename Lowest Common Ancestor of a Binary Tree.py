# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Mỗi node đi qua đúng một lần -> Time: O(N)
        # Space: O(H) với H là độ cao của cây <= N -> Space: O(N)

        ans = None
        def dfs(node):
            nonlocal ans

            if not node:
                return False, False
            
            pLeft, qLeft = dfs(node.left)
            pRight, qRight = dfs(node.right)

            isPInUSubTree = pLeft or pRight or p == node
            isQInUSubTree = qLeft or qRight or q == node

            if isPInUSubTree and isQInUSubTree and ans is None:
                ans = node
            
            return isPInUSubTree, isQInUSubTree

        dfs(root)
        return ans