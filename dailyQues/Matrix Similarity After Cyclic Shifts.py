from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m, n = len(mat), len(mat[0])
        checkRows = [False] * m

        def shiftLeft(row, k):
            n = len(row)
            k %= n
            row = row * 2
            return row[k:k+n]

        def shiftRight(row, k):
            n = len(row)
            k %= n
            row = row * 2
            return row[n-k:n-k+n]

        for i in range(m):

            if i % 2 == 0:
                newRow = shiftLeft(mat[i], k)
            else:
                newRow = shiftRight(mat[i], k)

            if newRow == mat[i]:
                checkRows[i] = True

        return all(checkRows)