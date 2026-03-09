from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        result = prices.copy()
        n = len(prices)
        
        for i in range(n):
            
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = result[idx] - prices[i]
            
            stack.append(i)
        
        return result