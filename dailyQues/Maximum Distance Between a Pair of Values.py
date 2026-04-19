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
    
import bisect

class Solution:
    def maxDistance(self, nums1, nums2):
        ans = 0
        
        for i, x in enumerate(nums1):
            l, r = i, len(nums2) - 1
            pos = i - 1
            
            while l <= r:
                mid = (l + r) // 2
                if nums2[mid] >= x:
                    pos = mid
                    l = mid + 1
                else:
                    r = mid - 1
                    
            ans = max(ans, pos - i)
        
        return ans