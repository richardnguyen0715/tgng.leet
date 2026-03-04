from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        # countMatrix[i][j] -> num of 1 element on row i col j
        m, n = len(mat), len(mat[0])
        countMatrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                
                if mat[i][j] == 1:

                    for k in range(m):
                        countMatrix[k][j] += 1

                    for p in range(n):
                        countMatrix[i][p] += 1
                    
                    countMatrix[i][j] -= 1

        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if countMatrix[i][j] == 1:
                        res += 1
        
        return res
                