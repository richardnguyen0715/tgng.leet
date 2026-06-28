from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        currCount = 0
        i = 0
        while i < n:
            if nums[i] == 1:
                currCount += 1
            else:
                res = max(res, currCount)
                currCount = 0
            
            i += 1
        
        res = max(res, currCount)
        return res
