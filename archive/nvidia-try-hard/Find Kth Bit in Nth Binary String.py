class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(strs):
            listStr = list(strs)
            for i, char in enumerate(listStr):
                if char == '0':
                    listStr[i] = '1'
                else:
                    listStr[i] = '0'
            return listStr[::-1]
        
        def findString(n):
            if n == 1:
                return "0"
            
            preStr = findString(n-1)
            # print(f"s[{n - 1}] = {preStr}")
            
            return preStr + "1" + "".join(invert(preStr))

        resStr = findString(n)
        print(f"s[{n}] = {resStr}")
        return resStr[k - 1]
    

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s: str) -> str:
            s = s[::-1]  # reverse
            return ''.join('1' if c == '0' else '0' for c in s)
        
        def findString(n):
            if n == 1:
                return "0"
            
            preStr = findString(n-1)
            # print(f"s[{n - 1}] = {preStr}")
            
            return preStr + "1" + "".join(invert(preStr))

        resStr = findString(n)
        print(f"s[{n}] = {resStr}")
        return resStr[k - 1]


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n: int, k: int) -> int:
            # trả về 0 hoặc 1
            if n == 1:
                return 0  # S_1 = "0"
            
            length = (1 << n) - 1          # 2^n - 1
            mid = (length + 1) // 2        # 2^{n-1}
            
            if k == mid:
                return 1
            elif k < mid:
                return helper(n - 1, k)
            else:
                # vị trí đối xứng trong S_{n-1}
                pos = length - k + 1
                # bit ở S_n[k] = invert(bit ở S_{n-1}[pos])
                return 1 - helper(n - 1, pos)
        
        return str(helper(n, k))