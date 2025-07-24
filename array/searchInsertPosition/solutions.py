def searchInsert(nums, val):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_bin = 0
    right_bin = len(nums)
    while(right_bin - left_bin > 1):
        median = int(left_bin + (right_bin - left_bin)//2)
        if nums[median] > val:
            right_bin = median
        elif nums[median] < val:
            left_bin = median
        else:
            return median
        print(f"left_bin: {left_bin}, right_bin: {right_bin}, median: {median}")
    if nums[left_bin] >= val:
        return left_bin
    else:
        return right_bin