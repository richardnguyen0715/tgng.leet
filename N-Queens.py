from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            # Kiểm tra cột
            if col in cols:
                return False
            
            # Kiểm tra đường chéo chính (row - col = constant)
            if (row - col) in main_diag:
                return False
            
            # Kiểm tra đường chéo phụ (row + col = constant)
            if (row + col) in anti_diag:
                return False
            
            return True
        
        def backtrack(row):
            if row == n:
                # Tạo solution từ positions
                solution = []
                for r in range(n):
                    line = ['.'] * n
                    line[positions[r]] = 'Q'
                    solution.append(''.join(line))
                result.append(solution)
                return
            
            for col in range(n):
                if is_safe(row, col):
                    # Đặt quân hậu
                    positions[row] = col
                    cols.add(col)
                    main_diag.add(row - col)
                    anti_diag.add(row + col)
                    
                    # Recursion
                    backtrack(row + 1)
                    
                    # Backtrack
                    cols.remove(col)
                    main_diag.remove(row - col)
                    anti_diag.remove(row + col)
        
        result = []
        positions = [-1] * n  # positions[i] = j nghĩa là hàng i có quân hậu ở cột j
        cols = set()          # Các cột đã có quân hậu
        main_diag = set()     # Đường chéo chính (row - col)
        anti_diag = set()     # Đường chéo phụ (row + col)
        
        backtrack(0)
        return result