from typing import List


# Time: O(N^2), Space: O(N^2) - O(1) if not consider about res
# Time: 3ms -> Beat: 5%

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r = c = 0

        for num in range(1, n * n + 1):
            matrix[r][c] = num

            nr = r + directions[d][0]
            nc = c + directions[d][1]

            if (
                nr < 0 or nr >= n or
                nc < 0 or nc >= n or
                matrix[nr][nc] != 0
            ):
                d = (d + 1) % 4
                nr = r + directions[d][0]
                nc = c + directions[d][1]

            r, c = nr, nc

        return matrix