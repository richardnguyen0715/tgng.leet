from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0

        # Min-heap -> Convert to max heap by * -1
        for i in range(len(stones)):
            stones[i] *= -1

        heapify(stones)

        while len(stones) >= 2:
            y = heappop(stones)
            x = heappop(stones)

            if (-1 * y) - (-1 * x) != 0:
                heappush(stones, (-1 * ((-1 * y) - (-1 * x))))
        
        return -stones[0] if stones else 0
