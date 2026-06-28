from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i , n):
                if abs(nums[j] - nums[i]) == k:
                    res += 1
        
        return res