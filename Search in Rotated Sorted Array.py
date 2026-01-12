from typing import List

# [4,5,6,7,0,1,2], target = 2 (case 1)

# [7,0,1,2,4,5,6], target = 4 (case 2)

# [0,1,2,4,5,6,7], target = 2 (case 3)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums: -> O(N)
        #     return -1
        
        
        # Time: O(logN)
        # Space: O(1)
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # (case 1)
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # (case 2)
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1