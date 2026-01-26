from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            # Trả về (rob_node, skip_node)
            if not node:
                return (0, 0)

            rob_l, skip_l = dfs(node.left)
            rob_r, skip_r = dfs(node.right)

            # Nếu cướp node này:
            rob_node = node.val + skip_l + skip_r

            # Nếu không cướp node này:
            skip_node = max(rob_l, skip_l) + max(rob_r, skip_r)

            return (rob_node, skip_node)

        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)