import math
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        minDistance = math.inf
        n = len(arr)

        for i in range(n - 1):
            minDistance = min(minDistance, abs(arr[i + 1] - arr[i]))
        
        res = []

        for i in range(n - 1):
            if abs(arr[i + 1] - arr[i]) == minDistance:
                res.append([arr[i], arr[i + 1]])
        
        return res

