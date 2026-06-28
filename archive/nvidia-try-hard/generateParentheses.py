from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        can = []
        
        def dfs(i, cur_open):
            if i == 2 * n:
                if cur_open == n:
                    res.append("".join(can.copy()))
                
                return

            if cur_open < n:
                can.append("(")
                cur_open += 1
                dfs(i + 1, cur_open)
                cur_open -= 1
                can.pop()
            
            cur_close = i - cur_open
            if cur_close < cur_open:
                can.append(")")
                dfs(i+1, cur_open)
                can.pop()
            
        dfs(0, 0)
        return res