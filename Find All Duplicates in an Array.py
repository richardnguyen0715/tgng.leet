from typing import List


# Beat: 72% Time, 16% Space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # Time: O(N)
        # Space: O(M), M : Max(Nums) <= 10^5 -> O(1)?
        

        n = max(nums) + 1
        duplicates = [0] * n

        res = set()
        for num in nums:
            duplicates[num] += 1
            if duplicates[num] == 2:
                res.add(num)

        return list(res)
    

# Beat: 8% Time, 70% Space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # Time: O(N)
        # Space: O(1)
        
        # Tính chất của bài toán là từ 1 -> n với n là length của nums luôn
        # Khi đó có thể sử dụng phương pháp Cyclic sort

        i = 0
        while i < len(nums):

            correct_pos = nums[i] - 1 # Vị trí đúng của nums[i]

            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])

        return result
    

# Time: O(N)
# Space: O(1)
# Beat: 80% Time, 50% Space
class Solution:
    
    # Sử dụng chính nums làm hash_table
    def findDuplicates(self, nums):
        result = []
        
        for num in nums:
            index = abs(num) - 1  # Convert to 0-based index
            
            # Nếu số tại vị trí này đã negative -> đã gặp trước đó
            if nums[index] < 0:
                result.append(abs(num))
            else:
                # Mark as visited bằng cách negate
                nums[index] = -nums[index]
        
        return result