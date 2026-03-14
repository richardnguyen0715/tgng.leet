def minDifference(nums, n):
    
    # TopDown DP
    # totalSum = sum(nums)
    
    # def dp(i, currSum):
        
    #     if i == -1:
    #         return abs(2 * currSum - totalSum) # difference of 2 sum of 2 subsets
    
    #     pick = dp(i - 1, currSum + nums[i]) # pick i to subset 1
    #     skip = dp(i - 1, currSum) # pick i to subset 2
        
    #     return min(pick, skip)
    
    # return dp(n - 1, 0)
    
    
    # BottomUp Dp
    totalSum = sum(nums)
    dp = [[float('inf')] * (totalSum + 1) for _ in range(n)]
    for curSum in range(totalSum+1):
        dp[-1][curSum] = abs(2 * curSum - totalSum)
    
    for i in range(n):
        for j in range(totalSum, -1, -1):
            dp[i][j] = dp[i-1][j] # skip
            if j + nums[i] <= totalSum:
                dp[i][j] = min(dp[i][j], dp[i-1][j + nums[i]])
    
    return dp[n-1][0]
    
print(minDifference([1, 6, 5, 11], 4))