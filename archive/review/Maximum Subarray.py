from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)
    
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            # Quyết định xem có nên mở rộng chuỗi ko
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum