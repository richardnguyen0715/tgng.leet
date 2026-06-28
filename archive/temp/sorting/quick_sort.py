def quickSort(nums, start, end):
    
    if start >= end:
        return nums
    import random
    count = start
    pivot = random.randint(start, end) # 2. pivot = end, 3. pivot = random.randint(start, end)
    nums = swap(nums, pivot, end)
    for i in range(start, end):
        if nums[i] <= nums[end]:
            nums = swap(nums, i, count)
            count += 1
    swap(nums, count, end)
    left_nums = quickSort(nums, start, count - 1)
    right_nums = quickSort(left_nums, count + 1, end)
    
    return right_nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    return nums

test_list = [1, 2, 4, 5, 2, 4, 6, 7, 2, 4, 7]
print(quickSort(test_list, 0, len(test_list) - 1))