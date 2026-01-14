class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Time: O(N + N) = O(2N) = O(N)
        # Space: O(1)

        if len(s) != len(t):
            return False

        letter_s = [0] * 26
        letter_t = [0] * 26

        for idx in range(len(s)): # O(N)
            letter_s[ord(s[idx]) - ord('a')] += 1
            letter_t[ord(t[idx]) - ord('a')] += 1
        
        return letter_s == letter_t # O(N)
