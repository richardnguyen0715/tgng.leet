from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
                
        backtrack([])
        return res
    
    
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = set()

        def dfs(candidates, visited):
            nonlocal res
            if len(candidates) == n:
                res.add(tuple(candidates.copy()))
                return

            for j in range(n):
                if j not in visited:
                    visited.add(j)
                    candidates.append(nums[j])
                    dfs(candidates, visited)
                    visited.remove(j)
                    candidates.pop()
            
        dfs([], set())
        res = [list(arr) for arr in res]
        return res
                