from typing import List
from collections import deque
import math


# ý tưởng: -> tìm đoạn subarray rộng nhất mà nhận phần tử thứ i là min trước -> sau đó tính tổng sau
# left[i] -> vị trí bên trái i mà gần i nhất sau cho nhỏ hơn i
# right[i] -> vị trí bên phải i mà gần i nhất sau cho nhỏ hơn i
# khi đó i sẽ là phần tử nhỏ nhất trong đoạn left[i] + 1 và right[i] - 1; vì left[i] < i  và right[i] < i


# Chỉ ok khi dãy toàn là số dương
 
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        # Mục tiêu của prefix sum là để tính tổng dãy với O(1); sum[i, j] = prefix[j] - prefix[i - 1]       
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        stack = deque()
        left = [0] * n
        right = [0] * n
        
        # Tìm bên trái trước
        for i in range(0, n):
            
            while len(stack) > 0 and nums[stack[0]] >= nums[i]:
                stack.popleft()
                
            if len(stack) > 0:
                left[i] = stack[0]
            else:
                left[i] = -1
            stack.appendleft(i)
            
        stack.clear()
        
        # Tìm bên phải sau
        for i in range(n - 1, -1, -1):
            
            while len(stack) > 0 and nums[stack[0]] >= nums[i]:
                stack.popleft()
                
            if len(stack) > 0:
                right[i] = stack[0]
            else:
                right[i] = n

            stack.appendleft(i)
        
        res = math.inf * -1
        for i in range(0, n):
            
            sum = prefix_sum[right[i] - 1]
            
            if left[i] != -1:
                sum -= prefix_sum[left[i]]
            
            res = max(res, sum * nums[i])
            
        
        return res % 1000000007