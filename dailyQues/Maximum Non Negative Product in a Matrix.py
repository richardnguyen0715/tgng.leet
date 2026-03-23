from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        # Time Limit Exceeded
        
        m, n = len(grid), len(grid[0])

        ans = float('-inf')

        # # cách này sai khi lấy max ở local thôi -> phải có thêm min local
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0: continue
        #         if i == 0:
        #             dp[i][j] = dp[i][j - 1] * grid[i][j]
        #         elif j == 0:
        #             dp[i][j] = dp[i - 1][j] * grid[i][j]
        #         else:
        #             dp[i][j] = max(dp[i][j - 1] * grid[i][j], dp[i - 1][j] * grid[i][j])
        # for row in dp:
        #     print(row)
        # ans = max(ans, dp[m - 1][n - 1])

        directions = [(1, 0), (0, 1)]

        def dfs(currCandi, visited):
            nonlocal ans
            if currCandi[-1] == (m - 1, n - 1):
                # print(currCandi)
                currProduct = 1
                for x, y in currCandi:
                    currProduct *= grid[x][y]
                ans = max(ans, currProduct)
                return
            
            for dx, dy in directions:
                newX = currCandi[-1][0] + dx
                newY = currCandi[-1][1] + dy
                if 0 <= newX <= m and 0 <= newY <= n and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    currCandi.append((newX, newY))
                    dfs(currCandi, visited)
                    visited.remove((newX, newY))
                    currCandi.pop()


        dfs([(0,0)], set())

        return ans % (10 ** 9 + 7) if ans >= 0 else -1


from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        # Time Limit Exceeded
        
        m, n = len(grid), len(grid[0])
        self.max_product = float('-inf')
        
        def dfs(i, j, current_product):
            # Base case: reached bottom-right corner
            if i == m - 1 and j == n - 1:
                self.max_product = max(self.max_product, current_product)
                return
            
            # right
            if j + 1 < n:
                dfs(i, j + 1, current_product * grid[i][j + 1])
            
            # down
            if i + 1 < m:
                dfs(i + 1, j, current_product * grid[i + 1][j])
        
        # Start DFS from top-left corner
        dfs(0, 0, grid[0][0])
        
        return self.max_product % (10**9 + 7) if self.max_product >= 0 else -1
    

from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Memoization: store (min_product, max_product) for each cell
        memo = {}
        
        def dfs(i, j):
            # Base case: out of bounds
            if i >= m or j >= n:
                return (float('inf'), float('-inf'))  # Invalid path
            
            # Base case: reached destination
            if i == m - 1 and j == n - 1:
                return (grid[i][j], grid[i][j])
            
            # Check memo
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Get results from right and down paths
            right_min, right_max = dfs(i, j + 1)
            down_min, down_max = dfs(i + 1, j)
            
            current = grid[i][j]
            candidates = []
            
            # Add valid candidates from right path
            if right_min != float('inf'):
                candidates.extend([current * right_min, current * right_max])
            
            # Add valid candidates from down path
            if down_min != float('inf'):
                candidates.extend([current * down_min, current * down_max])
            
            if not candidates:
                result = (float('inf'), float('-inf'))
            else:
                result = (min(candidates), max(candidates))
            
            memo[(i, j)] = result
            return result
        
        min_prod, max_prod = dfs(0, 0)
        return max_prod % MOD if max_prod >= 0 else -1


from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] = (min_product, max_product) at position (i,j)
        # We need both min and max because negative * negative = positive
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]
        
        # Initialize first cell
        dp[0][0] = (grid[0][0], grid[0][0])
        
        # Fill first row
        for j in range(1, n):
            prev_min, prev_max = dp[0][j-1]
            curr = grid[0][j]
            new_min = min(prev_min * curr, prev_max * curr)
            new_max = max(prev_min * curr, prev_max * curr)
            dp[0][j] = (new_min, new_max)
        
        # Fill first column
        for i in range(1, m):
            prev_min, prev_max = dp[i-1][0]
            curr = grid[i][0]
            new_min = min(prev_min * curr, prev_max * curr)
            new_max = max(prev_min * curr, prev_max * curr)
            dp[i][0] = (new_min, new_max)
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                curr = grid[i][j]
                
                # Get products from top and left
                top_min, top_max = dp[i-1][j]
                left_min, left_max = dp[i][j-1]
                
                # Calculate all possible products
                candidates = [
                    top_min * curr,
                    top_max * curr,
                    left_min * curr,
                    left_max * curr
                ]
                
                dp[i][j] = (min(candidates), max(candidates))
        
        max_product = dp[m-1][n-1][1]
        return max_product % MOD if max_product >= 0 else -1