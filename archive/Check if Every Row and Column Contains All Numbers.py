from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        print(n)

        for i in range(n):
            intMap = [0] * (n + 1)
            for j in range(n):
                intMap[matrix[i][j]] = 1
            print(intMap)
            if sum(intMap[1:]) != len(intMap) - 1:
                return False
        
        for i in range(n):
            intMap = [0] * (n + 1)
            for j in range(n):
                intMap[matrix[j][i]] = 1
            print(intMap)
            if sum(intMap[1:]) != len(intMap) - 1:
                return False

        return True
    
    

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        print(n)

        for i in range(n):
            rowSum = [0] * (n + 1)
            colSum = [0] * (n + 1)
            for j in range(n):
                rowSum[matrix[i][j]] = 1
                colSum[matrix[j][i]] = 1

            if sum(rowSum[1:]) != len(rowSum) - 1:
                return False

            if sum(colSum[1:]) != len(colSum) - 1:
                return False

        return True