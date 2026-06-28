class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }
        
        def is_connected(x, y, nx, ny):
            for dx, dy in dirs[grid[nx][ny]]:
                if nx + dx == x and ny + dy == y:
                    return True
            return False
        
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y):
            if (x, y) == (m - 1, n - 1):
                return True
            
            visited[x][y] = True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if is_connected(x, y, nx, ny):
                        if dfs(nx, ny):
                            return True
            return False
        
        return dfs(0, 0)