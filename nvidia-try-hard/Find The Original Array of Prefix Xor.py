from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        ans = pref.copy()
        for i in range(1, len(pref)):
            ans[i] = pref[i] ^ pref[i-1]

        # print(ans)
        return ans