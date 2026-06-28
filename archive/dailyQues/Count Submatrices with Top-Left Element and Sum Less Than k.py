from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])

        sumMatrix = [[0] * n for _ in range(m)]

        # prefixsum matrix
        for r in range(m):
            for c in range(n):
                if c == 0:
                    sumMatrix[r][c] = grid[r][c]
                else:
                    sumMatrix[r][c] = sumMatrix[r][c - 1] + grid[r][c]
            
        # for row in sumMatrix:
        #     print(row)
        # sum matrix that got the bottom-right [i,j]
        totalMatrix = [[0] * n for _ in range(m)]
        count = 0
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    totalMatrix[r][c] = grid[r][c]
                elif r == 0:
                    totalMatrix[r][c] = sumMatrix[r][c]
                elif c == 0:
                    totalMatrix[r][c] = totalMatrix[r-1][c] + grid[r][c]
                else:
                    totalMatrix[r][c] = totalMatrix[r-1][c] + sumMatrix[r][c-1] + grid[r][c]

                if totalMatrix[r][c] <= k:
                    count += 1

        print(totalMatrix)
        return count

                

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Chỉ cần 1 ma trận prefix sum
        for r in range(m):
            for c in range(n):
                # Tính prefix sum trực tiếp trên grid
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                if c > 0:
                    grid[r][c] += grid[r][c-1]
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r-1][c-1]
                
                # Kiểm tra điều kiện ngay lập tức
                if grid[r][c] <= k:
                    count += 1
        
        return count
    
    
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Chỉ lưu hàng trước đó
        prev_row = [0] * n
        
        for r in range(m):
            curr_row = [0] * n
            for c in range(n):
                curr_row[c] = grid[r][c]
                
                if c > 0:
                    curr_row[c] += curr_row[c-1]
                if r > 0:
                    curr_row[c] += prev_row[c]
                if r > 0 and c > 0:
                    curr_row[c] -= prev_row[c-1]
                
                if curr_row[c] <= k:
                    count += 1
            
            prev_row = curr_row
        
        return count