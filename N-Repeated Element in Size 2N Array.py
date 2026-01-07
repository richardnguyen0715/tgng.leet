from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        exist = set()
        for num in nums:
            if num not in exist:
                exist.add(num)
            else:
                return num