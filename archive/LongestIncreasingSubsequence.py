from typing import List
import math



# Cách này sai, vì subsequnce != subarray. Subsequence cho phép loại bỏ các phần tử, chỉ cần giữa nguyên thứ tự
# Ví dụ: [0, 1, 0, 2, 3, 4, 5] thì subsequence là [0, 1, 2, 3, 5] -> loại bỏ 0 và 4
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = -math.inf
        left = 0
        candidates = []
        for right in range(len(nums)):
            candidate = nums[right]

            while candidates and candidates[-1] <= candidate:
                left += 1
                candidates.pop()

            candidates.append(candidate)
            res = max(res, len(candidates))
        
        return res
    

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Gọi DP là mảng chứa chiều dài phần của mảng tăng dần tối đa tại vị trí thứ i
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            
            # Xét từ vị trí thứ i đến trước đó xem có mảng tăng dần nào không?
            for j in range(i):
                
                if nums[j] < nums[i]: # Mảng tăng dần
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Max dp là do chưa chắc phần tử cuối cùng luôn có độ dài lớn nhất        
        return max(dp)