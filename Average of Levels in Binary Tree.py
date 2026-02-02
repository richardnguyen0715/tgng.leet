from typing import Optional, List
from collections import deque
from statistics import mean

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        dq = deque()
        dq.append((root, 0))
        storage = {}
        while dq:
            node, level = dq.popleft()
            if level not in storage:
                storage[level] = [node.val]
            else:
                storage[level].append(node.val)
           
            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))

        res = []
        for key, lst in storage.items():
            res.append(mean(lst))
        
        return res

