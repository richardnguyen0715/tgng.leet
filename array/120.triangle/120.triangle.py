from typing import List


# Time: O(N^2), Space: O(N)
# Time: beat 22%

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
        
            return triangle[i][j] + min(
                dfs(i + 1, j),
                dfs(i + 1, j + 1)
            )
        
        return dfs(0, 0)