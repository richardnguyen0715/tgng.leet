from typing import List
from collections import deque


# Ý tưởng là thay vì thực hiện chạy DFS từ 1 đến 0 thì ta sẽ BFS từ 0 cho tới các ô bằng 1
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])

        # Mặc định khoảng cách bằng vô cực
        result = [[float("inf")] * cols for _ in range(rows)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            current_distance = result[x][y]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and result[new_x][new_y] > current_distance + 1:
                    result[new_x][new_y] = current_distance + 1
                    queue.append((new_x, new_y))
        
        return result



class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        DP approach với 2 passes.
        
        Time: O(m × n)
        Space: O(1) - in-place modification (hoặc O(mn) nếu tạo result mới)
        """
        rows, cols = len(mat), len(mat[0])
        
        # Khởi tạo: 0 giữ nguyên, 1 → infinity
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    mat[r][c] = float('inf')
        
        # Pass 1: Top-left to bottom-right
        # Update từ top và left neighbors
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] > 0:  # Không phải 0
                    if r > 0:
                        mat[r][c] = min(mat[r][c], mat[r-1][c] + 1)
                    if c > 0:
                        mat[r][c] = min(mat[r][c], mat[r][c-1] + 1)
        
        # Pass 2: Bottom-right to top-left
        # Update từ bottom và right neighbors
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] > 0:
                    if r < rows - 1:
                        mat[r][c] = min(mat[r][c], mat[r+1][c] + 1)
                    if c < cols - 1:
                        mat[r][c] = min(mat[r][c], mat[r][c+1] + 1)
        
        return mat