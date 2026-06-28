from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if not root:
            return []

        parent = {}

        # Xây dựng một map chứa parent của các node
        def buildParentMap(node, parentNode):
            if not node:
                return
            
            parent[node] = parentNode

            buildParentMap(node.left, node)
            buildParentMap(node.right, node)
        
        buildParentMap(root, None)

        dq = deque()
        dq.append((target, 0))
        visited = {target}
        result = []

        while dq:
            node, distance = dq.popleft()

            if distance == k:
                result.append(node.val)
            
            # Đi ngược lại dần dần parent, đi xuông theo left, right
            for neighbor in [node.left, node.right, parent[node]]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    dq.append((neighbor, distance + 1))
        
        return result