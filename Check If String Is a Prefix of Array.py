from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        cur = ""
        for w in words:
            cur += w
            if cur == s:
                return True
            if len(cur) > len(s):
                return False
        return False
