from collections import lru_cache


class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        

        if n < 0:
            return 1.0 / self.myPow(x, -n)

        if n == 0:
            return 1

        half_pow = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half_pow * half_pow
        
        else:
            return x * half_pow * half_pow
        
        
    
    
# Problem: Time Limit Exceeded khi N quá lớn
class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if n > 0:
            return x * self.myPow(x, n - 1)
        else:
            return (1 / x) * self.myPow((1 / x), abs(n) - 1)