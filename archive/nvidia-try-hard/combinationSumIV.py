from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        res = 0

        def dfs(current_sum):
            nonlocal res
            if current_sum == target:
                res += 1
            elif current_sum > target:
                return
            
            for num in nums:
                current_sum += num
                dfs(current_sum)
                current_sum -= num
        
        dfs(0)
        return res
    
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]
    

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # Memoization cache: dp[remaining] = number of ways to reach target
        memo = {}
        
        def dfs(remaining: int) -> int:
            # Base cases
            if remaining == 0:
                return 1  # Found one valid combination
            if remaining < 0:
                return 0  # Overshot the target
            
            # Return cached result if already computed
            if remaining in memo:
                return memo[remaining]
            
            # Try adding each number and sum up all possibilities
            ways = 0
            for num in nums:
                ways += dfs(remaining - num)
            
            # Cache and return
            memo[remaining] = ways
            return ways
        
        return dfs(target)
    
    
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(total):
            if total == target:
                return 1
            if total > target:
                return 0
            if total in memo:
                return memo[total]

            c = 0
            for i in nums:
                c += backtrack(total + i)

            memo[total] = c
            return c

        return backtrack(0)