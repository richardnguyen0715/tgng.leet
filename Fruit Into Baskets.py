from typing import List
from collections import deque




# Cách này bị TLE
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # Có 2 rổ, mỗi rổ chứa duy nhất một loại, lấy từ trái qua phải
        # mỗi rổ có thể chứa vô hạn số lượng
        # Mỗi ô chỉ lấy được 1 trái
        # Nếu quyết định lấy rồi mà gặp loại T3 thì ko thể lấy nữa (từ trái qua phải)
        
        fruitTypes = deque()
        left = 0
        n = len(fruits)
        ans = float("-inf")
        cur_sum = 0

        for right in range(n):
            fruitType = fruits[right]
            # print("Process: ", fruitType)

            fruitTypes.append(fruitType)
            

            while fruitTypes and len(set(fruitTypes)) > 2: # O(N) cho len(set())
                # print(f"left: {left} will be removed, current_sum: {cur_sum}, before fruitTypes: {fruitTypes}")
                left += 1
                fruitTypes.popleft() # O(N)
                # print(f"After left: {left}, after fruitTypes: {fruitTypes}")
            
            # print(f"passed - current fruitTypes: {fruitTypes}")
            cur_sum = len(fruitTypes)
            ans = max(cur_sum, ans)
            # print(f"{right} right - current max: {ans}")
        
        return ans


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}  # {fruit_type: count}
        left = 0
        max_fruits = 0
        
        # Time: O(n)
        # Space: O(n) hoặc O(min(n,k)) - n là số phần tử, k là số loại trái cây trong hash <= 2 => nên có thể là O(1) nếu best case
        
        for right in range(len(fruits)):
            # Thêm fruit vào window
            fruit_type = fruits[right]
            fruit_count[fruit_type] = fruit_count.get(fruit_type, 0) + 1
            
            # Thu nhỏ window nếu có > 2 loại fruit
            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                
                # Xóa fruit type nếu count = 0
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                
                left += 1
            
            # Update kết quả
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits