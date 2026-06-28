from typing import List
import math



# TLE - Time limit exceeded
# N^2 - time
# 1 - space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        
        return maxProfit



# Beat: 60% time, 31% space
# Time: O(N)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        minPrice = math.inf

        n = len(prices)
        for right in range(n):
            minPrice = min(minPrice, prices[right])
            maxProfit = max(maxProfit, prices[right] - minPrice)

        return maxProfit



# Beat: 97% time, 40% space
# Time: O(N)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        maxPrice = prices[0]
        minPrice = prices[0]

        n = len(prices)

        for price in prices:
            if price < minPrice:
                minPrice = price
                maxPrice = price
            elif price > maxPrice:
                maxPrice = price
            else:
                continue
            
            maxProfit = max(maxProfit, maxPrice - minPrice)
        
        return maxProfit

