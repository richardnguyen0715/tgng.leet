from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pointer = 0
        ans = []
        for i in range(1, n + 1):
            print(i, pointer)
            if pointer < len(target) and i == target[pointer]:
                ans.append("Push")
                pointer += 1
            else:
                ans.append("Push")
                ans.append("Pop")
            if pointer == len(target):
                break
        return ans