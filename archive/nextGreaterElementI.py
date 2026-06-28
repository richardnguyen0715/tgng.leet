from typing import List


# Time: O(N * M), space: O(1) => beat: 5.95% time, 8.44% space
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        res = [-1] * n

        for i in range(n):
            j = 0
            while nums2[j] != nums1[i]:
                j += 1
            
            if j != m - 1:
                
                right = j + 1

                while right < m and nums2[right] < nums2[j]:
                    right += 1
                
                if right < m:
                    res[i] = nums2[right]

        return res


# Time: O(M*N), space: O(1) -> beat: 5.01% time, 18.61% space
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        res = [-1] * n

        for i in range(n):
            j = m - 1
            max_res = -1
            # print("i :", i)
            while j > 0 and nums2[j] != nums1[i]:
                if nums2[j] > nums1[i]:
                    # print("get greater j: ", j)
                    max_res = nums2[j]
                j -= 1
            
            if max_res != nums1[i]:
                res[i] = max_res

        return res
