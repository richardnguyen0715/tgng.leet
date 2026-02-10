import math
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        board = [[math.inf] * 3 for _ in range(3)]

        def whoWin(boards):
            # Check hàng
            for i in range(3):
                if boards[i][0] == boards[i][1] == boards[i][2] and boards[i][0] != math.inf:
                    return boards[i][0]
            
            # Check cột
            for j in range(3):
                if boards[0][j] == boards[1][j] == boards[2][j] and boards[0][j] != math.inf:
                    return boards[0][j]
            
            # Check đường chéo chính (0,0) -> (1,1) -> (2,2)
            if boards[0][0] == boards[1][1] == boards[2][2] and boards[0][0] != math.inf:
                return boards[0][0]
            
            # Check đường chéo phụ (0,2) -> (1,1) -> (2,0)  
            if boards[0][2] == boards[1][1] == boards[2][0] and boards[0][2] != math.inf:
                return boards[0][2]
            
            return math.inf  # No winner

        for idx, (x, y) in enumerate(moves):
            if idx % 2 == 0:
                board[x][y] = 1
            else:
                board[x][y] = 0

        # for i in range(3):
        #     print(board[i])

        res = whoWin(board)

        # print(res)

        if res == 1:
            player = "A"
        elif res == 0:
            player = "B"
        elif len(moves) == 9:
            player = "Draw"
        else:
            player = "Pending"

        return player
    
    

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        board = [[None] * 3 for _ in range(3)]

        def checkWinner(boards, player):
            # Check hàng
            for i in range(3):
                if all(boards[i][j] == player for j in range(3)):
                    return True
            
            # Check cột
            for j in range(3):
                if all(boards[i][j] == player for i in range(3)):
                    return True
            
            # Check đường chéo
            if all(boards[i][i] == player for i in range(3)):
                return True
            
            if all(boards[i][2-i] == player for i in range(3)):
                return True
            
            return False

        # Simulate game
        for idx, (x, y) in enumerate(moves):
            current_player = 'A' if idx % 2 == 0 else 'B'
            board[x][y] = current_player
            
            # Check win after each move (optimization)
            if checkWinner(board, current_player):
                return current_player

        # No winner found
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"