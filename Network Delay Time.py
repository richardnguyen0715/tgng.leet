from heapq import heappop, heappush
from typing import List
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        # Chuyển từ danh sách cạnh sang danh sách kề
        adj = defaultdict(list)
        weight = {}
        for u, v, w in times:
            adj[u].append(v)
            weight[(u, v)] = w
        
        # Danh sách chứa khoảng cách ngắn nhất từ đỉnh k đến các đỉnh khác
        dis = [float('inf')] * (n + 1) # Do ko sử dụng cạnh 0, đi từ n = 1
        
        dis[k] = 0 # Cạnh gốc
        
        heap = [(0, k)]
        fixed = set()
        
        while heap:
            disU, u = heappop(heap)
            
            if u in fixed:
                continue
            
            fixed.add(u)
            
            # Xét các cạnh kề của u
            
            for v in adj[u]:
                if v not in fixed and dis[v] > dis[u] + weight[(u, v)]:
                    dis[v] = dis[u] + weight[(u, v)]

                    # Trả lại cho heap phần tử đỉnh hiện tại với khoảng cách vừa được cập nhật
                    heappush(heap, (dis[v], v))
        
        # Lấy kết quả distance ra
        
        maxDis = max(dis[1:]) # Loại index 0 vì các cạnh lấy từ 1 -> n
        
        if maxDis == float("inf"): # Không tồn tại đường đi từ một đỉnh khác đến đỉnh gốc
            return -1
    
        return maxDis
            
            