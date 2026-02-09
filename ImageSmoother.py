from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m = len(img)
        n = len(img[0])

        res = [[0] * n for _ in range(m)]

        def calSubrounding(img, i, j):
            # top = (i - 1, j)
            # bottom = (i + 1, j)
            # left = (i, j - 1)
            # right = (i, j + 1)
            # upLeft = (i - 1, j - 1)
            # upRight = (i - 1, j + 1)
            # bottomLeft = (i + 1, j - 1)
            # bottomRight = (i + 1, j + 1)
            directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
            totalCell = 0
            countCell = 0
            for dx, dy in directions:
                newX, newY = i + dx, j + dy
                if 0 <= newX < m and 0 <= newY < n:
                    countCell += 1
                    totalCell += img[newX][newY]
            
            return totalCell // countCell
        
        for i in range(m):
            for j in range(n):
                res[i][j] = calSubrounding(img, i, j)
            
        return res

