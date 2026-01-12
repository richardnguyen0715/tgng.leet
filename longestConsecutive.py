from typing import List


# Got negative nums -> Wrong answer
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)

        max_num = max(nums)
        positions = [0] * (max_num + 1)

        for num in nums:
            positions[num] = 1

        print(positions)
        
        ans = 0
        max_sum = 0
        n = len(positions)
        for i in range(0, n):
            if positions[i] >= 1:
                max_sum += 1
            else:
                max_sum = 0
            
            ans = max(ans, max_sum)
        
        return ans



# Memory Limit Exceeded
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        # Chuyển tất cả các số âm thành số dương bằng cách cộng cho số đối của thằng nhỏ nhất.
        min_num = min(nums)
        nums = [num + (-1) * (min_num) for num in nums]
        max_num = max(nums)
        positions = [0] * (max_num + 1)

        for num in nums:
            positions[num] = 1

        # print(positions)
        
        ans = 0
        max_sum = 0
        n = len(positions)
        for i in range(0, n):
            if positions[i] >= 1:
                max_sum += 1
            else:
                max_sum = 0
            
            ans = max(ans, max_sum)
        
        return ans
    
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Chỉ bắt đầu đếm từ số đầu tiên của sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Đếm độ dài sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
    
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))  # Loại bỏ duplicate và sort
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)