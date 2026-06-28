from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if n <= 3:
            return False

        left = 0
        right = n - 1

        while left < n - 1 and nums[left] < nums[left + 1]:
            left += 1

        # left = 2, nums[left] = 5
        print("left vs nums: ", left, nums[left])
        
        while right >= 1 and nums[right] > nums[right - 1]:
            right -= 1

        # right = 4, nums[right] = 2
        print("right vs nums: ", right, nums[right])

        if left >= right or left == 0 or right == n - 1:
            return False
        
        while left < right:
            if nums[left] <= nums[left + 1]:
                return False
            
            left += 1

        return True
        
