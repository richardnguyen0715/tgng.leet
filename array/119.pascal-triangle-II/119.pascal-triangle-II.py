from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = [1]

        for _ in range(rowIndex):

            ans.append(1)

            for j in range(len(ans) -2, 0, -1):
                ans[j] += ans[j- 1]
        
        return ans