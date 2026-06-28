from collections import combinations
from typing import List


# Time limit exceeded, but Right!!!
# Time: O(N^4)
# Space: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for combination in combinations(nums, 4):
            if sum(combination) == target:
                ans.add(tuple(combination))
        return [list(i) for i in ans]
    

# Time limit exceeded, but Right!!!
# Time: O(N^4)
# Space: O(N)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        print(nums)
        candidates = []
        ans = set()
        visited = set()
        def dfs(i):
            if len(candidates) == 4:
                if sum(candidates) == target:
                    print(candidates)
                    temp = candidates.copy()
                    temp.sort()
                    ans.add(tuple(temp))
                return
            
            candidates.append(nums[i])
            visited.add(i)

            for j in range(n):
                if j not in visited:
                    dfs(j)
            
            candidates.pop()
            visited.remove(i)

        for i in range(n):
            dfs(i)        
        
        return [list(i) for i in ans]
    

# Time: O(N^4)
# Space: O(N)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        print(nums)
        candidates = []
        ans = set()
        
        def dfs(i):
            if len(candidates) >= 4:
                if sum(candidates) == target:
                    temp = candidates.copy()
                    ans.add(tuple(temp))
                return
            
            for j in range(i, n):
                # Cùng level thì skip
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                candidates.append(nums[j])
                dfs(j + 1)
                candidates.pop()
            
        dfs(0)
        
        return [list(i) for i in ans]
    
    
# Beat: 29% time, 28% space
# Time: O(N^3)
# Space: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            # Skip duplicate cho i
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1, n - 2):
                
                # Skip duplicate cho j
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Two pointers cho 2 số còn lại
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
    

# Prunning -> Beat: 95% time, 32% space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Early termination
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Early termination cho j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result