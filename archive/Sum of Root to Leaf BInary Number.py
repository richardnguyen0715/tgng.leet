# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        cnt = 0
        def preOrder(root, path):
            nonlocal cnt
            if not root:
                return
            
            path.append(str(root.val))
            if not root.left and not root.right:
                res = path.copy()
                cnt += int("".join(res), 2)
            
            preOrder(root.left, path)
            preOrder(root.right, path)
            path.pop()

        preOrder(root, [])

        return cnt
            