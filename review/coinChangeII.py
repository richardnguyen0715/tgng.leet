from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        ans = 0
        visited = set()

        # TLE
        
        def dfs(candidates, curSum):
            nonlocal ans

            if curSum > amount:
                return

            if curSum == amount:
                candidates.sort()
                tupleCan = tuple(candidates)
                if tupleCan not in visited:
                    ans += 1
                    # print("checked")
                    print(candidates)
                    visited.add(tupleCan)
                return
            
            
            for coin in coins:
                if coin + curSum <= amount:
                    curSum += coin
                    candidates.append(coin)
                    dfs(candidates, curSum)
                    curSum -= coin
                    candidates.pop()
        dfs([], 0)
        return ans


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # số cách đổi của amount i
        dp = [0] * (amount + 1)
        dp[0] = 1 # Không lấy coin nào

        # Tránh tạo ra permutation trùng lặp
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        print(dp)
        return dp[amount]