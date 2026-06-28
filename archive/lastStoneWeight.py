from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Time: N^2LogN -> Vẫn chưa tối ưu vì phải sort đi sort lại nhiều lần
        # Space: 1
        
        if not stones:
            return 0
        
        while len(stones) > 1: # N
            stones.sort() # NLogN
            x, y = stones[-2], stones[-1]
            stones.pop()
            stones.pop()
            if x != y:
                offset = y - x
                stones.append(offset)
        
        return 0 if not stones else stones[0]
    

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Time: NLogN
        # Space: 1
        
        if not stones:
            return 0
        
        stones = [-1 * stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            if x != y:
                heappush(stones, x - y)    
        
        return 0 if not stones else -1 * heappop(stones)
        