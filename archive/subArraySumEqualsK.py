from typing import List


# Cách này bị time exceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        # O(N^3) vì sum() cũng là một vòng lặp
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            # print(i)
            for j in range(n):
                end = min(n, j + i)
                substr = nums[j: end]
                if len(substr) < i:
                    continue
                # print(j, end)
                # print(substr)
                if sum(substr) == k:
                    ans += 1
        
        return ans
    

# Cách này cũng bị time exceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        # O(N^2)
        for i in range(n):
            current_sum = 0
            for j in range(i , n):
                current_sum += nums[j]
                if current_sum == k:
                    ans += 1
        return ans
    
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefix sum array -> tổng đã có từ vị trí đầu tiên tới vị trí hiện tại.
        # Ví dụ: [1, 2, 3, 4] -> 0: 1, 1: 1 + 2 = 3, 2: 1 + 2 + 3 = 6, 3: 1 + 2 + 3 + 4 = 10
        
        # Định lý: số substring từ vị trí j + 1 đến i là prefix_sum[i] - prefix_sum[j]
        # => Tìm số subarray có tổng bằng k thì là prefix_sum[j] = prefix_sum[i] - k -> tức là tại vị trí i, nếu trước đó đã có prefix_sum = prefix_sum[i] - k thì sẽ tồn tại một subarray có tổng bằng k
        
        prefix_sum = 0
        sum_count = {0 : 1}  # key: giá trị của prefix_sum, value: số lần mà prefix_sum = 0 (do key là 0) xuất hiện, ở đây ta khởi tạo prefix_sum = 0 nên nó xuất hiện 1 lần đầu tiên
        count = 0
        
        for num in nums:
            prefix_sum += num
            
            # Nếu prefix_sum - k đã xuất hiện trước đó thì tức là có substr cộng lại bằng k
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]

            # Defaut value = 0 -> get(..., 0)
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        # example:
        # [1, 2, 3, 4], k = 3
        
        
        return count