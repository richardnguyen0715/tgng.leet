from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        
        left = [0] * n
        right = [0] * n
        
        stack = []
        
        for i in range(n):
            while stack and stack[-1][1] > maxHeights[i]:
                stack.pop()
            
            if not stack:
                left[i] = maxHeights[i] * (i + 1)
        
            else:
                prev_index = stack[-1][0]
                
                left[i] = left[prev_index] + maxHeights[i] * (i - prev_index)
            
            stack.append((i, maxHeights[i]))
        
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] > maxHeights[i]:
                stack.pop()
            
            if not stack:
                right[i] = maxHeights[i] * (n - i)
            
            else:
                next_idx = stack[-1][0]
                right[i] = right[next_idx] + maxHeights[i] * (next_idx - i)
            
            stack.append((i, maxHeights[i]))
            
        maxSum = 0
        for i in range(n):
            total = left[i] + right[i] - maxHeights[i]
            maxSum = max(maxSum, total)
            
        
        return maxSum