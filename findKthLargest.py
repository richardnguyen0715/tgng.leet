from heapq import heappop, heappush, heapify
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create an empty heap
        h = []
        heapify(h)

        for i in nums:  # -i to stimulate Max Heap
            heappush(h, -i)

        for i in range(k - 1):
            heappop(h)

        return -h[0]
    
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create an empty heap
        h = [-i for i in nums]
        heapify(h)
        
        for i in range(k - 1):
            # Pop max element
            heappop(h)

        return -h[0]