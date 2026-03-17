from typing import List


class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        n = len(nums)

        left = 0
        right = n - 1
        ans = 0

        while left < right:

            height = min(nums[left], nums[right])

            ans = max(ans, (right-left) * height)

            if nums[left] <= nums[right]:
                left += 1
            else:
                right -= 1
        
        return ans
