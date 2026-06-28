from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stack lưu index của các phần tử chưa tìm được next greater
        
        # Duyệt 2 vòng để xử lý circular array
        for i in range(2 * n):
            current_idx = i % n  # Circular index
            current_val = nums[current_idx]
            
            # Pop các phần tử nhỏ hơn current_val
            # Vì current_val lớn hơn → nó là next greater của các phần tử đó
            while stack and nums[stack[-1]] < current_val:
                idx = stack.pop()
                res[idx] = current_val
            
            # Chỉ push index trong lần duyệt đầu tiên (i < n)
            # Lần duyệt thứ 2 chỉ để tìm next greater, không thêm vào stack
            if i < n:
                stack.append(current_idx)
        
        return res