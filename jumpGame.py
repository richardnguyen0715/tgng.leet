from typing import List



# Time Limit Exceeded
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        last_idx = len(nums) - 1
        flag = False
        def dfs(curr):
            nonlocal flag

            if curr == last_idx:
                flag = True
                return
            
            if curr > last_idx:
                return

            for i in range(1, nums[curr] + 1):
                curr += i
                dfs(curr)
                curr -= i

        dfs(0)
        return flag


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        # time: O(N)
        # space: O(1)

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        
        return True