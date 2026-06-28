from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        left = 0
        right = n - 1
        while left <= right:
            left_count = 0
            while nums[left] == nums[left + 1]:
                left += 1
                left_count += 1

            if left_count < 1:
                return nums[left]
            
            left += 1
            
            right_count = 0
            while nums[right] == nums[right - 1]:
                right -= 1
                right_count += 1
            
            if right_count < 1:
                return nums[right]
            
            right -= 1