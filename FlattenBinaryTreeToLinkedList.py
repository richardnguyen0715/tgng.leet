from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Space: O(N), Time: O(N)
# Beat: 100% Time, 5% Space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None
        
        order_list = []

        def preOrder(root):
            nonlocal order_list
            if root == None:
                return
            
            order_list.append(root)
            # if root not in hash_map:
            #     hash_map[root] = []
            # else:
            #     if root.left != None:
            #         hash_map[root].append(root.left)
            #     if root.right != None:
            #         hash_map[root].append(root.right)
            
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)

        for i in range(len(order_list) - 1):
            order_list[i].left = None
            order_list[i].right = order_list[i + 1]

        
        return order_list[0]


