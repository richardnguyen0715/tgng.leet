from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])

        rowSum = [[0] * n for _ in range(m)]
        colSum = [[0] * n for _ in range(m)]
        rowSum[0][0] = grid[0][0]
        colSum[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0: continue

                rowSum[i][j] = rowSum[i][j - 1] + grid[i][j] if j != 0 else grid[i][j]
                colSum[i][j] = colSum[i - 1][j] + grid[i][j] if i != 0 else grid[i][j]

        # horizontal partition
        for i in range(1, m):
            before = 0
            for j in range(0, i):
                before += rowSum[j][n - 1]
            after = 0
            for j in range(i, m):
                after += rowSum[j][n - 1]

            if before == after:
                return True

        # vertical partition
        for i in range(1, n):
            before = 0
            for j in range(0, i):
                before += colSum[m - 1][j]
            after = 0
            for j in range(i, n):
                after += colSum[m - 1][j]  # Fixed: changed from rowSum to colSum
            
            if before == after:
                return True

        return False
    
    

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        current_sum = 0
        
        for i in range(m - 1):
            current_sum += sum(grid[i])
            
            if current_sum == target:
                return True
        
        current_sum = 0
        
        for j in range(n - 1):
            current_sum += sum(grid[i][j] for i in range(m))
            if current_sum == target:
                return True
        
        
        return False