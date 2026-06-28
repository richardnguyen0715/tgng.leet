import math
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = -math.inf
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i] and nums[j] - nums[i] > res:
                    res = nums[j] - nums[i]
        
        return -1 if res == -math.inf else res