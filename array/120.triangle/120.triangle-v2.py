from typing import List


# Time: O(N^2); Space: O(N)
# Time: beat 100%

#       2
#      3 4
#     6 5 7
#    4 1 8 3

# dp = [4, 1, 8, 3] (init)

# bỏ đi row cuối cùng -> xét row kế cuối nên mới trừ 2
# 6 + min(4,1) = 7
# 5 + min(1,8) = 6
# 7 + min(8,3) = 10

# dp = [7,6,10,3]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = triangle[-1][:]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]