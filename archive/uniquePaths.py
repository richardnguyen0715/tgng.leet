class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        # Gọi DP là số cách đi từ (0,0) đến ô (r,c)
        # DP[m-1][n-1] = result
        
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]
    

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [0] * n # Dp của hàng hiện tại
        dpPrev = [0] * n # Dp của hàng trước đó

        for r in range(m):
            for c in range(n):

                if r == 0 or c == 0:
                    dp[c] = 1

                else:
                    dp[c] = dpPrev[c] + dp[c - 1]
                
            dpPrev, dp = dp, dpPrev

        return dpPrev[n - 1]
