from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            return []

        res = [[0] * n for _ in range(m)]

        # Res[i][j] = i * n + j

        # 1,2,3,4
        # 0 -> 0,0
        # 1 -> 0,1
        # 2 -> 1,0
        # 3 -> 1,1
        
        # [1,1,1,1], m = 4, n = 1

        # 0 -> 0,0
        # 1 -> 1,0
        # 2 -> 2,0
        # 3 -> 3,0

        for i in range(m):
            for j in range(n):
                res[i][j] = original[i * n + j]
        
        return res