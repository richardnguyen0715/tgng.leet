from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        res = []

        for i in range(2 ** n):
            gray = i ^ (i >> 1)
            res.append(gray)
        
        return res
    

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        # Base case
        result = [0, 1]
        
        # Build từ n=1 lên n
        for i in range(2, n + 1):
            # Reflect: đảo ngược thứ tự
            reflected = result[::-1]
            
            # Prefix: thêm bit 1 vào đầu cho phần reflected
            prefix_bit = 1 << (i - 1)  # 2^(i-1)
            
            # Thêm vào kết quả
            for num in reflected:
                result.append(prefix_bit | num)
        
        return result