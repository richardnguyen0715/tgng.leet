from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        n = len(nums)
        cur_sum = 0
        ans = float("inf")
        
        for right in range(n):
            num = nums[right]
            
            cur_sum += num
            
            while cur_sum >= target:
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
        return ans if ans != float("inf") else 0
        
        
        