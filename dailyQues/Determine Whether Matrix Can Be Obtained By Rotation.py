from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotateMatrix(mat):
            n = len(mat)

            # transpose
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # reverse mỗi hàng
            for i in range(n):
                mat[i].reverse()
            
            return mat
        
        def compareMatrix(a, b):
            n = len(a)
            for i in range(n):
                for j in range(n):
                    if a[i][j] != b[i][j]:
                        return False
            return True
        
        # print(rotateMatrix(mat))
        n = len(mat)
        for i in range(4):
            mat = rotateMatrix(mat)
            print(mat)
            if compareMatrix(mat, target):
                return True
        
        return False



