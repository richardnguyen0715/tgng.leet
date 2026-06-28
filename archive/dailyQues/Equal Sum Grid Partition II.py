from typing import List
from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        def numberOfIsland(grid, rowHigh, colHigh, rowLow, colLow):
            visited = set()
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            def dfs(i, j):
                visited.add((i, j))
                for dx, dy in directions:
                    newX, newY = i + dx, j + dy
                    if (rowHigh <= newX <= rowLow and 
                        colHigh <= newY <= colLow and 
                        (newX, newY) not in visited and 
                        grid[newX][newY] != -1):
                        dfs(newX, newY)
            
            count = 0
            for i in range(rowHigh, rowLow + 1):
                for j in range(colHigh, colLow + 1):
                    if grid[i][j] != -1 and (i, j) not in visited:
                        dfs(i, j)
                        count += 1
            
            return count

        print("Row")
        for i in range(m):
            print("check row: ", i)
            current_sum = sum(grid[i])
            print("current sum: ", current_sum)

            if current_sum == target:
                return True

            for j in range(n):
                print(current_sum, target - grid[i][j])
                if current_sum - grid[i][j] == target:
                    temp = grid[i][j]
                    grid[i][j] = -1
                    count = numberOfIsland(grid, 0, 0, m-1, n-1)
                    if count == 1:
                        return True
                    grid[i][j] = temp
        
        print("Col")
        for j in range(n):
            print("check col: ", j)
            current_sum = sum(grid[i][j] for i in range(m))
            print("current_sum: ", current_sum)
            if current_sum == target:
                return True

            for k in range(m):
                print(current_sum, target - grid[k][j])
                if current_sum - grid[k][j] == target:
                    temp = grid[k][j]
                    grid[k][j] = -1
                    count = numberOfIsland(grid, 0, 0, m-1, n-1)
                    if count == 1:
                        return True
                    grid[k][j] = temp
                    
        return False
    
    

