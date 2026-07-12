from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        sortedArr = sorted(arr)

        print(sortedArr)

        mapped = {}
        i = 1
        for k in range(n):
            if k != 0 and sortedArr[k] != sortedArr[k - 1]:
                i += 1
            mapped[sortedArr[k]] = i
        
        print(mapped)

        ans = []
        for key in arr:
            ans.append(mapped[key])

        return ans
        