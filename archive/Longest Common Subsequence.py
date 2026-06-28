class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # Topdown DP
        # @lru_cache(None)
        # def dp(i, j):
        #     if i == -1 or j == -1:
        #         return 0

        #     if text1[i] == text2[j]:
        #         return dp(i - 1, j - 1) + 1
        #     else:
        #         return max(dp(i, j-1), dp(i-1, j))
        # return dp(m-1, n -1)


        # BottomUp DP
        # dp = [[0] * (n+1) for _ in range(m + 1)]

        # for i in range(m):
        #     dp[i][-1] = 0

        # for j in range(n):
        #     dp[-1][j] = 0

        # for i in range(m):
        #     for j in range(n):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # return dp[m-1][n-1]


        # BottomUp + Shift index by 1
        dp = [[0] * (n+1) for _ in range(m + 1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0: continue
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


        # backtrack
        i = m
        j = n
        path = []
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                path.append(text1[i-1])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                i -= 1
            else:
                j -= 1
        
        print(path[::-1])

        return dp[m][n]