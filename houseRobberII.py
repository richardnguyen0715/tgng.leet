from typing import List

class Solution:
    def rob_line(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]                  # dp[i-2]
        prev1 = max(nums[0], nums[1])    # dp[i-1]

        for i in range(2, n):
            cur = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = cur

        return prev1

    def rob(self, nums: List[int]) -> int:
        
        # Analyze: Không được cướp đồng thời nhà cuối và nhà đầu -> chỉ có 2 trường hợp là có cướp nhà cuối và có cướp nhà đầu
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Trường hợp 1: không cướp nhà cuối → xét [0..n-2]
        case1 = self.rob_line(nums[:-1])
        # Trường hợp 2: không cướp nhà đầu → xét [1..n-1]
        case2 = self.rob_line(nums[1:])

        return max(case1, case2)