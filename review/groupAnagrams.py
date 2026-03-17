from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            
            groups[tuple(freq)].append(string)
        
        return list(groups.values())