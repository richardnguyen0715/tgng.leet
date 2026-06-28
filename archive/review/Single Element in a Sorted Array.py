from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        left = 0
        right = n - 1

        # Quy luật: chẵn-lẻ bằng nhau nếu như không có single point, từ single point trở đi sẽ bị lệch khỏi quy luật, ví dụ:
        # Không có single point: 1 1 2 2 3 3 4 4 ... -> lẻ bất kì sẽ bằng lẻ + 1 (chẵn)
        # Có single point: 1 1 2 2 3 3 4 5 5 ... -> lẻ khác chắn tại 4 -> đã xuất hiện single point!!!!, 1 1 2 2 3 3 vẫn đúng quy luật -> chưa có single point

        while left < right:

            mid = left + (right - left) // 2 # avoid out of the number of bits -> change in to a new num
            
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        
        return nums[left]
