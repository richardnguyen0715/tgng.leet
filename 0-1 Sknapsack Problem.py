def knapsackProblem(W, weights, values, n):
    
    
    # # topdown DP
    # def dp(currPos, currCap):
        
    #     if currCap < 0:
    #         return float('-inf')
    
    #     if currPos < 0:
    #         return 0
    
    #     pick = dp(currPos - 1, currCap - weights[currPos]) + values[currPos]
    #     skip = dp(currPos - 1, currCap)
        
    #     return max(pick, skip)

    # return dp(n-1, W)


    # topdown DP -> Giảm được 1/2 state cho cách giải trên, do không cần xét đến w < 0
    def dp(currPos, currCap):

        if currPos < 0:
            return 0
    
        ans = dp(currPos - 1, currCap)
        
        if currCap >= weights[currPos]:
            ans = max(ans, dp(currPos - 1, currCap - weights[currPos]) + values[currPos])
        
        return ans


    i = n - 1
    w = W
    path = []
    while i != -1:
        if dp(i, w) == dp(i -1, w - weights[i]) + values[i]: # pick
            path.append(i)
            w -= weights[i]
            i -= 1
        else: # skip
            i -= 1
    
    print(path)

    return dp(n-1, W)
