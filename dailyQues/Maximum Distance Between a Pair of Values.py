from typing import List


# O(MN) -> TLE
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        ans = 0
        for i in range(m):
            for j in range(i, n):
                if nums1[i] > nums2[j]: continue
                
                ans = max(ans, j - i) 
                
        return ans
    
    

from typing import List

# O(M + N)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        ans = 0
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
                
        return ans