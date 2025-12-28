class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        iLeft = bisect_left(nums, target)
        if iLeft == len(nums) or nums[iLeft] != target:
            return [-1, -1]
        
        iRight = bisect_right(nums, target)
        return [iLeft, iRight - 1]