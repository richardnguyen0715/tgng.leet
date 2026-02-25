from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # Time: O(MN)
        # Space: O(MN)
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i - 1][j],
                            dp[i][j - 1],
                            dp[i - 1][j - 1]
                        ) + 1
                    max_side = max(max_side, dp[i][j])
        
        for row in dp:
            print(row)
        return max_side * max_side
    
    
    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # Time: O(MN)
        # Space: O(N)
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])

        dp = [0] * n
        prev = 0
        max_size = 0

        for i in range(m):
            for j in range(n):
                temp = dp[j]

                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = min(dp[j], dp[j -1], prev) + 1
                    max_size = max(max_size, dp[j])
                else:
                    dp[j] = 0
                
                prev = temp
        
        return max_size * max_size