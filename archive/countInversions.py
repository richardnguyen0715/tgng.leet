def mergeAndCount(nums, n):
    if n <= 1:
        return 0

    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]

    count = mergeAndCount(left, mid)
    count += mergeAndCount(right, n - mid)
    count += merge(nums, left, right, mid, n - mid)

    return count


def merge(nums, left, right, m, n):
    i = j = k = 0
    result = 0

    while i < m and j < n:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            result += m - i
            j += 1
        k += 1

    while i < m:
        nums[k] = left[i]
        i += 1
        k += 1

    while j < n:
        nums[k] = right[j]
        j += 1
        k += 1

    return result



print(mergeAndCount([3, 5, 2, 1, 6], 5))