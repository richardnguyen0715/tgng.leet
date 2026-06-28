from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeros = []
        m = len(matrix)
        n = len(matrix[0])
        # Find Zeros
        for row in range(m): # Run row
            if 0 in matrix[row]:
                for idx, val in enumerate(matrix[row]): # Run col
                    if val == 0:
                        zeros.append((row, idx))

        for z_row, z_col in zeros:
            matrix[z_row] = [0] * n

            for row in range(m):
                matrix[row][z_col] = 0

        print(matrix)
