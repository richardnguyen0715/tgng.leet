class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        key_map = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        cand = []
        ans = []
        n = len(digits)
        def Try(i):
            if i == n:
                ans.append("".join(cand))
                return

            for j in key_map[digits[i]]:
                cand.append(j)
                Try(i + 1)
                cand.pop()

        Try(0)
        return ans