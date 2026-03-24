from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        # Time Limit Exceeded
        product = 1
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                product *= grid[i][j] # Chỗ này là vấn đề -> Số quá lớn dẫn đến nhân chậm
        
        for i in range(n):
            for j in range(m):
                grid[i][j] = (product // grid[i][j]) % 12345 # Chỗ này là vấn đề -> Số quá lớn nên // và % chậm
        
        return grid
        


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        # Edge case 1: Single element
        if n == 1 and m == 1:
            return [[1]]  # Không có phần tử nào khác
        
        result = [[1] * m for _ in range(n)]
        
        # Pass 1: Prefix
        prefix = 1
        for i in range(n):
            for j in range(m):
                result[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD # Luôn giữ cho số nhỏ
        
        # Pass 2: Suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                result[i][j] = (result[i][j] * suffix) % MOD # Luôn giữ cho số nhỏ
                suffix = (suffix * grid[i][j]) % MOD
        
        return result
    

# [[1,2],[3,4]]

# prefix
# 0 - 0 - 1
# 0 - 1 - 2
# 1 - 0 - 6
# 1 - 1 - 24
# [[1, 1], [2, 6]]
# suffix
# 1 - 1 - 4
# 1 - 0 - 12
# 0 - 1 - 24
# 0 - 0 - 24
# [[24, 12], [8, 6]]