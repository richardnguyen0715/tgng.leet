def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = (right + left) // 2
        print(left, mid, right)
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid 
    return -1

def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)
    while left <= right:
        mid = (right + left) // 2
        print(left , mid, right)
        if arr[mid] >= target:
            ans = mid   
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return ans


arr = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(lower_bound(arr, 3))