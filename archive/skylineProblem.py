from typing import List


def skylineProblem(nums: List[int]):
    
    n = len(nums)
    res = []
    for i in range(n):
        found = False
        for j in range(i - 1, -1, -1): # [i - 1, -1) = [i - 1, 0]
            if nums[j] > nums[i]:
                found = True
                res.append(j)
                break
            
        if not found:
            res.append(-1)
            
    return res


# Refactor code
def skylineProblem(nums: List[int]):
    
    # Time: O(N^2)
    
    n = len(nums)
    res = []
    for i in range(n):
        j = i - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        res.append(j)
            
    return res


# Sử dụng stack để optimize
from collections import deque


def skylineStack(nums: List[int]):
    
    # Time: O(N) - Mỗi phần tử chỉ vào và ra stack tối đa đúng 1 lần.
    # Space: O(N)
    
    stack = deque()
    n = len(nums)
    res = []
    
    for i in range(n):
        while len(stack) > 0 and nums[stack[0]] <= nums[i]:
            stack.popleft()
        
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[0])
        
        stack.appendleft(i)
    
    return res

print(skylineStack([8, 3, 4, 3, 5, 9]))