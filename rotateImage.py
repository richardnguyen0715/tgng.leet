from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
     
        n = len(matrix)
        hash_map = {}
        for i in range(0, n):
            for j in range(0, n):
                hash_map[(j, n - 1 -i)] = matrix[j][n - 1 - i]

                if (i, j) in hash_map.keys():
                    value = hash_map.get((i, j))
                else:
                    value = matrix[i][j]

                matrix[j][n - 1 - i] = value
                
                
# Rotate Image


# 7 4 1
# 8 5 2
# 9 6 3


# (0,0) (0,1) (0,2) -> (0,2) (1,2) (2,2)
# (1,0) (1,1) (1,2) -> (0,1) (1,1) (2,1)
# (2,0) (2,1) (2,2) -> (0,0) (1,0) (2,0)


# row = col
# col = n - row - 1


# (0,2) -> 3
# (1,2) -> 6
# (2,2) -> 9
# (0,1) -> 2
# (1,1) -> 5
# (2,1) -> 8
# (0,0) -> 1
# (1,0) -> 4
# (2,0) -> 7
