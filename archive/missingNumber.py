from typing import List


# Success, but not optimized -> beat 5% time and 5% space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n + 1):
            if i not in nums:
                return i
        
# Success, beat 14% time and 21% space -> convert list to tuple to make "in" operator got O(1) in time complexity  
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums =tuple(nums)
        for i in range(0, n + 1):
            if i not in nums:
                return i



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # nums =tuple(nums)
        nums.sort()
        i = 0
        while i < n:
            if nums[i] != i:
                break
            i += 1

        return i
            
        