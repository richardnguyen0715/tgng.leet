from typing import List



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Analyze:
            # - Cách này bị chia cho 0
            # - Đề không cho sử dụng phép chia
            # - Cài đặt thuật toán với O(N)
        
        res = []
        multi_product = 1
        for num in nums:
            multi_product *= num
        
        for num in nums:
            res.append(multi_product / num)
        
        return res


    
# Beat: 12% Time, 9% Space
# Ý tưởng: thay vì nghĩ "loại bỏ X" thì ta sẽ ghép "trái của x" và "phải của x". 
# Do không có thuật toán nào O(1) cho việc nhân từng phần tử trong dãy và loại bỏ x.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                
        # Time: O(N)
        # Space: O(N)
        
        n = len(nums)
        res = [0] * n
        left = [1] * n
        right = [1] * n

        left_multiply = 1
        for i in range(1, n):
            left_multiply *= nums[i - 1]
            left[i] = left_multiply
        
        right_multiply = 1
        for i in range(n-2, -1, -1):
            right_multiply *= nums[i + 1]
            right[i] = right_multiply
        
        print(left)
        print(right)

        for i in range(n):
            res[i] = left[i] * right[i]

        
        return res

    

# Beat: 35% Time, 35% Space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Optimized version: 
        # Time: O(N)
        # Space: O(1) vì không tính space result

        n = len(nums)
        res = [1] * n

        left_multiply = 1
        for i in range(1, n):
            left_multiply *= nums[i - 1]
            res[i] *= left_multiply
        
        right_multiply = 1
        for i in range(n-2, -1, -1):
            right_multiply *= nums[i + 1]
            res[i] *= right_multiply
        
        return res

        
         