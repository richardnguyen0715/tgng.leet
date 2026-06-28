from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(0, n):
                if i != j and nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans