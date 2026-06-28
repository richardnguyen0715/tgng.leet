from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        result = [[float("inf")] * cols for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    result[i][j] = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_distance = 0

        while queue:
            x, y = queue.popleft()
            current_distance = result[x][y]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and result[new_x][new_y] > current_distance + 1:
                    result[new_x][new_y] = current_distance + 1
                    max_distance = max(max_distance, result[new_x][new_y])
                    queue.append((new_x, new_y))
        
        return max_distance if max_distance != 0 else -1
                    