from typing import List



# Time Limit Exceeded
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        current_solution = []

        current_sum = 0
        def choose(i):
            # Chọn que thứ i, tới n là hết que
            if i == n:
                if sum(current_solution) == target:
                    ans.append(current_solution.copy())
                
                return
            
            for freq in range(target // candidates[i] + 1):
                for j in range(freq):
                    current_solution.append(candidates[i])
                choose(i+1)
                for j in range(freq):
                    current_solution.pop()

        choose(0)

        return ans
    
    

# Pruning -> Sum >= Target ? Stop : Continue
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        current_solution = []

        current_sum = 0
        def choose(i):
            
            if i == n or sum(current_solution) >= target:
                if sum(current_solution) == target:
                    ans.append(current_solution.copy())
                
                return
            
            for freq in range(target // candidates[i] + 1):
                for j in range(freq):
                    current_solution.append(candidates[i])
                choose(i+1)
                for j in range(freq):
                    current_solution.pop()

        choose(0)

        return ans
    
    
# Tính current sum sẵn
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        current_solution = []

        current_sum = 0
        def choose(i):
            nonlocal current_sum
            if i == n or current_sum >= target:
                if current_sum == target:
                    ans.append(current_solution.copy())
                
                return
            
            for freq in range(target // candidates[i] + 1):
                for j in range(freq):
                    current_solution.append(candidates[i])
                current_sum += freq * candidates[i]
                choose(i+1)
                current_sum -= freq * candidates[i]
                for j in range(freq):
                    current_solution.pop()

        choose(0)

        return ans
    


# Loại bỏ hết tất cả phần tử lớn hơn target sau khi sort tăng dần
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        for i in range(len(candidates)):
            if candidates[i] > target:
                candidates = candidates[:i]
                break

        n = len(candidates)
        ans = []
        current_solution = []

        current_sum = 0
        def choose(i):
            nonlocal current_sum
            if i == n or current_sum >= target:
                if current_sum == target:
                    ans.append(current_solution.copy())
                
                return
            
            for freq in range(target // candidates[i] + 1):
                for j in range(freq):
                    current_solution.append(candidates[i])
                current_sum += freq * candidates[i]
                choose(i+1)
                current_sum -= freq * candidates[i]
                for j in range(freq):
                    current_solution.pop()

        choose(0)

        return ans
    

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        path = []

        def dfs(start, remain):
            if remain == 0 :
                res.append(path.copy())

            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:
                    break
                
                path.append(x)
                dfs(i, remain-x)
                path.pop()


        dfs(0, target)
        return res