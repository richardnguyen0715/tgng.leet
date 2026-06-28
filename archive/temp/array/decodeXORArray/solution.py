from typing import List

class Solution:
	def decode(self, encoded: List[int], first: int) -> List[int]:
		"""
		0 xor 1 = 1
		0 xor 0 = 0
		a xor b = c => b = c xor a
		---
		Space Comp: O(1) without ouput, O(n) with output
		Time Comp: O(n)
		"""
		arr = [first]
		for v in encoded:
			arr.append(arr[-1] ^ v)
		return arr