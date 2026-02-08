from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:

        # Solution 1: Top-Down DP

        # # Time: O(N)
        # # Space: O(N)
        
        # n = len(s)

        # # Số cách decode tại vị trí thứ i của chuỗi s
        # @lru_cache(None)
        # def dfs(i):
        #     if i == n:
        #         # Đã đi tới vị trí cuối cùng -> tức là trước đó đã hợp lệ hết
        #         return 1
            
        #     ans = 0
        #     # Case 1: nếu như mình chọn đi một bước -> 1 -> 9
        #     if s[i] != '0':
        #         ans += dfs(i + 1)
            
        #     # Case 2: nếu như mình chọn đi 2 bước -> 10 -> 26
        #     if i + 1 < n and ( s[i] == '1' or (s[i] == '2' and s[i +1] <= '6')):
        #         ans += dfs( i + 2 )
            
        #     return ans
        
        # return dfs(0)
        
        
        # # Solution 2: Bottom-Up DP

        # # Time: O(N)
        # # Space: O(N)

        # n = len(s)
        # dp = [0] * (n + 1)
        # dp[n] = 1
        # for i in range(n - 1, -1, -1):
        #     # Case 1:
        #     if s[i] != '0':
        #         dp[i] += dp[i + 1]

        #     # Case 2:
        #     if i + 1 < n and ( s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
        #         dp[i] += dp[i + 2]
            
        # return dp[0]
        
        # n = len(s)
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # for i in range(1, n + 1):
        #     # Case 1:
        #     if s[i-1] != '0':
        #         dp[i] += dp[i - 1]

        #     # Case 2:
        #     if i - 2 >= 0 and ( s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
        #         dp[i] += dp[i - 2]
        
        # return dp[n]


        # Solution 2.5: Bottom-Up DP - Space Optimized

        # Time: O(N)
        # Space: O(1)
        
        n = len(s)
        dp, dpPrev1, dpPrev2 = 0, 1, 0
        for i in range(n - 1, -1, -1):
            dp = 0
            # Case 1:
            if s[i] != '0':
                dp += dpPrev1

            # Case 2:
            if i + 1 < n and ( s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                dp += dpPrev2
            
            dpPrev2 = dpPrev1
            dpPrev1 = dp
            
        return dp