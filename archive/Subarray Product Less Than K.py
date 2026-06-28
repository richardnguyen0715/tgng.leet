from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0

        n = len(nums)

        print(nums)
        res = 0
        product = 1
        left = 0
        for right in range(n):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1
            
            res += right - left + 1
        
        return res

