from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        # O(N * K * LogK)
        for s in strs:
            key = ''.join(sorted(s))
            mp.setdefault(key, []).append(s)

        return list(mp.values())



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        # O(N*K)

        for word in strs:
            # Đếm tần suất ký tự
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1

            # tuple dùng làm key vì hash được
            groups[tuple(freq)].append(word)

        return list(groups.values())
