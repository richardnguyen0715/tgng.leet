from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        temp_matrix = [mtx.copy() for mtx in matrix]
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                matrix[j][n - 1- i] = temp_matrix[i][j]

        