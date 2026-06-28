from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 #since we're comparing their neighbours right cannot be at end it must have a neightbour to compare with

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid  # instead of mid - 1 do mid since mid can be the peak too

        return l