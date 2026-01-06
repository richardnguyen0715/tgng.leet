from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) <= 1:
            return [nums]
        
        # Find all of the combinations of nums
        result = nums.copy()
        n = len(nums)
        nums.sort()
        combinations = []
        combination = []
        visited = set()
        def find_combinations(curr):
            visited.add(curr)
            combination.append(nums[curr])
            
            # print(combination)
            
            if len(combination) == n and combination not in combinations:
                combinations.append(combination.copy())
                return
            
            for i in range(0, n):
                if i not in visited:
                    find_combinations(i)
                    visited.remove(i)
                    combination.pop()
            
            
        for i in range(0, n):
            find_combinations(i)
            combination = []
            visited = set()
            # print("Done")
        
        return combinations
    
    
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def p(nums, used, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i] == False:
                    used[i] = True
                    curr.append(nums[i])
                    p(nums, used, curr)
                    used[i] = False
                    curr.pop()


        used = [False] * len(nums)
        res = []
        p(nums, used, [])
        return res

            
