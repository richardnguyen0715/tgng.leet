from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        visited = [False] * (n + 1)
        for num in nums:
            visited[num] = True
        ans = []
        for i in range(1, n + 1):
            if not visited[i]:
                ans.append(i)
        return ans