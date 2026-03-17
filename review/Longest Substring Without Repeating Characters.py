class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n <= 1:
            return n
        
        charSet = set()
        left = 0
        ans = 0
        
        for right in range(n):
            char = s[right]

            if char not in charSet:
                charSet.add(char)
            else:
                ans = max(ans, len(charSet))

                while left <= right and s[left] != char:
                    charSet.remove(s[left])
                    left += 1
                
                left += 1
            
        ans = max(ans, len(charSet))
            
        return ans



