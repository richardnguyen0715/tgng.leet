from typing import List


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        
        # Time limit excceded
        n = len(heights)
        ans = float("-inf")
        
        for i in range(n):
            
            temp_heights = heights.copy()
            # peak = temp_heights[i]
            
            # peak to end
            for j in range(i + 1, n):
                while temp_heights[j] > temp_heights[j - 1]:
                    temp_heights[j] -= 1
            
            # start to peak
            for j in range(i - 1, -1, -1):
                while temp_heights[j] > temp_heights[j + 1]:
                    temp_heights[j] -= 1
                
            # print(f"peak: {peak} - {temp_heights}")
            
            ans = max(ans, sum(temp_heights))
        
        return ans

                

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        left = [0] * n
        right = [0] * n
        
        stack = []
        
        for i in range(n):
            while stack and stack[-1][1] > heights[i]:
                stack.pop()
            
            if not stack:
                left[i] = heights[i] * (i + 1)
        
            else:
                prev_index = stack[-1][0]
                
                left[i] = left[prev_index] + heights[i] * (i - prev_index)
            
            stack.append((i, heights[i]))
        
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] > heights[i]:
                stack.pop()
            
            if not stack:
                right[i] = heights[i] * (n - i)
            
            else:
                next_idx = stack[-1][0]
                right[i] = right[next_idx] + heights[i] * (next_idx - i)
            
            stack.append((i, heights[i]))
            
        maxSum = 0
        for i in range(n):
            total = left[i] + right[i] - heights[i]
            maxSum = max(maxSum, total)
            
        
        return maxSum