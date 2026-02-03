from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        dq = deque()
        dq.append((root, 0))
        result = []

        while dq:
            node, height = dq.popleft()
            
            if len(result) <= height:
                result.append([node.val])
            else:
                result[height].append(node.val)

            if node.left:
                dq.append((node.left, height + 1))
            if node.right:
                dq.append((node.right, height + 1))
        
        result.reverse()
        return result