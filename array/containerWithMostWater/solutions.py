def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    max = -1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        print(left,":", right, ':', area)
        if area > max:
            max = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
    return max
    
if __name__ == "__main__":
    # height = [1, 2, 3, 1000, 9]
    height = [1,1]
    # height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))