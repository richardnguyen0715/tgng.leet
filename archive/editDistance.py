from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # # Topdown DP
        # @lru_cache(None)
        # def dp(i, j):
        #     if i == 0:
        #         return j
        #     if j == 0:
        #         return i
            
        #     if word1[i - 1] == word2[j - 1]:
        #         return dp(i-1, j-1)
            
        #     return min(dp(i, j -1), dp(i-1, j), dp(i-1, j -1)) + 1
        
        # m, n = len(word1), len(word2)

        # return dp(m, n)
        
        # BottomUp DP
        # m, n = len(word1), len(word2)
        # dp = [[-1] * (n+1) for _ in range(m+1)]
        # for i in range(m+1):
        #     for j in range(n+1):
        #         if i == 0:
        #             dp[i][j] = j
        #         elif j == 0:
        #             dp[i][j] = i
        #         elif word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        # return dp[m][n]
    
    
        # Bottom Up DP with optimized space
        m, n = len(word1), len(word2)
        dp, dpPrev = [-1] * (n+1), [-1] * (n+1)
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[j] = j
                elif j == 0:
                    dp[j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[j] = dpPrev[j-1]
                else:
                    dp[j] = min(dpPrev[j], dp[j-1], dpPrev[j-1]) + 1
            dp, dpPrev = dpPrev, dp
        
        return dpPrev[n]