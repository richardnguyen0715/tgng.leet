def solutions(nums):

    # Time: O(N)
    # Space: O(1)
    
    # Note: 
    # No need to conti!!! -> Skip + take?
        # Brute force? -> i j ? 2 ^ n?? :)) 
        # Dp? bottomUP? -> O(N)? -> Can!!!
    
    
    # Dry run: [2, 7, 9, 3, 1] -> 2, 7, 11, 11, 12
    
    if not nums:
        return 0

    # optimized space !!!! -> prev used
    
    prev1 = 0 # dp[i - 1]
    prev2 = 0 # dp[i - 2]
    
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr
    
    return prev1
    

print(solutions([2, 7, 9, 3, 1]))