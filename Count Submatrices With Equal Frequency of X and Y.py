from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])

        prefixCount = [[[0, 0] for _ in range(n)] for _ in range(m)]
        if grid[0][0] == 'X':
            prefixCount[0][0][0] = 1
        elif grid[0][0] == 'Y':
            prefixCount[0][0][1] = 1
        
        # for row in prefixCount:
        #     print(row)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                prefixCount[i][j][0] = prefixCount[i][j - 1][0]
                prefixCount[i][j][1] = prefixCount[i][j - 1][1]
                if grid[i][j] == 'X':
                    prefixCount[i][j][0] += 1
                elif grid[i][j] == 'Y':
                    prefixCount[i][j][1] += 1
        
        # for row in prefixCount:
        #     print(row)

        sumCount = [[[0, 0] for _ in range(n)] for _ in range(m)]
        if grid[0][0] == 'X':
            sumCount[0][0][0] = 1
        elif grid[0][0] == 'Y':
            sumCount[0][0][1] = 1

        count = 0
        for i in range(m):
            for j in range(n):

                if i == 0:
                    sumCount[i][j][0] = prefixCount[i][j][0]
                    sumCount[i][j][1] = prefixCount[i][j][1]
                else:
                    sumCount[i][j][0] = sumCount[i-1][j][0] + prefixCount[i][j][0]
                    sumCount[i][j][1] = sumCount[i-1][j][1] + prefixCount[i][j][1]
                
                if sumCount[i][j][0] > 0 and sumCount[i][j][0] == sumCount[i][j][1]:
                    count += 1
        
        # for row in sumCount:
        #     print(row)
        
        return count


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]], ans = 0) -> int:

        n = len(grid[0])
        X, Y = [0] * n, [0] * n

        for row in grid:
            rowX, rowY = 0, 0

            for j in range(n):

                rowX += (row[j] == 'X')
                rowY += (row[j] == 'Y')

                X[j] += rowX
                Y[j] += rowY

                ans+= (X[j] > 0) & (X[j] == Y[j])

        return ans