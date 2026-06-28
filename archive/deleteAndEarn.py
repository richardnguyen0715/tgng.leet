from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_val = max(nums)
        points = [0] * (max_val + 1)

        # Gom điểm cho từng value
        for x in nums:
            points[x] += x

        if max_val == 0:
            return points[0]
        if max_val == 1:
            return max(points[0], points[1])

        # House Robber trên mảng points[0..max_val]
        prev2 = points[0]                       # dp[0]
        prev1 = max(points[0], points[1])       # dp[1]

        for i in range(2, max_val + 1):
            cur = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = cur

        return prev1