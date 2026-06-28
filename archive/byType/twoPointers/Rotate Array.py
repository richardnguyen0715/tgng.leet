from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        temp = temp * 2
        n = len(nums)
        k %= n
        ans = temp[n - k:2*n - k]
        for idx in range(n):
            nums[idx] = ans[idx]
        

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        if k == 0:
            return
        
        count = 0
        
        start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                temp = nums[next_idx]
                nums[next_idx] = prev
                prev = temp
                current = next_idx
                count += 1
                
                if start == current:
                    break
            
            start += 1
            

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        # Reverse toàn bộ array
        nums.reverse()
        
        # Reverse k phần tử đầu
        nums[:k] = nums[:k][::-1]
        
        # Reverse n-k phần tử cuối
        nums[k:] = nums[k:][::-1]