def maximalRectangle(matrix):
    if not matrix:
        return 0
    
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for row in matrix:
        # Cập nhật heights
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        
        # Tính largest rectangle in histogram
        max_area = max(max_area, largestRectangleInHistogram(heights))
    
    return max_area

def largestRectangleInHistogram(heights):
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area