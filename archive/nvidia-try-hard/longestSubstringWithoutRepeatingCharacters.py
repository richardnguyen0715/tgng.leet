class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        
        if n <= 1:
            return n
        
        ans = 0
        start = 0
        set_char = set()
        i = 0
        
        while i < n:
            if s[i] not in set_char:
                set_char.add(s[i])
            else:
                ans = max(ans, len(set_char))
                
                duplicated = s[i]
                
                while start < i and s[start] != duplicated:
                    start += 1
                start += 1
            
                set_char = set()
                for j in range(start, i + 1):
                    set_char.add(s[j])
                
            i += 1
        
        if set_char:
            ans = max(ans, len(set_char))
            
        return ans
        
        