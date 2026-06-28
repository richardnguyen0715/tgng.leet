from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # O(NLogN)
        n = len(nums)
        ans = set()
        
        for idx, num in enumerate(nums):
            
            target = num * (-1)
            
            left = idx + 1
            right = n - 1
            
            while left <= right:
                
                if nums[left] + nums[right] == target:
                    ans.add((nums[idx], nums[left], nums[right])) # Set -> Unique, cannot be implemented for set(list)
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
                    
        return [list(res) for res in ans]
        

