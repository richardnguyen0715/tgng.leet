class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Time: O(M)
        # Space: O(1)
        
        n = len(s1)
        m = len(s2)
        
        if m < n:
            return False
    
        need = [0] * 26
        slide_w = [0] * 26
        
        # hash s1
        for char in s1:
            need[ord(char) - ord('a')] += 1
        
        # sliding
        for i in range(m):
            slide_w[ord(s2[i]) - ord('a')] += 1
            
            # Độ lớn của cửa sổ lớn hơn rồi -> trượt lên trên, tức là loại bỏ i - n
            if i >= n:
                slide_w[ord(s2[i - n]) - ord('a')] -= 1
            
            if need == slide_w:
                return True
        
        return False
                
                
                

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Time: O(M)
        # Space: O(1)

        def getHash(char):
            return 1 << (ord(char) - ord('a'))
        
        
        def checkPermutation(a, b):
            arrA = list(a)
            arrB = list(b)
            arrA.sort()
            arrB.sort()
            return arrA == arrB


        n = len(s1)
        m = len(s2)
        
        if m < n:
            return False

        s1Hash = 0
        s2Hash = 0

        for i in range(n):
            s1Hash += getHash(s1[i])
            s2Hash += getHash(s2[i])

        for i in range(n, m):
            if s1Hash == s2Hash and checkPermutation(s1, s2[i - n: i]):
                return True
            
            s2Hash -= getHash(s2[i - n])
            s2Hash += getHash(s2[i])


        print(s1Hash)
        print(s2Hash)

        print(s2[m - n: m])
                
        return s1Hash == s2Hash and checkPermutation(s1, s2[m - n: m])