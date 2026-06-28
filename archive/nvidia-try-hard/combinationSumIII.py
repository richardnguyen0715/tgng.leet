from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = []
        res = set()

        def dfs(start: int, current_sum: int):
            if len(candidates) == k:
                if current_sum == n:
                    # không sort để debug cho dễ
                    # print(candidates)
                    # print(sum(candidates))
                    # print(current_sum)
                    res.add(tuple(candidates))
                return
       
            for i in range(start, 10):
                if current_sum + i > n:
                    break
                candidates.append(i)
                dfs(i + 1, current_sum + i)
                candidates.pop()

        dfs(1, 0)
        print(res)
        return [list(ans) for ans in res]