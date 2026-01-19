from typing import List


# Time Limit Exceeded
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        for i in range(n):
            right = min(i + k, n - 1)
            while i < right:
                if nums[i] == nums[right]:
                    return True
                right -= 1
        
        return False


# Success, but not optimized -> beat 5% time, 10% space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        position_map = {}
        n = len(nums)
        
        for i in range(n):
            if nums[i] not in position_map:
                position_map[nums[i]] = [i]
            else:
                position_map[nums[i]].append(i)
        
        for key, val in position_map.items():
            if len(val) < 2:
                continue
            
            val.sort()
            for i in range(len(val) - 1):
                if val[i + 1] - val[i] <= k:
                    return True
            
        return False


# Optimized -> save maximum position of number!!! -> beat 80% time, 50% space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        position_map = {}
        n = len(nums)

        for i in range(n):
            if nums[i] not in position_map:
                position_map[nums[i]] = i
            else:
                if i - position_map[nums[i]] <= k:
                    return True
                else:
                    position_map[nums[i]] = i
            
        return False