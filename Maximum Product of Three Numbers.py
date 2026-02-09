from typing import List
import math


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        maxProd = -math.inf
        currProd = 1

        def getProd(nums, left, right):
            k = nums[left]
            for num in nums[left + 1: right + 1]:
                k *= num
            return k


        for right in range(n):
            num = nums[right]

            print("right: ", right)
            print("nums right - nums left", num, nums[left])
            while right - left + 1 > 3:
                numLeft = nums[left]
                if numLeft != 0:
                    currProd //= numLeft
                else:
                    currProd = getProd(nums, left + 1, right)
                left += 1
            
            currProd *= num
            print("currPrd: ", currProd)
            if right - left + 1 == 3:
                maxProd = max(maxProd, currProd)
        
        
        return maxProd


# Time: O(NLogN)
# Space: O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        lastMax = nums[n-3] * nums[n-2] * nums[n-1]
        print("last", lastMax)
        firstMax = nums[0] * nums[1] * nums[n - 1]
        print("first", firstMax)
        return max(lastMax, firstMax)
