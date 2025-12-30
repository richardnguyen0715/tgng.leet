from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        n = len(grid)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
        visited = set()
        queue = deque()
        queue.append((0, 0, 1)) # x, y, distance

        while queue:
            
            x, y, d = queue.popleft()

            if (x, y) == (n - 1, n - 1):
                return d

            for dx, dy in directions:
                u, v = x + dx, y + dy
                if (0 <= u < n) and (0 <= v < n) and ((u, v) not in visited) and grid[u][v] == 0:
                    queue.append((u, v, d + 1))

        return -1