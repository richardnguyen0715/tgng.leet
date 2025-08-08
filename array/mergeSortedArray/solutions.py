from typing import List

class Solutions:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		---
		TWO POINTER METHODS:
			Length of nums1 = k ( k = m + n )
			nums1 = [1, 2, 3, 0, 0, 0], nums2 = [2, 5, 6], n = 3, m = 3.
			3 - 6 => 6
			3 - 5 => 5
			3 - 2 => 3
			2 - 2 => 2
			1, 2 - ... => 1, 2
			nums1 = [1, 2, 2, 3, 5, 6]
		---
		Time Comp: O(1)
		Space Comp: O(m + n)
		"""
		k = m + n - 1
		i1, i2 = m - 1, n - 1
  
		while i1 >= 0 and i2 >= 0:
			if nums1[i1] >= nums2[i2]:
				nums1[k] = nums1[i1]
				i1 -= 1
			else:
				nums1[k] = nums2[i2]
				i2 -= 1
			k -= 1
   
		while i1 >= 0:
			nums1[k] = nums1[i1]
			i1 -= 1
			k -= 1
   
		while i2 >= 0:
			nums1[k] = nums2[i2]
			i2 -= 1
			k -= 1