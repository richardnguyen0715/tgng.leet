from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        import math
        
        res = math.inf
        n = len(nums)
        
        total = sum(nums)
        
        for i in range(0, 2 ** n): # Số trường hợp có thể có của các dãy bit, ví dụ n = 3 thì có tối đa 8 trường hợp -> duyệt các số từ 0 (tương ứng 000) đến 2^N - 1 (tương ứng 111)     
            qSum = 0
            for j in range(0, n): # Số bit có trong từng trường hợp, n = 3 thì dãy có tối đa 3 bit. Ví dụ [1,0,1] tương ứng với [x, z]

                if (i >> j) & 1 == 1: # Tức là dãy bit i, tại vị trí j có giá trị là 1, tương ứng nums[j] có tồn tại trong path
                    qSum += nums[j]
            
            if (abs(total - qSum - qSum) > res):
                res = abs(total - qSum - qSum)
            
        return res
    