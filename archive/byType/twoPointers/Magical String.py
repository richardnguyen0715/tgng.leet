class Solution:
    def magicalString(self, n: int) -> int:
        
        s = [1, 2, 2]
        i = 2
        num = 1
        
        while len(s) < n:
            count = s[i]
            s.extend([num] * count) # Lấy thêm đúng count phần tử num để có được chuỗi là chính độ dài của nó
            num = 3 - num # 2 thì thành 1 mà 1 thì thành 2
            i += 1
        
        return s[:n].count(1)