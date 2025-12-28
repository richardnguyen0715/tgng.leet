from typing import List

class NumArray:
	"""
	Prefix sum
	"""

	def __init__(self, nums: List[int]):
		"""
		n = length of nums
		Sum of: nums[0: i], i: 0 -> n - 1
		Pool: n + 1 -> Contain nums
		=> Sum of nums[left: right+1] = pool[right+1] - pool[left]
		---
		Space Comp: O(n)
		Time Comp: O(n)
		"""
		self.pool = [0]
		for v in nums:
			self.pool.append(self.pool[-1] + v)
		
	
	def sumRange(self, left: int, right: int) -> int:
		"""
		Return: sum(nums[left: right+1])
		Time Comp: O(1)
		Space Comp: O(1)
		"""
		return self.pool[right+1] - self.pool[left]