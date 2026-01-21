# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional



# Beat: 34% time, 5.68% space
# Time: O(N + N + K) = O(N)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        # problem: -> build heap tốn thời gian và tốn thêm space
         
        import heapq

        heap_tree = []

        def treeTravel(root):
            nonlocal heap_tree
            if root == None:
                return
            
            heap_tree.append(root.val)
            treeTravel(root.left)
            treeTravel(root.right)

        treeTravel(root) # O(N)
        print(heap_tree)
        
        heapq.heapify(heap_tree) # O(N)
        print(heap_tree)

        for i in range(0, k - 1):
            heapq.heappop(heap_tree)
        
        return heapq.heappop(heap_tree)
    


# Beat: 42% time, 5.68% space
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ele_pos = [0] * 10001
        
        # problem: chỉ thấy phí khi số nhỏ

        def treeTravel(root):
            nonlocal ele_pos
            if root == None:
                return
            ele_pos[root.val] = 1
            treeTravel(root.left)
            treeTravel(root.right)

        treeTravel(root)
        j = 0
        cnt = 0
        while cnt < k and j < 100001:
            if ele_pos[j] == 1:
                cnt += 1
                print(cnt)
            j += 1
        
        return j - 1
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Beat: 100% time, 5.69% space
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Optimize: Chỉ lưu theo max_val trong dãy thôi
        
        import math
        vals_list = []
        max_val = math.inf * (-1)

        def treeTravel(root):
            nonlocal vals_list, max_val
            if root == None:
                return
            vals_list.append(root.val)
            if root.val > max_val:
                max_val = root.val
                
            treeTravel(root.left)
            treeTravel(root.right)
        treeTravel(root)
       
        ele_pos = [0] * (max_val + 1)
        for i in vals_list:
            ele_pos[i] = 1

        j = 0
        cnt = 0
        while cnt < k and j < (max_val + 1):
            if ele_pos[j] == 1:
                cnt += 1
                print(cnt)
            j += 1
        
        return j - 1
        


