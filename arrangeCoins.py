import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = int(math.sqrt(2*n))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            cntCoinNeeded = mid * (mid + 1) // 2
            if cntCoinNeeded <= n: # Đang tìm thằng lớn hơn nên lấy bên trái trước
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans