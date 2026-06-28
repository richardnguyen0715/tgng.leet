from functools import lru_cache


class Solution:
    @lru_cache(None)
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        
        mapHash = []
        i = 0
        while i < len(prev):
            char = prev[i]
            count = 1
            
            # Đếm số ký tự giống nhau liên tiếp
            while i + 1 < len(prev) and prev[i + 1] == char:
                count += 1
                i += 1
            
            mapHash.append((char, count))
            i += 1

        ans = ""
        for char, count in mapHash:
            ans += f"{count}{char}"

        print(n, mapHash, ans)

        return ans
        

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        result = ""
        
        i = 0
        while i < len(prev):
            char = prev[i]
            count = 1
            
            # Đếm ký tự giống nhau liên tiếp
            while i + 1 < len(prev) and prev[i + 1] == char:
                count += 1
                i += 1
            
            # Thêm vào kết quả: count + char
            result += str(count) + char
            i += 1
            
        return result
    

from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        
        result = ""
        for char, group in groupby(prev):
            count = len(list(group))
            result += str(count) + char
            
        return result