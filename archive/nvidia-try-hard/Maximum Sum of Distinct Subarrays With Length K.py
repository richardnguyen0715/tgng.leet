from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Tìm tổng lớn nhất của subarray độ dài k với các phần tử khác nhau.
        
        Time Complexity: O(n) - mỗi phần tử được thêm/xóa đúng 1 lần
        Space Complexity: O(k) - tối đa k phần tử trong hash map
        """
        n = len(nums)
        if n < k:
            return 0
        
        freq = defaultdict(int)  # Đếm tần suất các phần tử trong window
        current_sum = 0
        max_sum = 0
        
        # Khởi tạo window đầu tiên
        for i in range(k):
            freq[nums[i]] += 1
            current_sum += nums[i]
        
        # Kiểm tra window đầu tiên
        if len(freq) == k:  # Tất cả phần tử đều distinct
            max_sum = current_sum
        
        # Sliding window
        for i in range(k, n):
            # Thêm phần tử mới (bên phải)
            freq[nums[i]] += 1
            current_sum += nums[i]
            
            # Xóa phần tử cũ (bên trái)
            left_element = nums[i - k]
            freq[left_element] -= 1
            current_sum -= left_element
            
            # Nếu tần suất = 0, xóa khỏi map
            if freq[left_element] == 0:
                del freq[left_element]
            
            # Cập nhật kết quả nếu tất cả phần tử distinct
            if len(freq) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum