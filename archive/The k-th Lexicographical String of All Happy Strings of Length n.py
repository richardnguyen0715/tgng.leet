class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

        res = []
        digits = ['a', 'b', 'c']

        def dfs(currCandi, prevDigit):
            nonlocal res
            if len(currCandi) == n:
                res.append("".join(currCandi))
                return
            
            for digit in digits:
                if digit != prevDigit:
                    currCandi.append(digit)
                    dfs(currCandi, digit)
                    currCandi.pop()
        
        
        dfs([], "")
        
        # print(res)
        if k > len(res):
            return ""
        
        return res[k - 1]