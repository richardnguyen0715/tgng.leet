from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        ans = 0
        
        for idx in range(n):
            
            left = idx + 1
            right = n - 1
            goal = target - nums[idx]
            
            while left < right:
                
                if nums[left] + nums[right] < goal:
                    ans += right - left
                    left += 1
                else:
                    right += 1
        
        return ans