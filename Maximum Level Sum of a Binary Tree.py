from collections import deque, defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Beat: 5% time, 7% space
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 1

        dq = deque()
        dq.append((root, 0))
        sumHeight = []
        maxSum = float('-inf') # max sum
        res = -1


        while dq:
            node, height = dq.popleft()

            print("node, val: ", node.val, height)

            if height >= len(sumHeight):
                sumHeight.append(node.val)
            else:
                sumHeight[height] += node.val

            if node.left:
                dq.append((node.left, height + 1))

            if node.right:
                dq.append((node.right, height + 1))


        mx = max(sumHeight)
        for i in range(len(sumHeight)):
            if sumHeight[i] == mx:
                return i + 1
            

# Beat: 86% Time, 16% space
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        result_level = 1
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            # Process tất cả nodes ở level hiện tại
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update result nếu tìm được sum lớn hơn
            if level_sum > max_sum:
                max_sum = level_sum
                result_level = level
            
            level += 1
        
        return result_level


# Beat: 5% time, 7% space
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 1

        flatten = []
        def preOrder(root, height):
            nonlocal flatten
            if not root:
                return
                
            flatten.append((height, root.val))
            preOrder(root.left, height + 1)
            preOrder(root.right, height + 1)
        
        preOrder(root, 1)

        flatten.sort()
        print(flatten)

        curMax = float("-inf")
        curSum = 0
        curHeight = 1
        res = -1

        for node in flatten:
            if node[0] == curHeight:
                curSum += node[1]
            else:
                print("last sum: ", curSum)
                print("last max: ", curMax)
                curHeight = node[0]
                if curSum > curMax:
                    curMax = curSum
                    res = node[0] - 1
                    print("Choose res: ", res - 1)
                curSum = node[1]
        
        # print("final sum: ", curSum)
        # print("final max: ", curMax)
        if curSum > curMax:
            curMax = curSum
            res = curHeight

        return res


# Beat: 8% time, 50% space
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 1

        heightMaps = defaultdict(list)
        def preOrder(root, height):
            nonlocal heightMaps
            if not root:
                return
                
            if height not in heightMaps:
                heightMaps[height] = root.val
            else:
                heightMaps[height] += root.val

            preOrder(root.left, height + 1)
            preOrder(root.right, height + 1)
        
        preOrder(root, 1)

        # print(heightMaps)
        maxVal = float("-inf")
        res = 1
        for key, val in heightMaps.items():
            if val > maxVal:
                maxVal = val
                res = key

        return res
                


# Beat: 86% Time, 70% Space     
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        
        level_sums = []
        
        def dfs(node, level):
            if not node:
                return
            
            # Mở rộng array nếu cần
            if level >= len(level_sums):
                level_sums.append(0)
            
            level_sums[level] += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        # Tìm level có sum lớn nhất
        max_sum = max(level_sums)
        return level_sums.index(max_sum) + 1  # +1 vì level bắt đầu từ 1