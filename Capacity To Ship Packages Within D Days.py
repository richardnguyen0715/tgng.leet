from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # left phải luôn lớn hơn hoặc bằng max của weights, vì nếu nhỏ hơn thì ko thể ship được các kiện hàng lớn
        left = max(weights)
        right = sum(weights)
        ans = -1

        def cntDayNeeded(cap):
            
            # luôn cần tối thiểu 1 ngày
            dayNeeded = 1
            sumCap = 0

            for weight in weights:
                # Nếu trọng lượng vượt qua capacity thì reset rồi cộng qua cho ngày mới
                if sumCap + weight > cap:
                    dayNeeded += 1
                    sumCap = 0
                sumCap += weight
            
            return dayNeeded


        while left <= right:
            mid = (left + right) // 2

            if cntDayNeeded(mid) <= days:
                ans = mid
                # Tìm nhỏ nhất nên đá phải sang
                right = mid - 1
            else:
                left = mid + 1
        
        return ans