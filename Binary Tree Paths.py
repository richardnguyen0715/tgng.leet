from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []

        def makeAns(arrList):
            return "->".join(arrList)

        def findPath(root, path):

            nonlocal res
            if not root:
                return

            path.append(str(root.val))

            if not root.left and not root.right:
                res.append(path.copy())
                return

            findPath(root.left, path.copy())
            findPath(root.right, path.copy())
        
        findPath(root, [])
        return [makeAns(ans) for ans in res]