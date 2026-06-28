from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        # N là số đỉnh, M là số cạnh
        # Time: O(N^2 + M + N^3 + N^2) = O(N^3)
        # Space: O(N^2)
        
        # Chuyển danh sách cạnh thành danh sách kề
        adj = defaultdict(list) # tạo một defaultdict với các phần tử là list sẵn
        
        # Tạo ma trận d chứa khoảng cách giữa đỉnh i - j
        d = [[float("inf") for _ in range(n)] for _ in range(n)] # O(N^2)
        for i in range(n):
            d[i][i] = 0
        
        for a, b, w in edges:  # O(M)
            adj[a].append(b)
            adj[b].append(a)
            d[a][b] = w
            d[b][a] = w
            
        # Sử dụng thuật toán floyd-warshall
        
        # K tượng trưng cho điểm sẽ chèn vào trong i, j
        for k in range(n): # O(N^3)
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][k] + d[k][j]: # Thêm k vào thì khoảng cách bé hơn
                        d[i][j] = d[i][k] + d[k][j]
                        
        
        # Sau khi có được khoảng cách ngắn nhất rồi thì kiểm tra
        min_reachable = float('inf')
        ans = None
        
        for i in range(n): # Xét từng đỉnh # O(N^2)
            
            num_reachable = 0
            
            for j in range(n): # Xét các đỉnh kề
                
                if d[i][j] <= distanceThreshold:
                    num_reachable += 1
            
            if num_reachable <= min_reachable:
                min_reachable = num_reachable
                ans = i
                
        return ans