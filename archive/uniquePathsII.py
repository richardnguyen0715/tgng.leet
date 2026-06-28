from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if ( row == 0 and col == 0 ):
                    dp[row][col] = 1
                elif grid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        for row in dp:
            print(row)
        
        return dp[m-1][n-1]
