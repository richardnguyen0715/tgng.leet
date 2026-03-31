class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        n = len(s1)

        if n != len(s2):
            return False
        
        s1_even = []
        s1_odd = []
        s2_even = []
        s2_odd = []

        for i in range(n):

            if i % 2 == 0:
                s1_even.append(s1[i])
                s2_even.append(s2[i])
            else:
                s1_odd.append(s1[i])
                s2_odd.append(s2[i])

        s1_even.sort()
        s2_even.sort()
        s1_odd.sort()
        s2_odd.sort()

        return s1_even == s2_even and s1_odd == s2_odd
    

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return (sorted(s1[::2]) == sorted(s2[::2]) and 
                sorted(s1[1::2]) == sorted(s2[1::2]))
