from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        
        def buildSubset(path, idx):
            
            nonlocal nums, res
            
            if idx == len(nums):
                res.append(path.copy())
                return
            
            
            # Thử cách thêm vào path
            path.append(nums[idx])
            buildSubset(path, idx + 1)
            path.pop()
            
            
            # Thử cách không thêm vào path
            buildSubset(path, idx + 1)
            
        
        buildSubset(path, 0)
        
        return res
        

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        for i in range(0, 2 ** n): # Số trường hợp có thể có của các dãy bit, ví dụ n = 3 thì có tối đa 8 trường hợp -> duyệt các số từ 0 (tương ứng 000) đến 2^N - 1 (tương ứng 111)     
            path = []
            
            for j in range(0, n): # Số bit có trong từng trường hợp, n = 3 thì dãy có tối đa 3 bit. Ví dụ [1,0,1] tương ứng với [x, z]

                if (i >> j) & 1 == 1: # Tức là dãy bit i, tại vị trí j có giá trị là 1, tương ứng nums[j] có tồn tại trong path
                    path.append(nums[j])
            
            res.append(path)
            
        return res
        