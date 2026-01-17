class Solution:
    def hammingWeight(self, n: int) -> int:

        # Time: O(32) = O(1); Or: O(K) with K is the number of bits of N
        # Space: O(1)
        
        # Call getBit func
        def getBit(x, k):
            return ( x >> k) & 1

        res = 0

        for i in range(32):
            if getBit(n, i) == 1:
                res += 1
        
        return res
    

class Solution:
    def hammingWeight(self, n: int) -> int:

        # Time: O(K) with K is the number of bits of N
        # Space: O(1)
        
        res = 0
        while n != 0:
            if n&1 == 1:
                res += 1
            n = n >> 1
        return res
    
    
class Solution:
    def hammingWeight(self, n: int) -> int:

        # Time: O(K) with K is the number of bits of 1 in N
        # Space: O(1)
        
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res