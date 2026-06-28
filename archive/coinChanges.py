from typing import List


# Cách Greedy này sai, do chỉ nhìn local minimum, không nhìn global minimum
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        coins.sort(reverse=True)
        res = 0
        for coin in coins:
            maxCnt = amount // coin
            res += maxCnt
            print(f"coin: {coin}, number: {maxCnt}")
            amount -= coin * maxCnt
            if amount <= 0:
                break

        print(amount)
        
        if amount == 0:
            return res
        return -1
        
        

# Time: O(Amount * N), N là độ dài của coins
# Space: O(Amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Gọi i là số tiền còn giữ
        # Gọi dp[i] là số đồng tối thiểu để tạo nên số tiền i

        dp = [math.inf] * (amount + 1) # Vì có thêm trạng thái tại 0 tiền thì cần 0 coin
        dp[0] = 0 # trạng thái base

        for i in range(amount + 1):

            # Thử các trường hợp coin
            for coin in coins:
                # Có thể tạo ra số tiền thứ i khi giá trị của đồng đó bé hơn hoặc bằng số tiền hiện tại - tức là i
                if coin <= i:
                    # tính số đồng tối thiểu để tạo ra số tiền thứ i
                    dp[i] = min(dp[i], dp[i - coin] + 1) # min giữa số đồng hiện tại và số đồng đã tạo được i - coin trước đó + 1

        return dp[amount] if dp[amount] != math.inf else -1


            
            

        
    
    
from functools import lru_cache
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(amount_remaining):
            
            if amount_remaining == 0:
                return 0
            
            if amount_remaining < 0:
                return math.inf
            
            min_coin = math.inf
            for coin in coins:
                min_coin = min(min_coin, dfs(amount_remaining - coin) + 1)
            
            return min_coin
        
        min_coin = dfs(amount)
        return min_coin if min_coin != math.inf else -1

            
            

        