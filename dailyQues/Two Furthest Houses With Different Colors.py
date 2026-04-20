from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if colors[i] == colors[j]: continue
                ans = max(ans, j - i)

        return ans