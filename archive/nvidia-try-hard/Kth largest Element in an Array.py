from heapq import heappop, heapify
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [num * -1 for num in nums]
        heapify(nums)

        for _ in range(k - 1):
            heappop(nums)
        
        return heappop(nums) * (-1)
