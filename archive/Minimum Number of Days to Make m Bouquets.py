from typing import List

# Nhận xét quan trọng: số ngày mà tăng thì số hoa nở tăng thì khả năng tạo được bó hoa tăng và ngược lại.


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # Time: O(N + N + LogN*N) = O(NLogN)
        # Space: O(1)
        
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1

        def calcBouquets(day):
            cntBouquets = 0
            cntConsecutiveFlowers = 0
            for d in bloomDay:
                # Hoa nở
                if d <= day:
                    cntConsecutiveFlowers += 1
                else:
                    cntBouquets += cntConsecutiveFlowers // k
                    cntConsecutiveFlowers = 0
            
            # Cộng đợt cuối cùng vì tới cuối (i = n) thì không còn điều kiện
            cntBouquets += cntConsecutiveFlowers // k
            return cntBouquets

        # mid, left, right sẽ tượng trưng cho số ngày
        while left <= right:
            mid = (left + right) // 2

            if calcBouquets(mid) >= m:
                ans = mid
                
                # Tìm minimum nên sẽ dịch về trái
                right = mid - 1
            
            else:
                left = mid + 1
        
        return ans