class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)
        i = n - 1
        while 0 <= i and s[i] == " ":
            i -= 1
        
        ans = 0
        while 0 <= i and s[i] != " ":
            ans += 1
            i -= 1
        
        return ans
