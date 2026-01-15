from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # Time: O(N)
        # Space: O(128)
        
        cnt = Counter(p)
        n = len(s)
        left = 0
        ans = []

        for right in range(n):
            c = s[right]
            cnt[c] -= 1

            while cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1

            if right - left + 1 == len(p):  # Khi tìm được toàn bộ phần tử thoả thì 100% là anagram
                ans.append(left)
        
        return ans
            
            