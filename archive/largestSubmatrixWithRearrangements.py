from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
        
        print(matrix)
        maxArea = 0

        for i in range(m):

            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                height = row[j]
                width = j + 1
                maxArea = max(maxArea, height * width)
            
        return maxArea


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        if not matrix: 
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            # build heights
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] else 0
            # sort heights in descending order to simulate column reordering
            sorted_heights = sorted(heights, reverse=True)
            for j in range(n):
                max_area = max(max_area, sorted_heights[j] * (j + 1))
        return max_area