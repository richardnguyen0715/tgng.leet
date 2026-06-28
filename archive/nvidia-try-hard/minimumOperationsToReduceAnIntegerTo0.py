class Solution:
    def minOperations(self, n: int) -> int:
        memo = {}
        
        
        # Bị TLE
        def dfs(num):
            if num == 0:
                return 0
            if num in memo:
                return memo[num]
            
            # Tìm lũy thừa của 2 gần nhất
            power = 1
            while power <= num:
                power <<= 1
            
            # Thử cả cộng và trừ
            prev_power = power >> 1
            
            # Trừ lũy thừa nhỏ hơn hoặc bằng
            result1 = 1 + dfs(num - prev_power)
            
            # Cộng lũy thừa lớn hơn
            result2 = 1 + dfs(power - num)
            
            memo[num] = min(result1, result2)
            return memo[num]
        
        return dfs(n)
    

# Cách số 2: đếm số bit 1 trong chuỗi biểu biễn, vì 2^N là một thao tác bit manipulation khá phổ biến
# Ví dụ: 39 - 100111, 39 + 1 = 40 = 101000, 40 - 8 = 32 = 100000, 32 - 32 = 0
# Có 4 bit một -> cần 4 thao tác để xử lý ; Thay vì trừ bit 1 thì có thể cộng để tạo carry, tức là nếu như có 2 bit 1 liên tiếp thì nên cộng thay vì trừ


class Solution:
    def minOperations(self, n: int) -> int:
        
        operations = 0
        
        while n > 0:
            
            if n & 1: # bit cuối cùng của n bằng 1
                if n & 2: # bit kế cuối của nó cũng bằng 1 -> lúc này cộng lên sẽ tốt hơn -> giảm nhiều bit một liên tiếp thành 1 bit một duy nhất là carry. Ví dụ: 111 (7) + 1 = 1000 (8), bit 1 ngoài cùng chính là carry
                    n += 1
                else:
                    n -= 1

                operations += 1
            else:
                # Dịch sang phải 1 bit -> mục tiêu là để thu nhỏ lại bài toán nhưng vẫn giữ nguyên bản chất, không cần cộng vì không quan tâm. Ví dụ: 1200 thì chỉ cần quan tâm 12, ko cần quan tâm 00
                n >>= 1
        
        return operations