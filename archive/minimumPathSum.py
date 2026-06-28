from typing import List




# Time Limit Exceeded
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Time: O(2^(M+N))
        
        import math
        
        res_sum = math.inf


        directions = [(0, 1), (1, 0)]
        visited = set()
        m, n = len(grid), len(grid[0])
        path = []
        
        def dfs(i, j, path):
            nonlocal res_sum, visited, m, n, directions
            if i == m - 1 and j == n - 1:
                # print(path)
                temp_sum = 0
                for x, y in path:
                    temp_sum += grid[x][y]
                temp_sum += grid[i][j]
                res_sum = min(res_sum, temp_sum)
                return
            

            path.append((i, j))
            visited.add((i, j))

            for dx, dy in directions:
                next_x = i + dx
                next_y = j + dy

                if 0 <= next_x < m and 0 <= next_y < n and (next_x, next_y) not in visited:
                    dfs(next_x, next_y, path)
            
            path.pop()
            visited.remove((i, j))
            


        dfs(0, 0, path)

        return res_sum
    


def minPathSum(self, grid: List[List[int]]) -> int:
    
    # Time: O(M + N + M * N) = O(M*N)
    # Space: O(M *N)
    
    m, n = len(grid), len(grid[0])
    
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[j][0]
        
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            
    return dp[m- 1][n- 1]
            


# Tối ưu hóa space khi chỉ cần lưu hàng hiện tại thôi
def minPathSum(self, grid: List[List[int]]) -> int:
    
    # Time: O(M * N)
    # Space: O(N)
    
    m, n = len(grid), len(grid[0])
    
    # Chỉ cần 1 array để lưu hàng hiện tại
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(m):
        dp[0] += grid[i][0]  # Cột đầu tiên
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
    
    return dp[n-1]


# In-place
def minPathSum(self, grid: List[List[int]]) -> int:
    
    # Time: O(M*N)
    # Space: O(1)
    
    m, n = len(grid), len(grid[0])
    
    # Fill first row
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # Fill first column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    
    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[m-1][n-1]


import heapq
def minPathSum(self, grid: List[List[int]]) -> int:
    
    # Dijkstra Algorithms
    # Time: O(MN*Log(MN))
    # Space: O(MN)
    
    m, n = len(grid), len(grid[0])
    pq = [(grid[0][0], 0, 0)]  # (cost, row, col)
    visited = set()
    directions = [(0, 1), (1, 0)]
    
    while pq:
        cost, i, j = heapq.heappop(pq)
        
        if (i, j) in visited:
            continue
            
        visited.add((i, j))
        
        if i == m-1 and j == n-1:
            return cost
        
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                heapq.heappush(pq, (cost + grid[ni][nj], ni, nj))
    
    return -1