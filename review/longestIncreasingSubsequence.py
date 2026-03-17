from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp = [1] * len(nums)

        for i in range(len(nums)):

            for j in range(i):

                if nums[j] < nums[i]:

                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        # ý tưởng là chứa các phần tử nhỏ đến lớn vào trong tails, gặp lớn hơn thì lấy ra
        arr = []

        for num in nums:

            # tìm phần tử gần nhất bên trái mà lớn hơn hoặc bằng nó
            pos = bisect.bisect_left(arr, num)

            if pos == len(arr):
                arr.append(num)
            else:
                arr[pos] = num
        
        return len(arr)