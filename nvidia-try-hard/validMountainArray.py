from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        right = len(arr) - 1
        n = len(arr)

        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1

        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1

        return left > 0 and right < n - 1 and left == right