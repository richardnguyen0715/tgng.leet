from typing import List


# TLE
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = nums[0]
        
        for i in range(n):
            current_product = 1
            for j in range(i, n):
                current_product *= nums[j]
                max_product = max(max_product, current_product)
                
                # Nếu gặp 0, current_product sẽ là 0
                # Subarray tiếp theo sẽ bắt đầu từ j+1
                if nums[j] == 0:
                    break
        
        return max_product
    
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Khởi tạo với phần tử đầu tiên
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Nếu số hiện tại là âm, hoán đổi max và min
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # Cập nhật max và min
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # Cập nhật kết quả
            max_product = max(max_product, current_max)
        
        return max_product
    
    
# Maximum Product SubArray


# [2,3,-2,4]

# ---

# Initiation:
# max = 2
# current_max = 2
# current_min = 2

# num = 3 > 0
# current_max = max(3, 2 * 3) = 6
# current_min = min(3, 2 * 3) = 3
# max = max(6,2) = 6

# num = -2 < 0
# current_max = 3
# current_min = 6

# current_max = max(-2, 3 * -2) = -2
# current_min = min(6, 6 * -2) = -12
# max = max(6,-2) = 6

# num = 4 > 0
# current_max = max(4, 4 * -2) = 4
# current_min = min(4, 4 * -12) = -48
# max = max(6, 4) = 6 

