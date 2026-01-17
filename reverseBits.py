class Solution:
    def reverseBits(self, n: int) -> int:
        
        # O(32) - Time
        # O(1) - Space

        def flipBit(n, i):
            return n ^ (1 << i)
                
        left = 0
        right = 31

        while left < right:
            i = ( n >> left ) & 1
            j = ( n >> right ) & 1

            if i != j:
                n = flipBit(n, left)
                n = flipBit(n, right)
                
                 # n = n ^ ((1 << left) | (1 << right))
            
            left += 1
            right -= 1
        
        return n
    
    

class Solution:
    def reverseBits(self, n: int) -> int:
        
        # O(32) - Time
        # O(1) - Space
        
        def setBit(n, i, pos):
            
            if i == 1:
                return n | (1 << pos)
            else:
                return n & (~(1 << pos))
                
        left = 0
        right = 31

        while left < right:
            i = ( n >> left ) & 1
            j = ( n >> right ) & 1

            if i != j:
                n = setBit(n, i, right)
                n = setBit(n, j, left)
                
            left += 1
            right -= 1
        
        return n
