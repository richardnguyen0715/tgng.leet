from typing import List
from collections import defaultdict


class Solution:
    
    # Time: O(N)
    # Space: O(N)
    # Beat: 18% time, 30% space
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        storage = defaultdict(int)
        for num in nums:
            storage[num] += 1
            if storage[num] > n //2:
                return num