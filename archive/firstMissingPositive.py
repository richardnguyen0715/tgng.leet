from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        # Time: O(N)
        # Space: O(1)
        
        nums = set(nums) # Time: O(1) with "in" operation, O(N) in turning list into set
        ans = 1
        while ans in nums: # Time: O(1)
            ans += 1
        
        return ans