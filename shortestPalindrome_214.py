
# Beat: 7% Time and 56% space
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s
        
        def isPalindrome(s): # O(N), N = |s|
            # left = 0
            # right = len(s) - 1
            # while left <= right:
            #     if s[left] != s[right]:
            #         return False
            #     left += 1
            #     right -= 1
            # return True
            return s == s[::-1]
        
        if isPalindrome(s):
            return s
        
        n = len(s)
        reversed_s = s[::-1]

        for i in range(n):
            for j in range(n - i):
                prefix = reversed_s[j:j+i]
                new_s = prefix + s
                if isPalindrome(new_s):
                    return new_s
                break
                    
                
            
            
                