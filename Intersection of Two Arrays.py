from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [k for k in set(nums1) if k in set(nums2)]