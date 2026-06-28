class Solution:
    def convert(self, s: str, numRows: int) -> str:

        
        res = []
        for arr_idx in range(numRows):
            res.append([])
        
        cnt = 0
        sign = 1
        n = numRows - 1
        for character in s:
            # print(character)
            res[cnt].append(character)
            if cnt + sign > n or cnt + sign < 0:
                sign *= -1
            cnt += sign
            # print("next", cnt, sign)
        
        ans = ""
        for rw in res:
            ans += "".join(rw)
        
        return ans
        
            