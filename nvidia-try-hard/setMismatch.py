from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        valid = [False] * (n+1)
        
        ans = []
        print(valid)
        for i in range(n):
            if valid[nums[i]]:
                ans.append(nums[i])
            else:
                valid[nums[i]] = True
        
        print(valid)
        for i in range(1, n + 1):
            if not valid[i]:
                ans.append(i)
        
        return ans