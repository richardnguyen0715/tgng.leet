from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Time: O(2N) = O(N)
        # Space: O(N)
        
        count = Counter(nums) # O(N)

        # print(count)

        for key, val in count.items(): # O(N)
            if val == 1:
                return key

        return -1
    
    

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        res = 0
        
        for num in nums:
            res = res ^ num
        
        return res
    
    

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path =[]

        def buildSubset(res, path, idx, nums):
            if idx == nums:
                res.append(path.copy())
                return

            
            path.append(nums[idx])
            buildSubset(res, path, idx + 1, nums)
            path.pop()
            
            buildSubset(res, path, idx + 1, nums)
        
        
        buildSubset(res, path, 0, nums)
            
