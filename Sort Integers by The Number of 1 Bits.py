from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        res = []
        for inter in arr:
            res.append((inter.bit_count(), inter))

        res.sort()
        print(res)

        return [ans[1] for ans in res]