from typing import List



# Time limit exceeded
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Nhận xét, tốc độ ăn càng nhanh thì thời gian cần để ăn hết càng ít
        # Chạy trên k -> với K là số chuối có thể ăn trong 1 giờ
        left = 1
        right = max(piles)
        ans = -1

        def timeNeeded(k, piles):
            timeCnt = 0
            pileRemain = 0
            pile = 0
            while pile < len(piles):
                pileRemain = piles[pile] - k
                # print(f"Ăn nảy số {pile}, còn lại chuối là: {pileRemain}")

                if pileRemain > 0:
                    # print(f"Ăn chưa hết nên ăn tiếp")
                    piles[pile] = pileRemain
                    timeCnt += 1
                    continue

                timeCnt += 1
                pile += 1
            
            # print(f"Với {k} thì cần {timeCnt} giờ để ăn hết")
            
            return timeCnt

        while left <= right:
            mid = left + (right - left) // 2

            # print("mid", mid)
            timeNe = timeNeeded(mid, piles.copy())
            # print("time needed", timeNe)

            if timeNe <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    
    
    
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        # Nhận xét, tốc độ ăn càng nhanh thì thời gian cần để ăn hết càng ít
        # Chạy trên k -> với K là số chuối có thể ăn trong 1 giờ
        left = 1
        right = max(piles)
        ans = -1
        
        def timeNeeded(k, piles):
            return sum(math.ceil(pile / k) for pile in piles)

        while left <= right:
            mid = left + (right - left) // 2

            # print("mid", mid)
            timeNe = timeNeeded(mid, piles.copy())
            # print("time needed", timeNe)

            if timeNe <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Nhận xét, tốc độ ăn càng nhanh thì thời gian cần để ăn hết càng ít
        # Chạy trên k -> với K là số chuối có thể ăn trong 1 giờ
        left = 1
        right = max(piles)

        def timeNeeded(k, piles):
                    return sum(math.ceil(pile / k) for pile in piles)

        while left < right:
            mid = left + (right - left) // 2

            # print("mid", mid)
            timeNe = timeNeeded(mid, piles.copy())
            # print("time needed", timeNe)

            if timeNe <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        # Nhận xét, tốc độ ăn càng nhanh thì thời gian cần để ăn hết càng ít
        # Chạy trên k -> với K là số chuối có thể ăn trong 1 giờ
        left = 1
        right = max(piles)

        def timeNeeded(k, piles):
            timeCnt = 0
            for pile in piles:
                # Tính số giờ cần để ăn hết pile này
                # Ceiling division: (pile + k - 1) // k hoặc math.ceil(pile / k)
                timeCnt += (pile + k - 1) // k
            return timeCnt

        while left < right:
            mid = left + (right - left) // 2

            # print("mid", mid)
            timeNe = timeNeeded(mid, piles.copy())
            # print("time needed", timeNe)

            if timeNe <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
    