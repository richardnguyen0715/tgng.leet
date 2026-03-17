from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # Gọi dp[i] là số tiền lớn nhất có thể kiếm được từ ngồi nhà thứ 0 -> i
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            take = dp[i - 2] + nums[i]
            skip = dp[i - 1]
            dp[i] = max(take, skip)
    
        return dp[n - 1]
            

