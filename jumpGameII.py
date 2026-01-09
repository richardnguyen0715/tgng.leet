from typing import List


# Memory Limit Exceeded
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        from collections import deque
        queue = deque()
        n = len(nums)

        # Path, Max_Reach: [0], nums[0]
        queue.append(([0], nums[0]))

        while queue:
            path, max_reach = queue.popleft()
            
            if path[-1] + max_reach >= n - 1:
                return len(path)
        
            for i in range(1, max_reach + 1):  # Sửa: từ 1 đến max_reach
                next_pos = path[-1] + i
                if next_pos < n:  # Kiểm tra bounds
                    new_path = path + [next_pos]  # Sửa: tạo new list thay vì append
                    queue.append((new_path, nums[next_pos]))

        return -1  # Không thể reach được



class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        from collections import deque
        queue = deque()
        n = len(nums)

        # Path, Max_Reach: [0], nums[0]
        queue.append(([0], nums[0]))

        while queue:
            path, max_reach = queue.popleft()
            
            if path[-1] + max_reach >= n - 1:
                return len(path)
        
            for i in range(max_reach, 0, -1):  # Sửa: từ 1 đến max_reach
                next_pos = path[-1] + i
                if next_pos < n:  # Kiểm tra bounds
                    new_path = path + [next_pos]  # Sửa: tạo new list thay vì append
                    queue.append((new_path, nums[next_pos]))

        return -1  # Không thể reach được


from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        queue = deque()
        visited = set()  # Tránh revisit
        
        queue.append((0, 0))  # (position, steps)
        visited.add(0)
        
        while queue:
            pos, steps = queue.popleft()
            
            # Thử tất cả possible jumps
            for jump in range(1, nums[pos] + 1):
                next_pos = pos + jump
                
                if next_pos >= len(nums) - 1:
                    return steps + 1
                
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, steps + 1))
        
        return -1
    
    
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        from collections import deque
        queue = deque()
        n = len(nums)
        visited = set([0])

        # Path, Max_Reach: [0], nums[0]
        queue.append(([0], nums[0]))

        while queue:
            path, max_reach = queue.popleft()
            
            if path[-1] + max_reach >= n - 1:
                return len(path)
        
            for i in range(max_reach, 0, -1):  # Sửa: từ 1 đến max_reach
                next_pos = path[-1] + i

                if next_pos < n and next_pos not in visited:  # Kiểm tra bounds
                    new_path = path + [next_pos]  # Sửa: tạo new list thay vì append
                    queue.append((new_path, nums[next_pos]))

                    visited.add(next_pos)


        return -1  # Không thể reach được
    
    
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        count = 0
        max_reach = 0
        curr_pos = 0

        for i in range(len(nums) - 1): # Loại bỏ phần tử cuối cùng ra do không cần thiết
            step = nums[i]
            max_next_step = i + step
            max_reach = max(max_reach, max_next_step)

            if i == curr_pos: # Tức là đã đi tới bước max reach hiện tại rồi
                curr_pos = max_reach
                count += 1

        return count
