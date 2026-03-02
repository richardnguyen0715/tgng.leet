from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Đếm số 0 trailing của mỗi hàng
        zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
        
        swaps = 0
        
        # Với mỗi vị trí i, tìm hàng phù hợp và swap lên
        for i in range(n):
            required = n - i - 1
            
            # Nếu hàng hiện tại đã OK, skip
            if zeros[i] >= required:
                continue
            
            # Tìm hàng đầu tiên thỏa mãn (từ dưới lên)
            target = -1
            for j in range(i + 1, n):
                if zeros[j] >= required:
                    target = j
                    break
            
            # Không tìm thấy → impossible
            if target == -1:
                return -1
            
            # Bubble swap target lên vị trí i
            while target > i:
                zeros[target], zeros[target - 1] = zeros[target - 1], zeros[target]
                target -= 1
                swaps += 1
        
        return swaps