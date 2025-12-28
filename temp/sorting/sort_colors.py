class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == 0:
                nums = self.swap(nums, count, i)
                count += 1
        
        for i in range(n):
            if nums[i] == 1:
                nums = self.swap(nums, count, i)
                count += 1

    def swap(self, nums, i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums

# [2,0,2,1,1,0]
# 1. 0, 0, 2, 1, 2
# 2. 0, 0, 1, 2, 2 -> stop
        