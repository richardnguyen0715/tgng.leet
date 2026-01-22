from collections import bisect

class Solution:
    def searchRange(self, nums, target):
        
        iLeft = bisect.bisect_left(nums, target, lo=0, hi=len)
        if iLeft == len(nums) or nums[iLeft] != target:
            return [-1, -1]
    
        iRight = bisect.bisect_right(nums, target)
        
        return [iLeft, iRight - 1]