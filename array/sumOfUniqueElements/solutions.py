from typing import List

class Solutions:
	def sumOfUnique(self, nums: List[int]) -> int:
		"""
		Time Comp: O(2M+N)
		Space Comp: O(M)
		"""
		max_val = max(nums)
		fre_arr = [0] * (max_val + 1) # M
		for v in nums: # N
			fre_arr[v] += 1
		result = 0
		for idx, val in enumerate(fre_arr): # M
			if val == 1:
				result += idx
		return result