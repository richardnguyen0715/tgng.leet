from typing import List
from collections import defaultdict
import math

# Time: O(N)
# Space: O(N)

# Beat: 5% Time, 12% Space
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        
        countStorage = defaultdict(int)
        numsDegree = 0
        valueDegree = set()
        for num in nums:
            countStorage[num] += 1
            if countStorage[num] > numsDegree:
                numsDegree = countStorage[num]
        
        for key, val in countStorage.items():
            if val == numsDegree:
                valueDegree.add(key)

        print(valueDegree)
        n = len(nums)
        res = math.inf
        for val in valueDegree:
            left = 0
            right = n - 1
            while nums[left] != val:
                left += 1
            while nums[right] != val:
                right -= 1
            
            res = min(res, right - left + 1)
        
        return res


# Time: O(N)
# Space: O(N)

# Beat: 70% Time, 11% Space
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        
        currentMax = 0
        countStorage = {}

        for idx, num in enumerate(nums):
            if num not in countStorage:
                countStorage[num] = [1, idx, math.inf]
            else:
                countStorage[num][0] += 1
                countStorage[num][2] = idx
                if countStorage[num][0] > currentMax:
                    currentMax = countStorage[num][0]
        
        res = math.inf
        for num, val in countStorage.items():
            if val[0] == currentMax:
                res = min(res, val[2] - val[1] + 1)
        
        return res if res != math.inf else 1