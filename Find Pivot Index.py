from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum = sum(nums)
        n = len(nums)
        leftSum = 0
        for i in range(n):
            rightSum = totalSum - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            leftSum += nums[i]

        return -1