from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row  = 0 
        col = 0
        ans = []
        directions = [False, True, False, False]  # Left, Right, Up, Down
        steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        count = [0, 0, 0, 0]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m * n):
            ans.append(matrix[row][col])
            
            cur_count = 0
            if directions[0] == True: # LEFT
                next_step = steps[0]
                cur_count = count[2]
            elif directions[1] == True: # RIGHT
                next_step = steps[1]
                cur_count = count[3]
            elif directions[2] == True: # UP
                next_step = steps[2]
                cur_count = count[1]
            elif directions[3] == True: # DOWN
                next_step = steps[3]
                cur_count = count[0]
            
            temp_row = row + next_step[0]
            temp_col = col + next_step[1]

            if directions[1] == True and temp_col > n - 1 - cur_count: # Right -> Down
                directions = [False, False, False, True]
                count[1] += 1
                next_step = steps[3]

            elif directions[3] == True and temp_row > m - 1 - cur_count: # Down -> Left
                directions = [True, False, False, False]
                count[3] += 1
                next_step = steps[0]

            elif directions[0] == True and temp_col < cur_count: # Left -> Up
                directions = [False, False, True, False]
                count[0] += 1
                next_step = steps[2]

            elif directions[2] == True and temp_row < cur_count: # Up -> Right
                directions = [False, True, False, False]
                count[2] += 1
                next_step = steps[1]

            
            row += next_step[0]
            col += next_step[1]

        return ans
                