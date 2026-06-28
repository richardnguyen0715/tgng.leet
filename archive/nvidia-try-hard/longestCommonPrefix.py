from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]
        for word in strs[1:]:
            j = 0
            while j < len(word) and j < len(res) and word[j] == res[j]:
                j += 1
            res = res[:j]
        return res