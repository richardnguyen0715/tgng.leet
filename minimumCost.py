from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        # Nums[0] luôn được chọn
        # Ta chỉ cần tìm 2 phần tử nhỏ nhất tiếp theo nhưng vẫn giữ được thứ tự i < j -> tự đúng khi sort lại mảng từ nums[1:]
        
        rest = sorted(nums[1:])
        return nums[0] + rest[0] + rest[1]
