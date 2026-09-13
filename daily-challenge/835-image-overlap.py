from typing import List


# Time Limit Exceeded
class Solution01:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        one_count_1 = 0
        one_count_2 = 0

        one_list_1 = []
        one_list_2 = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one_count_1 += 1
                    one_list_1.append([i, j])
                if img2[i][j] == 1:
                    one_count_2 +=1 
                    one_list_2.append([i, j])
        
        # print(one_count_1)
        # print(one_list_1)

        # print(one_count_2)
        # print(one_list_2)

        if one_count_1 == 0 or one_count_2 == 0:
            return 0
        
        directions = ["left", "right", "top", "bottom"]

        def translate(one_list, direction):
            new_one_list = []

            for x, y in one_list:

                if direction == "left":
                    new_x = x
                    new_y = y - 1

                elif direction == "right":
                    new_x = x
                    new_y = y + 1

                elif direction == "top":
                    new_x = x - 1
                    new_y = y

                elif direction == "bottom":
                    new_x = x + 1
                    new_y = y

                if 0 <= new_x < n and 0 <= new_y < n:
                    new_one_list.append([new_x, new_y])

            return new_one_list

        def compareMatrix(one_list_1, one_list_2):
            ans = 0
            n = len(one_list_1)
            m = len(one_list_2)

            for i in range(n):
                one_1 = one_list_1[i]
                for j in range(m):
                    one_2 = one_list_2[j]
                    if one_1[0] == one_2[0] and one_1[1] == one_2[1]:
                        ans += 1
                        break
            
            return ans
            
        ans = 0

        def dfs(one_list, depth):
            nonlocal ans

            if depth > 2 * (n - 1):
                return

            ans_dfs = compareMatrix(one_list, one_list_2)
            ans = max(ans, ans_dfs)

            for direction in directions:
                new_one_list = translate(one_list, direction)
                dfs(new_one_list, depth + 1)
                
        dfs(one_list_1, 0)
        return ans

# Time Limit Exceeded
# Cách này thay vì lưu one_list luôn thì chỉ cần lưu dx, dy là độ dịch chuyển
class Solution02:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        one_list_1 = []
        one_list_2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one_list_1.append([i, j])

                if img2[i][j] == 1:
                    one_list_2.append([i, j])

        if not one_list_1 or not one_list_2:
            return 0

        # Dùng set để kiểm tra một điểm có tồn tại trong img2 hay không
        one_set_2 = set(map(tuple, one_list_2))

        directions = [
            (0, -1),   # left
            (0, 1),    # right
            (-1, 0),   # top
            (1, 0)     # bottom
        ]

        ans = 0

        def dfs(dx, dy, depth):
            nonlocal ans

            if depth > 2 * (n - 1):
                return

            # Tính overlap của phép dịch (dx, dy)
            overlap = 0

            for x, y in one_list_1:
                new_x = x + dx
                new_y = y + dy

                if (new_x, new_y) in one_set_2:
                    overlap += 1

            ans = max(ans, overlap)

            # Thử 4 hướng
            for move_x, move_y in directions:
                dfs(
                    dx + move_x,
                    dy + move_y,
                    depth + 1
                )

        dfs(0, 0, 0)

        return ans
    
    
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        one_list_1 = []
        one_set_2 = set()

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one_list_1.append((i, j))

                if img2[i][j] == 1:
                    one_set_2.add((i, j))

        if not one_list_1 or not one_set_2:
            return 0

        ans = 0

        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):

                overlap = 0

                for x, y in one_list_1:
                    new_x = x + dx
                    new_y = y + dy

                    if (new_x, new_y) in one_set_2:
                        overlap += 1

                ans = max(ans, overlap)

        return ans
    

# Kiều gì thì kiểu dx, dy cũng nằm trong đoạn [-(n-1), n-1]?
# Solution này ok: O(N^2 * M) với N là kích thước ma trận và M là số lượng số 1
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        one_list_1 = []
        one_set_2 = set()

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one_list_1.append((i, j))

                if img2[i][j] == 1:
                    one_set_2.add((i, j))

        if not one_list_1 or not one_set_2:
            return 0

        ans = 0

        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):

                overlap = 0

                for x, y in one_list_1:
                    new_x = x + dx
                    new_y = y + dy

                    if (new_x, new_y) in one_set_2:
                        overlap += 1

                ans = max(ans, overlap)

        return ans
    
    

# Cách này tham khảo
# Solution này ngắn nhất: (beat 78%) O(K x M) với K M lần lượt là số lượng số 1 của 2 ma trận
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        one_list_1 = []
        one_list_2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one_list_1.append((i, j))

                if img2[i][j] == 1:
                    one_list_2.append((i, j))

        if not one_list_1 or not one_list_2:
            return 0

        shifts = {}

        for x1, y1 in one_list_1:
            for x2, y2 in one_list_2:

                dx = x2 - x1
                dy = y2 - y1

                shifts[(dx, dy)] = shifts.get((dx, dy), 0) + 1

        return max(shifts.values())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    