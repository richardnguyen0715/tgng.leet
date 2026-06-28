from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        parent = list(range(m * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        for i in range(m):
            for j in range(n):
                current_id = i * n + j
                
                # right
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    neighbor_id = i * n + (j + 1)
                    
                    if find(current_id) == find(neighbor_id):
                        return True
                    
                    union(current_id, neighbor_id)
                
                # down
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    neighbor_id = (i + 1) * n + j
                    
                    if find(current_id) == find(neighbor_id):
                        return True
                    
                    union(current_id, neighbor_id)
        
        return False