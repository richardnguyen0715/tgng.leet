class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        for i in range(n):
            insta = max(nums[0:i+1]) - min(nums[i:n])
            # print(insta)
            if insta <= k:
                return i
        
        return -1
        
