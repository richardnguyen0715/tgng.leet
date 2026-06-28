from typing import List


# Time Limit Exceeded
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums
        
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
        
        ans = -1
        for idx, arr in enumerate(combinations):
            if arr == result:
                ans = idx
                break

        ans += 1
        print(ans)
        if ans > len(combinations) - 1:
            ans = 0
        
        print(combinations)
        print(ans)
        nums[:] = combinations[ans]
        
        

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        
        # 1. Find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 2. If pivot exists, find successor and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. Reverse suffix
        nums[i + 1:] = reversed(nums[i + 1:])
