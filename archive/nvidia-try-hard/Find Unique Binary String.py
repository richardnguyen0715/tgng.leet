from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        nums = set(nums)
        res = ""

        def dfs(candidates):
            nonlocal nums, res
            if len(candidates) == n:
                ans = "".join(candidates)

                if ans not in nums:
                    res = ans
                
                return
            
            for i in ["1", "0"]:
                candidates.append(i)
                dfs(candidates)
                candidates.pop()
            
        dfs([])
        return res
    
    
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        intNums = set()
        for num in nums:
            intNums.add(int(num, 2))
        
        n = len(nums)
        
        for i in range(2 ** n):
            if i not in intNums:
                return bin(i)[2:].zfill(n)
            

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        res = []
        
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        
        return "".join(res)