from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexMap = {}

        for idx, num in enumerate(nums): # O(N)
            indexMap[num] = idx

        print(indexMap)
        
        for idx, num in enumerate(nums): # O(N)
            residual = target - num

            if residual in indexMap and indexMap[residual] != idx: # O(1)
                return [idx, indexMap[residual]]