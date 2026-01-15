from typing import List


# Time Complexity: O(N)
# Space Complexity: O(N) 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hash_table = {}

        for idx, num in enumerate(numbers):

            need_num = target - num

            # print(need_num)

            if need_num not in hash_table: # O(1)
                hash_table[num] = idx
                # print(idx)
            else:
                need_idx = hash_table[need_num]

                if need_idx < idx:
                    return [need_idx + 1, idx + 1]
                else:
                    return [idx + 1, need_idx + 1]
            
        
        return -1
            

        
# TLE -> Time: O(N^2), Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        
        for i in range(0, n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                

# Binary Searchs

# 1 2 3 4 5 , target 4, mid 3

# Time: O(NLogN)
# Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binarySearch(nums, left, right, target):
            
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            
            return -1
        
        n = len(numbers)
        for idx, num in enumerate(numbers):
            need = target - num
            left = idx  + 1
            right = n - 1
            ans = binarySearch(numbers, left, right, need)
            
            if ans != -1:
                return [idx + 1, ans + 1]
            


# 2 Pointers
# Time: O(N)
# Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]