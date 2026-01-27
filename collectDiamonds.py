def collectDiamonds(nums, start, end, height):
    
    # Time: O(NLogN) , Suy Biến thì O(N^2)
    
    if start == end:
        return 1

    if start > end:
        return 0

    # Tìm minIndex trong đoạn start
    minIndex = start
    for i in range(start + 1, end + 1):
        if nums[i] < nums[minIndex]:
            minIndex = i
        
    verticalResult = end - start + 1 # Ăn theo cột -> thì ăn hết cột, ví dụ [1,3] -> ăn 3 cột
    horizontalResult = nums[minIndex] - height # Ăn theo hàng thì ăn hết hàng tính từ thằng thấp nhất đến độ cao hiện tại
    
    # ăn xong hàng thì còn dư bên trái và phải của minIndex có cột cao hơn nó -> tính cho cột cao hơn nó.
    leftResult = collectDiamonds(nums, start, minIndex - 1, nums[minIndex])
    rightResult = collectDiamonds(nums, minIndex + 1, end, nums[minIndex])
    horizontalResult = horizontalResult + leftResult + rightResult
    
    return min(verticalResult, horizontalResult)


def runCollect(nums):
    return collectDiamonds(nums, 0, len(nums) - 1, 0)


print(runCollect([3, 5, 3, 3, 4, 3]))