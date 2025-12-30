from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(a, b):

            visited.add((a, b))

            for dx, dy in directions:
                x, y = a + dx, b + dy

                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and (x, y) not in visited:
                    dfs(x, y)



        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1

        return ans
    
def solutionWithBFS(grid: List[List[str]]):
    
    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    
    def bfs(a, b):
        
        dq = deque()
        visited.add((a, b))
        dq.append((a, b))
        
        
        # deque: [(a, b), (..., ...)]
        while(dq):
            u, v = dq.popleft()
            
            for dx, dy in directions:
                x, y = u + dx, v + dy
                
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1" and (x,y) not in visited:
                    visited((x, y))
                    dq.append((x, y))
                    
    
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and (i, j) not in visited: # Connected components
                bfs(i ,j)
                ans += 1
                
    
    return ans
                