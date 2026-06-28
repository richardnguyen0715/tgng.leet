class Solution:
    def mirrorDistance(self, n: int) -> int:
        reversed_n = int(str(n)[::-1])
        return abs(reversed_n - n)