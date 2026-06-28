from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        choosen = -1

        for row in range(m):
            print(matrix[row][0])
            print(matrix[row][n - 1])
            print(target)
            if matrix[row][0] <= target <= matrix[row][n-1]:
                choosen = row
                break

        if choosen == -1:
            return False

        left = 0
        right = n - 1

        while left <= right:
            mid = (right + left) // 2

            if matrix[choosen][mid] == target:
                return True
            elif matrix[choosen][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return False
