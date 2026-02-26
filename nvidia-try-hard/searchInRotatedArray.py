from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums: -> O(N) -> Wrong
        #     return -1
        
        if not nums:
            return -1
        
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
        
            elif nums[mid] >= nums[left]: # Mid can be right
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # Mid - 1 is right
                
                else:
                    left = mid + 1 # Mid + 1 is left
                
            else: # Mid can be left
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
            
        return -1