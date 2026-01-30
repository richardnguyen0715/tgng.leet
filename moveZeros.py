from typing import List


# Time: O(N)
# Space: O(N)
# Beat: 100% time, 12% space
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
        
        for i in range(len(nums) - len(res)):
            res.append(0)
        
        print(res)
        
        for i in range(len(nums)):
            nums[i] = res[i]
        

# Time: O(N ^ 2)
# Space: O(1)
# Beat: 5% Time, 12% Space
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return nums

        def swap(nums, a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == 0:
                j = i
                while j < n - 1 and nums[j] == 0:
                    j += 1
                swap(nums, i, j)
            i += 1