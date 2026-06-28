class Solution:
    def maxPower(self, s: str) -> int:
        
        res = 0
        left = 0
        cur = 0

        for right in range(0, len(s)):
            char = s[right]

            while s[left] != char:
                cur -= 1
                left += 1
            
            cur += 1
            res = max(res, cur)
        
        return res