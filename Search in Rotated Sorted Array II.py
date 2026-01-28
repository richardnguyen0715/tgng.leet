from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            # Duplicates rồi thì bỏ luôn 2 biên trái phải, ví kiểu như 10 1 10 10 10 thì thu lại còn 1 10 10
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[mid] == nums[right]: # != nums[left]
                right -= 1
            
            elif nums[mid] > nums[right]: # Minimum sẽ ở nữa bên phải
                left = mid + 1 # bỏ luôn mid vì mid đã lớn hơn right
            
            else:
                right = mid # lấy mid vì mid chỉ nhỏ hơn thôi nhưng ko biết nhỏ nhất hay không
        
        return nums[left]