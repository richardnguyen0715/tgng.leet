from typing import List


# Beat: 72.9% Time, 15% Space
# Time: O(N)
# Space: O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        for key, val in hash_map.items():
            if val == 1:
                return key
            
       
# Beat: 72% time, 23% space
# Time: O(N)
# Space: O(1)     
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        return ones
    

# Beat: 19% Time, 40% Space
# Time: O(32 ^ N)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0

        for i in range(32):
            count = 0

            for num in nums:
                if num & ( 1 << i):
                    count += 1
            
            if count % 3:
                result |= (1 << i)
            
        return result if result < 2**31 else result - 2 **32