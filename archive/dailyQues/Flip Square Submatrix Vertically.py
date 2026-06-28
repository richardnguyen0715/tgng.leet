from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        l = x
        r = l + k - 1

        while l <= r:
            l_row = grid[l]
            r_row = grid[r]

            for idx in range(y, y + k):
                l_row[idx], r_row[idx] = r_row[idx], l_row[idx]
            
            l += 1
            r -= 1
        return grid


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        boundCol = min(n - 1, y + k - 1)
        boundRow = min(m - 1, x + k - 1)

        print(boundCol)
        print(boundRow)

        count = 0
        for i in range(m):
            flag = False
            for j in range(n):
                if x <= i <= (boundRow - k//2) and y <= j <= boundCol:
                    grid[i][j], grid[boundRow - count][j] =  grid[boundRow - count][j], grid[i][j]
                    flag = True
            if flag:
                count += 1
        
        for row in grid:
            print(row)
        
        return grid