from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Monotonic increasing stack (lưu index)
        res = 0
        n = len(heights)
        
        for i in range(n):
            # Khi gặp cột thấp hơn, tính diện tích cho các cột cao hơn trước đó
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]  # Độ cao của hình chữ nhật
                # Tính chiều rộng: từ cột sau stack[-1] đến trước i
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            
            stack.append(i)
        
        # Xử lý các cột còn lại trong stack
        while stack:
            h = heights[stack.pop()]
            w = n if not stack else n - stack[-1] - 1
            res = max(res, h * w)
        
        return res