class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()

        def getRhombusSum(grid, row, col, k):

            if k == 0:
                return grid[row][col]
            
            total = 0
            
            # Trái -> Trên
            for i in range(k):
                total += grid[row-i][col-k+i]
            
            # Trên -> Phải
            for i in range(k):
                total += grid[row-k+i][col+i]
            
            # Phải -> Dưới
            for i in range(k):
                total += grid[row+i][col+k-i]
            
            # Dưới -> Trái
            for i in range(k):
                total += grid[row+k-i][col-i]
        
            return total
        
        for row in range(m):
            for col in range(n):
                
                maxRadius = min(row, col, m-1-row, n-1-col)

                for k in range(maxRadius + 1):
                    rhombusSum = getRhombusSum(grid, row, col, k)
                    sums.add(rhombusSum)
        
        sortedSums = sorted(sums, reverse=True)
        return sortedSums[:3]