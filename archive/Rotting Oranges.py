from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return -1
    
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
            
        if fresh_count == 0:
            return 0
    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0
        
        while queue:
            level = len(queue)
            
            for _ in range(level):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    n_x, n_y = x + dx, y + dy
                    
                    if 0 <= n_x < rows and 0 <= n_y < cols and grid[n_x][n_y] == 1:
                        grid[n_x][n_y] = 2
                        fresh_count -= 1
                        queue.append((n_x, n_y))
            
            if queue:
                result += 1
                
        
        return result if fresh_count == 0 else -1
        