from collections import deque
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Precompute row and column prefix sums for O(1) range queries
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
        
        col_prefix = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]
        
        # Build value index for O(1) lookup
        value_positions = {}
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val not in value_positions:
                    value_positions[val] = []
                value_positions[val].append((i, j))
        
        # Try horizontal cuts
        for row in range(1, m):
            if self.check_horizontal_cut_optimized(grid, row, row_prefix, value_positions):
                return True
        
        # Try vertical cuts
        for col in range(1, n):
            if self.check_vertical_cut_optimized(grid, col, col_prefix, value_positions):
                return True
        
        return False
    
    def check_horizontal_cut_optimized(self, grid, cut_row, row_prefix, value_positions):
        m, n = len(grid), len(grid[0])
        
        # O(m) sum calculation using prefix sums
        top_sum = sum(row_prefix[i][n] for i in range(cut_row))
        bottom_sum = sum(row_prefix[i][n] for i in range(cut_row, m))
        
        if top_sum == bottom_sum:
            return True
        
        diff = abs(top_sum - bottom_sum)
        
        # Early termination: check if diff exists in grid
        if diff not in value_positions:
            return False
        
        # Only check cells with the exact difference value
        if top_sum > bottom_sum:
            # Try cells from top section
            candidates = [(r, c) for r, c in value_positions[diff] if r < cut_row]
            if candidates:
                return self.check_candidates_batch(grid, 0, cut_row - 1, 0, n - 1, candidates)
        else:
            # Try cells from bottom section
            candidates = [(r, c) for r, c in value_positions[diff] if r >= cut_row]
            if candidates:
                return self.check_candidates_batch(grid, cut_row, m - 1, 0, n - 1, candidates)
        
        return False
    
    def check_vertical_cut_optimized(self, grid, cut_col, col_prefix, value_positions):
        m, n = len(grid), len(grid[0])
        
        # O(n) sum calculation using prefix sums
        left_sum = sum(col_prefix[m][j] for j in range(cut_col))
        right_sum = sum(col_prefix[m][j] for j in range(cut_col, n))
        
        if left_sum == right_sum:
            return True
        
        diff = abs(left_sum - right_sum)
        
        # Early termination
        if diff not in value_positions:
            return False
        
        if left_sum > right_sum:
            candidates = [(r, c) for r, c in value_positions[diff] if c < cut_col]
            if candidates:
                return self.check_candidates_batch(grid, 0, m - 1, 0, cut_col - 1, candidates)
        else:
            candidates = [(r, c) for r, c in value_positions[diff] if c >= cut_col]
            if candidates:
                return self.check_candidates_batch(grid, 0, m - 1, cut_col, n - 1, candidates)
        
        return False
    
    def check_candidates_batch(self, grid, r1, r2, c1, c2, candidates):
        """Check multiple candidates with optimized connectivity check"""
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        
        # If section has only 1 cell, can't remove it
        if rows * cols == 1:
            return False
        
        # Optimization: If section is small, use faster method
        if rows * cols <= 20:
            for remove_r, remove_c in candidates:
                if self.is_connected_small(grid, r1, r2, c1, c2, remove_r, remove_c):
                    return True
            return False
        
        # For larger sections, use optimized BFS
        for remove_r, remove_c in candidates:
            if self.is_connected_optimized(grid, r1, r2, c1, c2, remove_r, remove_c):
                return True
        
        return False
    
    def is_connected_small(self, grid, r1, r2, c1, c2, remove_r, remove_c):
        """Optimized for small sections"""
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        
        if rows * cols == 1:
            return False
        
        # Use local coordinate system for faster access
        visited = [[False] * cols for _ in range(rows)]
        
        # Find start position
        start_r, start_c = -1, -1
        for i in range(rows):
            for j in range(cols):
                actual_r, actual_c = r1 + i, c1 + j
                if actual_r != remove_r or actual_c != remove_c:
                    start_r, start_c = i, j
                    break
            if start_r != -1:
                break
        
        # BFS with local coordinates
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        count = 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    actual_r, actual_c = r1 + nr, c1 + nc
                    if actual_r != remove_r or actual_c != remove_c:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        count += 1
        
        return count == rows * cols - 1
    
    def is_connected_optimized(self, grid, r1, r2, c1, c2, remove_r, remove_c):
        """Optimized BFS with early termination"""
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        expected = rows * cols - 1
        
        if expected == 0:
            return False
        
        # Find starting cell
        start_r, start_c = None, None
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if i != remove_r or j != remove_c:
                    start_r, start_c = i, j
                    break
            if start_r is not None:
                break
        
        # Use set for faster lookup (better than 2D array for sparse access)
        visited = {(start_r, start_c)}
        queue = deque([(start_r, start_c)])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # Early termination: if we've visited all expected cells
            if len(visited) == expected:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (r1 <= nr <= r2 and c1 <= nc <= c2 and 
                    (nr, nc) not in visited and 
                    (nr != remove_r or nc != remove_c)):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return len(visited) == expected
    
    
    
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g: List[List[int]]) -> bool:
            m, n = len(g), len(g[0])
            s1 = s2 = 0
            cnt1 = defaultdict(int)
            cnt2 = defaultdict(int)
            for i, row in enumerate(g):
                for j, x in enumerate(row):
                    s2 += x
                    cnt2[x] += 1
            for i, row in enumerate(g[: m - 1]):
                for x in row:
                    s1 += x
                    s2 -= x
                    cnt1[x] += 1
                    cnt2[x] -= 1
                if s1 == s2:
                    return True
                if s1 < s2:
                    diff = s2 - s1
                    if cnt2[diff]:
                        if (
                            (m - i - 1 > 1 and n > 1)
                            or (
                                i == m - 2
                                and (g[i + 1][0] == diff or g[i + 1][-1] == diff)
                            )
                            or (n == 1 and (g[i + 1][0] == diff or g[-1][0] == diff))
                        ):
                            return True
                else:
                    diff = s1 - s2
                    if cnt1[diff]:
                        if (
                            (i + 1 > 1 and n > 1)
                            or (i == 0 and (g[0][0] == diff or g[0][-1] == diff))
                            or (n == 1 and (g[0][0] == diff or g[i][0] == diff))
                        ):
                            return True
            return False

        return check(grid) or check(list(zip(*grid)))