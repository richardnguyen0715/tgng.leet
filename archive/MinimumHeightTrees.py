from collections import deque, defaultdict
from typing import List



# TLE
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case
        if n == 1:
            return [0]
        
        # Build adjacency list
        edgesMap = defaultdict(list)
        for u, v in edges:
            edgesMap[u].append(v)
            edgesMap[v].append(u)
        
        results = []
        
        # BFS từ mỗi node để tìm height của tree khi node đó làm root
        for root in range(n):
            dq = deque()
            dq.append((root, 0))
            visited = set()
            max_height = 0  # Thay đổi: track max height thay vì res
            
            while dq:
                node, height = dq.popleft()
                
                if node in visited:  # Skip nếu đã visit
                    continue
                    
                visited.add(node)
                max_height = max(max_height, height)  # Update max height
                
                # Thêm tất cả neighbors chưa visit
                for neighbor in edgesMap[node]:
                    if neighbor not in visited:
                        dq.append((neighbor, height + 1))
            
            results.append((root, max_height))
        
        # Tìm minimum height
        min_height = min(result[1] for result in results)
        
        # Trả về tất cả roots có min height
        ans = []
        for root, height in results:
            if height == min_height:
                ans.append(root)
        
        return ans
    
    
    
from collections import defaultdict, deque


# Sắp xếp topo
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge cases
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        
        # Build adjacency list và đếm degree
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # Tìm tất cả leaf nodes (degree = 1)
        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        remaining = n
        
        # Loại bỏ leaves từng lớp cho đến khi còn 1-2 nodes
        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            
            # Xử lý tất cả leaves hiện tại
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                
                # Loại bỏ leaf khỏi neighbors
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                # Nếu neighbor trở thành leaf mới
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)
    
    
nums = [1,2,3]
nums.reverse()