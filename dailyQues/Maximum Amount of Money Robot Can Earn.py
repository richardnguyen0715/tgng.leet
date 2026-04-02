from typing import List

# Cách này bị memory limit
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
        path = []
        directions = [(0, 1), (1, 0)] # Right, Down
        m, n = len(coins), len(coins[0])
        
        def dfs(i, j, candidates, visited):
            nonlocal path
            if i == m - 1 and j == n - 1:
                # print("ping")
                path.append(candidates.copy())
                return
            
            for dx, dy in directions:
                nX = dx + i
                nY = dy + j

                if 0 <= nX < m and 0 <= nY < n and (nX, nY) not in visited:
                    candidates.append(((nX, nY), coins[nX][nY]))
                    visited.add((nX, nY))
                    dfs(nX, nY, candidates, visited)
                    candidates.pop()
                    visited.remove((nX, nY))

        dfs(0, 0, [((0, 0), coins[0][0])], set())

        def findMaximum(path):
            n = len(path)
            robbers = []
            coins = 0
            for i in range(n):
                if path[i][1] >= 0:
                    coins += path[i][1]
                else:
                    robbers.append(path[i][1])
            
            robbers.sort()

            print(robbers)
            print(coins)
            
            if len(robbers) <= 2:
                return coins
            
            if len(robbers) == 3:
                return coins + robbers[-1]

            if len(robbers) > 3:
                return coins + sum(robbers[2:])


        # print(path)
        ans = float("-inf")
        for pt in path:
            # print("printing")
            print(pt)
            maxCoins = findMaximum(pt)
            ans = max(ans, maxCoins)
        
        return ans
    
    
# Time limit exceed
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        directions = [(0, 1), (1, 0)]
        max_coins = float("-inf")
        
        def calculateMaxFromPath(path_values):
            # Tách các giá trị âm (robbers) và không âm
            robbers = []
            total_sum = 0
            
            for val in path_values:
                if val < 0:
                    robbers.append(val)
                total_sum += val
            
            # Nếu có ≤ 2 robbers, neutralize tất cả
            if len(robbers) <= 2:
                return total_sum - sum(robbers)  # Bỏ đi tất cả robbers
            
            # Nếu có > 2 robbers, neutralize 2 robbers tệ nhất
            robbers.sort()  # Sắp xếp từ nhỏ đến lớn (tệ nhất đến tốt nhất)
            return total_sum - robbers[0] - robbers[1]  # Bỏ đi 2 robbers tệ nhất
        
        def dfs(i, j, path_values, visited):
            nonlocal max_coins
            
            if i == m - 1 and j == n - 1:
                path_max = calculateMaxFromPath(path_values)
                max_coins = max(max_coins, path_max)
                return
            
            for dx, dy in directions:
                nX, nY = i + dx, j + dy
                
                if 0 <= nX < m and 0 <= nY < n and (nX, nY) not in visited:
                    coin_value = coins[nX][nY]
                    visited.add((nX, nY))
                    path_values.append(coin_value)
                    
                    dfs(nX, nY, path_values, visited)
                    
                    path_values.pop()
                    visited.remove((nX, nY))
        
        # Bắt đầu từ ô (0,0)
        dfs(0, 0, [coins[0][0]], {(0, 0)})
        
        return max_coins
    
    

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = maximum coins at position (i,j) with k neutralizations used
        # k can be 0, 1, or 2
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base case: starting position
        if coins[0][0] < 0:
            dp[0][0][0] = coins[0][0]  # Don't neutralize
            dp[0][0][1] = 0           # Neutralize this robber
        else:
            dp[0][0][0] = coins[0][0]
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                current_coin = coins[i][j]
                
                # Check all possible previous positions
                for prev_i, prev_j in [(i-1, j), (i, j-1)]:
                    if prev_i >= 0 and prev_j >= 0:
                        # For each number of neutralizations used so far
                        for k in range(3):
                            if dp[prev_i][prev_j][k] == -float('inf'):
                                continue
                            
                            if current_coin >= 0:
                                # Positive coin, just add it
                                dp[i][j][k] = max(dp[i][j][k], 
                                                dp[prev_i][prev_j][k] + current_coin)
                            else:
                                # Negative coin (robber)
                                # Option 1: Don't neutralize, lose coins
                                dp[i][j][k] = max(dp[i][j][k], 
                                                dp[prev_i][prev_j][k] + current_coin)
                                
                                # Option 2: Neutralize if we have neutralizations left
                                if k < 2:
                                    dp[i][j][k+1] = max(dp[i][j][k+1], 
                                                      dp[prev_i][prev_j][k])
        
        # Return the maximum among all neutralization states at destination
        return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])