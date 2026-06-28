from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        dq = deque()
        dq.append((root, 0))
        ans = []
        while dq:

            node, node_depth = dq.popleft()

            if node_depth >= len(ans):
                ans.append([node.val])
            else:
                ans[node_depth].append(node.val)

            if node.left:
                dq.append((node.left, node_depth + 1))
            
            if node.right:
                dq.append((node.right, node_depth + 1))

            
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()
            
        return ans
        
            
