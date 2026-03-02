def solutions(nums):

    # time: O(N)
    # space: O(1)
    
    max_sum_one = 0
    max_sum_two = 0
    
    for val in nums:
        take = max_sum_two + val
        skip = max_sum_one
        
        cur_best = max(take, skip)
        
        max_sum_two = max_sum_one
        max_sum_one = cur_best
    
    return max_sum_one
    

print(solutions([2, 7, 9, 3, 1]))