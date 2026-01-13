

# TLE
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Time: O(N^3)
        # Space: O(1)
        if not s:
            return ""
        
        ans = [0, 0]
        for left in range(0, len(s)):
            for right in range(left + 1, len(s)):
                
                if self.isPalindrome(s, left, right) and (right - left > ans[1] - ans[0]):
                    ans = [left, right]
        
        return s[ans[0]:ans[1] + 1]
    
    
    def isPalindrome(self, s: str, left, right) -> bool:
        
        while left <= right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
            
        return True
    


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Time: O(N^2)
        # Space: O(1)

        if not s:
            return ""

        ans = [0, 0]
        for idx in range(len(s) - 1):
            left, right = self.extend(s, idx, idx)
            if right - left > ans[1] - ans[0]:
                ans = [left, right]
            
            if s[idx] == s[idx + 1]:
                left, right = self.extend(s, idx, idx + 1)
                if right - left > ans[1] - ans[0]:
                    ans = [left, right]

        return s[ans[0]:ans[1] + 1]

    def extend(self, s, i1, i2):
        while 0 <= i1 and i2 < len(s) and s[i1] == s[i2]:
            i1 -= 1
            i2 += 1
        return i1 + 1, i2 - 1