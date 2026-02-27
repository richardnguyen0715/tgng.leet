def solution(nums):
    
    # Skyline prolems????
    # Idea: Using Stack?....

    stack = [] # Store the positions
    n = len(nums)
    result = [-1] * n
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        
        stack.append(i)
    
    return result
    


print(solution([4, 5, 2, 25]))