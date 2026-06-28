from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp(i) là số tiền cướp được từ nhà thứ 0 đến nhà thứ i

        # option 1: cướp nhà ith -> res = nums[i] + dp[i-2]
        # option 2: bỏ qua nhà ith -> res = dp[i-1]
        # basecase: 0 -> nums[0] - cướp nhà số 0 chắc chắn sẽ ok hơn là ko cưóp vì i = 0 thì chỉ có 2 option nhà; 1 -> max(nums[0], nums[1]), chọn 1 trong 2 nhà, nào lớn thì cướp.
    
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            take = nums[i] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(take, skip)
        
        return dp[n -1]
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Time: O(N)
        # Space: O(N)
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            cur = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = cur
        
        return prev
    

from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            # i: index của nhà hiện tại
            if i >= n:
                return 0

            # Lựa chọn 1: bỏ qua nhà i
            skip = dfs(i + 1)

            # Lựa chọn 2: cướp nhà i, rồi nhảy sang i+2
            take = nums[i] + dfs(i + 2)

            return max(skip, take)

        return dfs(0)
    


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            skip = dfs(i + 1)            # không cướp nhà i
            take = nums[i] + dfs(i + 2)  # cướp nhà i

            memo[i] = max(skip, take)
            return memo[i]

        return dfs(0)