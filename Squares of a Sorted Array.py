from typing import List


class Solution:
    # Time: O(NLogN)
    # Space: O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [num * num for num in nums]
        res.sort()
        return res
    
    

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Time: O(N)
        # Space: O(1)
        
        n = len(nums)
        left = 0
        right = n - 1
        pos = n - 1
        res = [0] * n

        while left <= right:
            leftSquared = nums[left] * nums[left]
            rightSquared = nums[right] * nums[right]

            if leftSquared >= rightSquared:
                res[pos] = leftSquared
                left += 1
            else:
                res[pos] = rightSquared
                right -= 1

            pos -= 1

        return res
