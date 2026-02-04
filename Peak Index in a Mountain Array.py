from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1  # peak không thể ở index 0
        right = len(arr) - 2  # peak không thể ở index cuối
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Nếu arr[mid] < arr[mid + 1] -> peak ở bên phải
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            # Nếu arr[mid] > arr[mid + 1] -> peak ở bên trái hoặc tại mid
            else:
                right = mid
        
        return left  # left == right tại peak