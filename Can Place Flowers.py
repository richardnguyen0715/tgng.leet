from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], m: int) -> bool:
        n = len(flowerbed)

        if m == 0:
            return True

        for i in range(n):
            bef = True
            aft = True
            if flowerbed[i] == 0:
                if i - 1 >= 0:
                    if flowerbed[i - 1] == 1:
                        bef = False
                
                if i + 1 <= n - 1:
                    if flowerbed[i + 1] == 1:
                        aft = False
                
                if bef and aft:
                    m -= 1
                    flowerbed[i] = 1
                
                if m <= 0:
                    break
        
        return m == 0
                    