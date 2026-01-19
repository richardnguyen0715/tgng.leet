from typing import List
from collections import deque


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        # Idea: [1,2,1] with circle -> [1, 2, 1, 1, 2, 1] == circle!!!
        
        n = len(nums)
        dup_nums = nums.copy()
        for num in nums:
            dup_nums.append(num)
            
        res = [0] * n
        stack = deque()
        
        for i in range(2*n - 1, -1, -1):
            while len(stack) > 0 and stack[0] <= dup_nums[i]:
                stack.popleft()
            
            if i < n:
                if len(stack) == 0:
                    res[i] = -1
                else:
                    res[i] = stack[0]
            stack.appendleft(dup_nums[i])
            
        return res
        
        