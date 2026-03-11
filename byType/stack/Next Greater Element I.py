from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        next_greater = {}
        stack = []
        
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            
            while stack and stack[-1] <= num:
                stack.pop()
            
            next_greater[num] = stack[-1] if stack else -1
            
            stack.append(num)
        
        return [next_greater[num] for num in nums1]