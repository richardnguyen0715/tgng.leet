from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        x = nums[:n//2]
        y = nums[n//2:]
        ans = []
        for xi, yi in zip(x, y):
            ans.append(xi)
            ans.append(yi)
        
        return ans