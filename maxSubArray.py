from typing import List
import numpy as np


# TLE
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -1 * np.inf
        for rang in range(n, 0, -1):
            for i in range(0, n - rang + 1):
                sub_sum = sum(nums[i:i+rang])
                if  sub_sum > max_sum:
                    max_sum = sub_sum
        return max_sum


# Kadane's Algorithms -> O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Kadane's Algorithms

        res = nums[0]
            
        maxEnding = nums[0]

        for i in range(1, len(nums)):

            maxEnding = max(maxEnding + nums[i], nums[i])

            res = max(res, maxEnding)
    
        return res           