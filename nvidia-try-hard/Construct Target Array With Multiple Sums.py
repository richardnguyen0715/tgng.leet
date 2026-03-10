import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Edge case: nếu chỉ có 1 phần tử
        if len(target) == 1:
            return target[0] == 1
        
        # Sử dụng max heap (Python heapq là min heap, nên dùng số âm)
        heap = [-x for x in target]
        heapq.heapify(heap)
        
        total_sum = sum(target)
        
        while True:
            # Lấy phần tử lớn nhất
            largest = -heapq.heappop(heap)
            
            # Nếu phần tử lớn nhất là 1, ta đã về được [1,1,...,1]
            if largest == 1:
                return True
            
            # Tính tổng của các phần tử còn lại
            rest_sum = total_sum - largest
            
            # Edge cases
            if rest_sum == 1:
                return True
            if rest_sum >= largest or rest_sum == 0:
                return False
            
            # Tính giá trị trước đó của phần tử lớn nhất
            # largest = prev_val + rest_sum
            # => prev_val = largest - rest_sum
            prev_val = largest % rest_sum
            
            # Nếu prev_val = 0, nghĩa là largest = k * rest_sum
            # Trong trường hợp này, prev_val phải là rest_sum
            if prev_val == 0:
                prev_val = rest_sum
            
            # Cập nhật heap và tổng
            heapq.heappush(heap, -prev_val)
            total_sum = total_sum - largest + prev_val