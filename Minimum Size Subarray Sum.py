from typing import List
import math

# 1. Brute Force

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Time: O(N^2)
        # Space: O(1)
        
        n = len(nums)
        ans = math.inf
        for i in range(0, n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                
                if cur >= target:
                    ans = min(ans, j - i + 1)
        
        return 0 if ans == math.inf else ans
                
                
           
# Sliding window
# Time:                 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Time: O(N + N) = O(N)
        # Space: O(1)
        
        n = len(nums)
        import math
        ans = math.inf
        left = 0
        cur_sum = 0

        for right in range(0, n): # O(N)
            cur_sum += nums[right]
            while cur_sum >= target: # O(N), but left is not reset -> maximum is N times
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                
        
        return 0 if ans == math.inf else ans

            



