from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left = 0
        right = n - 1


        left_max = 0 
        right_max = 0

        water = 0
        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:

                    left_max = height[left]
                
                else:
                    water = water + (left_max - height[left])

                left += 1

            else:

                if height[right] >= right_max:

                    right_max = height[right]
                
                else:
                    water = water + (right_max - height[right])
                
                right -= 1

        return water