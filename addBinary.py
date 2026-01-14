class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = int(a, 2) + int(b, 2) # Time Complexity: O(1)
        return str(bin(ans))[2:] # Time Complexity: O(logN)