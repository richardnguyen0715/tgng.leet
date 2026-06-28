

# TLE
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0

        while x < n:
            if 1 << x == n:
                return True
            
            x += 1
        
        return False
    


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n /= 2
            
        return n == 1
    
    

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0 or n % 2 != 0 and n != 1:
            return False
        
        left = 0
        right = n // 2
        while left <= right:
            mid = (right + left) // 2
            if 1 << mid == n:
                return True
            elif 1 << mid > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return False