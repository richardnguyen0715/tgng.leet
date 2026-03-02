def solutions(nums, weights, target):
    
    if len(nums) == 0:
        return 0
    
    n = len(nums)
    
    left = 0
    sumNums = 0
    sumWeights = 0
    ans = 0
    
    # Sliding Window: Fail with negative
    # for right in range(n): 
    #     num = nums[right]
    #     weight = weights[right]
        
    #     while left <= right and num + sum > target:
    #         left += 1
    #         sum -= num
    #         sumWeight -= weight
        
    #     sum += num
    #     sumWeight += weight
    #     ans = max(ans, sumWeight)
    
    # return ans
    
    
    for right in range(n):
        sumNums += nums[right]
        sumWeights += weights[right]

        while sumNums > target:
            sumNums -= nums[left]
            sumWeights -= weights[left]
            left +=1
        
        ans = max(ans, sumWeights)
        
    return ans
        

A = [1, 1, 1, 1, 1, 1, 1]
W = [5, -100, 10, 10, -50, 20, 5]
K = 7

print(solutions(A,W,K))