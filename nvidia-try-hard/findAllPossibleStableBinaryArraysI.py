class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        # Time limit Exceeded
        nLength = zero + one

        def checkStable(number, limit, zero, one):
            n = len(number)
            # Kiểm tra điều kiện 3: mọi subarray có size > limit phải chứa cả 0 và 1
            for i in range(n):
                for j in range(i + limit, n):  # j - i + 1 > limit
                    subarray = number[i:j+1]
                    
                    # Kiểm tra xem subarray có chứa cả 0 và 1 không
                    hasZero = '0' in subarray
                    hasOne = '1' in subarray
                    
                    if not (hasZero and hasOne):
                        return False
            
            return True

        count = 0
        for number in range(1, 2 ** nLength - 1):
            binNum = format(number, f'0{nLength}b')
            
            # Đếm tổng số 0 và 1
            totalZero = binNum.count('0')
            totalOne = binNum.count('1')

            if totalZero != zero and totalOne != one:
                continue

            # print(binNum)
            if checkStable(binNum, limit, zero, one):
                count += 1
        
        return count % (10 ** 9 + 7)


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k] = số cách để có i số 0, j số 1, kết thúc bằng k (0 hoặc 1)
        from functools import lru_cache
        
        
        # OKE!!
        @lru_cache(None)
        def dp(i, j, last):
            # Base cases
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            
            result = 0
            
            if last == 0:  # Kết thúc bằng 0
                # Có thể thêm từ 1 đến min(i, limit) số 0 liên tiếp
                for k in range(1, min(i + 1, limit + 1)):
                    result = (result + dp(i - k, j, 1)) % MOD
            else:  # Kết thúc bằng 1
                # Có thể thêm từ 1 đến min(j, limit) số 1 liên tiếp
                for k in range(1, min(j + 1, limit + 1)):
                    result = (result + dp(i, j - k, 0)) % MOD
            
            return result
        
        return (dp(zero, one, 0) + dp(zero, one, 1)) % MOD
    
    

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][last] = số cách tạo array có i số 0, j số 1, kết thúc bằng 'last'
        # last = 0 nghĩa là kết thúc bằng 0, last = 1 nghĩa là kết thúc bằng 1
        dp = {}
        
        # Memory Limit Exceeded
        def solve(zeros_left, ones_left, last_digit, consecutive_count):
            # Base case
            if zeros_left == 0 and ones_left == 0:
                return 1
            if zeros_left < 0 or ones_left < 0:
                return 0
            if consecutive_count > limit:
                return 0
                
            # Memoization
            state = (zeros_left, ones_left, last_digit, consecutive_count)
            if state in dp:
                return dp[state]
            
            result = 0
            
            # Thêm số 0
            if zeros_left > 0:
                if last_digit == 0:
                    # Tiếp tục chuỗi 0
                    if consecutive_count < limit:
                        result += solve(zeros_left - 1, ones_left, 0, consecutive_count + 1)
                else:
                    # Bắt đầu chuỗi 0 mới
                    result += solve(zeros_left - 1, ones_left, 0, 1)
            
            # Thêm số 1
            if ones_left > 0:
                if last_digit == 1:
                    # Tiếp tục chuỗi 1
                    if consecutive_count < limit:
                        result += solve(zeros_left, ones_left - 1, 1, consecutive_count + 1)
                else:
                    # Bắt đầu chuỗi 1 mới
                    result += solve(zeros_left, ones_left - 1, 1, 1)
            
            result %= MOD
            dp[state] = result
            return result
        
        # Bắt đầu với số 0 hoặc số 1
        result = 0
        if zero > 0:
            result += solve(zero - 1, one, 0, 1)
        if one > 0:
            result += solve(zero, one - 1, 1, 1)
            
        return result % MOD
    

from collections import deque

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        L = limit + 1
        
        # Khởi tạo base case
        dp0_prev, dp1_prev = [0] * (one + 1), [0] * (one + 1)
        for j in range(1, min(one, limit) + 1):
            dp1_prev[j] = 1  # Array chỉ có j số 1 (≤ limit)
        
        # Deque để lưu L hàng gần nhất của dp1 (tối ưu memory)
        dp1q = deque([dp1_prev[:]])
        
        for i in range(1, zero + 1):
            dp0, dp1 = [0] * (one + 1), [0] * (one + 1)
            
            # Base case: array chỉ có i số 0
            if i <= limit:
                dp0[0] = 1
            
            # Lấy hàng cũ để trừ đi (sliding window)
            old1 = dp1q[0] if i >= L else None
            
            for j in range(1, one + 1):
                # dp0[i][j]: kết thúc bằng 0
                # = tổng dp1[k][j] với k từ max(0,i-limit) đến i-1
                # = dp1[i-1][j] + dp1[i-2][j] + ... + dp1[max(0,i-limit)][j]
                # = (dp0[i-1][j] + dp1[i-1][j]) - dp1[i-limit-1][j] (nếu có)
                dp0[j] = (dp0_prev[j] + dp1_prev[j] - (old1[j] if old1 else 0)) % mod
                
                # dp1[i][j]: kết thúc bằng 1  
                # = tổng dp0[i][k] với k từ max(0,j-limit) đến j-1
                # = dp0[i][j-1] + dp0[i][j-2] + ... + dp0[i][max(0,j-limit)]
                # = (dp0[i][j-1] + dp1[i][j-1]) - dp0[i][j-limit-1] (nếu có)
                dp1[j] = (dp0[j-1] + dp1[j-1] - (dp0[j-L] if j >= L else 0)) % mod
            
            # Cập nhật deque và previous arrays
            dp1q.append(dp1[:])
            if len(dp1q) > L:
                dp1q.popleft()
            
            dp0_prev, dp1_prev = dp0, dp1
        
        return (dp0_prev[one] + dp1_prev[one]) % mod