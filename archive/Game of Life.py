from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def findNextState(x, y):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                         (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            neiLive = 0
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < m and 0 <= new_y < n:
                    # Chỉ cần đếm láng giềng sống
                    if board[new_x][new_y] == 1:
                        neiLive += 1
            
            # Áp dụng rules
            if board[x][y] == 1:  # Ô đang sống
                if neiLive < 2 or neiLive > 3:
                    return 0  # Chết
                else:  # neiLive == 2 or neiLive == 3
                    return 1  # Sống tiếp
            else:  # Ô đang chết
                if neiLive == 3:
                    return 1  # Sống lại
                else:
                    return 0  # Vẫn chết
        
        # Tạo board mới để lưu kết quả
        newBoard = [[0] * n for _ in range(m)]
        
        # Tính toán trạng thái mới cho tất cả ô
        for i in range(m):
            for j in range(n):
                newBoard[i][j] = findNextState(i, j)
        
        # Copy kết quả về board gốc
        for i in range(m):
            for j in range(n):
                board[i][j] = newBoard[i][j]