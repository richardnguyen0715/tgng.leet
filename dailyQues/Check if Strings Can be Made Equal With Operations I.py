class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        def dfs(sList, target, i):

            if i == 2:
                if "".join(sList) == target:
                    return True
                return False

            # swap
            newSList = sList.copy()
            j = i + 2 
            newSList[i], newSList[j] = newSList[j], newSList[i]
            swap = dfs(newSList, target, i + 1)

            # no swap
            noSwap = dfs(sList, target, i + 1)

            return swap or noSwap
        
        changeS1 = dfs(list(s1), s2, 0)
        changeS2 = dfs(list(s2), s1, 0)
        
        return changeS1 or changeS2
            