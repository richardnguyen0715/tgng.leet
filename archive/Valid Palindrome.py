class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for ch in s.lower():
            if ch.isalnum():
                filtered.append(ch)
        return filtered == filtered[::-1]
