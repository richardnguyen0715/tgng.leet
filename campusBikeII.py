from functools import lru_cache


def assignBikes(workers, bikes):

    n, m = len(workers), len(bikes)
    
    def mahattanDistance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    # ans = float('inf')
    # backtracking - brute force => TLE
    # Time: O(M^N)
    # Space: O(N) 
    # def dfs(iW, usedBikes, totalDist):
    #     nonlocal ans
    #     if iW == n:
    #         ans = min(ans, totalDist)
    #         return
        
    #     for iB in range(m):
    #         if iB not in usedBikes:
    #             usedBikes.add(iB)
    #             dfs(iW+1, usedBikes, totalDist + mahattanDistance(workers[iW], bikes[iB]))
    #             usedBikes.remove(iB)
    # dfs(0, set(), 0)
    # return ans

    # Solution 2: sử dụng DP
    # @lru_cache(maxsize=128, typed=False)
    # def dp(iW, usedBikes):
    #     # Time: O(N * 2 ^ M * M * M) => TLE
    #     if iW == n:
    #         return 0
        
    #     ans = float("inf")
    #     for iB in range(m):
    #         if iB not in usedBikes:
    #             newUsedBikes = tuple(list(usedBikes) + [iB])
    #             dist = mahattanDistance(workers[iW], bikes[iB])
    #             ans = min(ans, dp(iW + 1, newUsedBikes) + dist)
    #     return ans
        
    # return dp(0, tuple())

    
    # Solution 3 - Ý tưởng là sử dụng bitmask trong đó bit thứ i == 1 thể hiện cho việc xe đạp đó đã được sử dụng, nhầm loại bỏ bước tạo visited tốn O(M)
    @lru_cache(maxsize=128, typed=False)
    def dp(iW, usedBikesMask):
        # Time: O(N * 2 ^ M * M * M) => TLE
        if iW == n:
            return 0
        
        # Tạo luôn một state mới chứ không phải backtrack 
        ans = float("inf")
        
        for iB in range(m):
            if (usedBikesMask >> iB) & 1: continue # đã được sử dụng rồi
            dist = mahattanDistance(workers[iW], bikes[iB])
            # usedBikesMask ^ (1 << iB) dùng để đảo bit
            ans = min(ans, dp(iW + 1, usedBikesMask ^ (1 << iB)) + dist)
        return ans
        
    return dp(0, 0)