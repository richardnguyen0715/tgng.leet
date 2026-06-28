class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        # If needle is longer than haystack, it can't be found
        if needle_len > haystack_len:
            return -1
        
        # Check each possible starting position
        for i in range(haystack_len - needle_len + 1):
            # Check if substring starting at i matches needle
            if haystack[i:i + needle_len] == needle:
                return i
        
        return -1
    


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(0, n):
            if haystack[i:min(i+m,n)] == needle:
                return i
        
        return -1