from typing import List
from collections import Counter

# Memory Limit Exceeded
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                return num
        
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        for key, val in cnt.items():
            if val >= 2:
                return key
            

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] not in hash_map:
                hash_map[nums[left]] = 1
            else:
                return nums[left]

            
            if nums[right] not in hash_map:
                hash_map[nums[right]] = 1
            else:
                return nums[right]
            
            left += 1
            right -= 1
        
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            count = sum(num <= mid for num in nums)
            
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        return left


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_sorted = nums.copy()
        nums_sorted.sort()
        
        for i in range(0, len(nums) - 1):
            if nums_sorted[i] == nums_sorted[i + 1]:
                return nums_sorted[i]
            


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point in the cycle
        slow = fast = nums[0]
        
        # Move slow one step, fast two steps
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow