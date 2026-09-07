
# OOM rồi, O(2^N)
class Solution01:
    def distinctSubseqII(self, s: str) -> int:

        n = len(s)
        visited = set()

        def Try(candidates, pos):

            if candidates:
                visited.add("".join(candidates))

            for i in range(pos, n):
                candidates.append(s[i])

                Try(candidates, i + 1)

                candidates.pop()

        Try([], 0)

        return len(visited)
    
    
# Cách Ảo Ma chôm được
class Solution:
    def distinctSubseqII(self, s: str) -> int:

        MOD = 10**9 + 7

        end = {}

        for c in s:
            total = sum(end.values())

            end[c] = total + 1

        return sum(end.values()) % MOD