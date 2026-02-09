from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        originalColor = image[sr][sc]

        def dfs(i , j):

            image[i][j] = color
            visited.add((i, j))
            
            for dx, dy in directions:
                newX, newY = i + dx, j + dy
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited and image[newX][newY] == originalColor:
                    dfs(newX, newY)

        dfs(sr, sc)
        return image
