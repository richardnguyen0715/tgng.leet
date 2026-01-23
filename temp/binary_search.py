def search(nums, target):
    left = 0
    right = len(nums)
    ans = 0
    while left < right:
        mid = (right + left) // 2
        
        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        
        else:
            left = mid + 1
    
    return ans

from collections import bisect

bisect.bisect_left([1, 2, 3], 2)