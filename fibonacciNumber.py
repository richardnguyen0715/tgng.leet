class Matrix22:
    def __init__(self, a00, a01, a10, a11):
        self.a00 = a00
        self.a01 = a01
        self.a10 = a10
        self.a11 = a11
    
    def matMul(self, anMat):
        b00 = self.a00 * anMat.a00 + self.a01 * anMat.a10
        b01 = self.a00 * anMat.a01 + self.a01 * anMat.a11
        b10 = self.a10 * anMat.a00 + self.a11 * anMat.a10
        b11 = self.a10 * anMat.a01 + self.a11 * anMat.a11
        return Matrix22(b00, b01, b10, b11)

    def matPow(self, n):
        if n == 0:
            return Matrix22(1, 0, 0, 1)
        
        if n == 1:
            return self
        
        half = self.matPow(n//2)

        if n % 2:
            return self.matMul(half.matMul(half))
        return half.matMul(half)


class Solution:
    # Time: O(LogN)
    # Space: O(N ^ 2)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        matA = Matrix22(1, 1, 1, 0)
        matB = matA.matPow(n - 1)
        return matB.a00

# ----

# Time: O(N)
# Space: O(N)
class Solution:
# manual implement @lru_cache(None)
    def __init__(self):
        self.memo = {}  

    def fib(self, n: int) -> int:

        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            return n

        return_val = self.fib(n-1) + self.fib(n-2)  
        self.memo[n] = return_val
        return return_val
    
    

import numpy as np

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        A = np.array([[1, 1],
                      [1, 0]], dtype=object)

        def mat_pow(mat, power):
            result = np.identity(2, dtype=object)
            while power > 0:
                if power & 1:
                    result = result @ mat
                mat = mat @ mat
                power >>= 1
            return result

        res = mat_pow(A, n - 1)
        return res[0][0]
    
    
    
class Solution:
    def fib(self, n: int) -> int:

        dp, dpPrev1, dpPrev2 = 0, 1, 0

        for i in range(2, n + 1):
            dp = dpPrev1 + dpPrev2
            dpPrev2 = dpPrev1
            dpPrev1 = dp
        
        return dp
