from typing import List


# WRONG ANSWER -> DFS IS NOT A SOLUTION HERE
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        import numpy as np
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_sum = -np.inf
        visited = set()
        num_step = 0
        n = len(matrix)

        def sum_matrix(matrix):
            n = len(matrix)
            ans = 0
            for i in range(0 ,n):
                for j in range(0, n):
                   ans += matrix[i][j]
            return ans

        def dfs(cur_x, cur_y):
            nonlocal num_step, matrix, max_sum, n
            
            if num_step == 2:
                max_sum = max(max_sum, sum_matrix(matrix))
                print(max_sum)
                return

            matrix[cur_x][cur_y] *= -1
            visited.add((cur_x, cur_y))
            num_step += 1

            for dx, dy in directions:
                new_x, new_y = cur_x + dx, cur_y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                    dfs(new_x, new_y)

            matrix[cur_x][cur_y] *= -1
            visited.remove((cur_x, cur_y))
            num_step -= 1
        
        for i in range(0, n):
            for j in range(0, n):
                dfs(i, j)

        return max_sum


# Tính bất biến: tính chẵn / lẻ của số phần tử âm -> Nếu ban đầu có số âm chẵn → luôn giữ chẵn; nếu ban đầu có số âm lẻ → luôn giữ lẻ. => Tổng lớn nhất khi tất cả các số là không âm. 
# Trường hợp 1: Số âm chẵn → tổng lớn nhất là tổng giá trị tuyệt đối của tất cả các phần tử.
# Trường hợp 2: Số âm lẻ → không thể làm tất cả các phần tử thành không âm -> giữ lại duy nhất 1 số âm và số đó phải là số âm có giá trị tuyệt đối nhỏ nhất để tổng là lớn nhất. Do đó, nếu ta giữ -K thì ta sẽ bị mất đi 2*K so với việc biến nó thành +K. 
# Vậy ta chỉ cần trừ đi 2 lần giá trị tuyệt đối nhỏ nhất trong ma trận khỏi tổng giá trị tuyệt đối của tất cả các phần tử.
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        import numpy as np
        total = 0
        min_ele = np.inf
        neg_count = 0
        
        for row in matrix:
            for col in row:
                total += abs(col)
                min_ele = min(min_ele, abs(col))
                if col < 0:
                    neg_count += 1
                
        if neg_count % 2 == 1:
            total -= 2 * min_ele
                
        return total
