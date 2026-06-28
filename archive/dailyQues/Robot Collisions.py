from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        # Wrong Answers!!!!!!!!!!
        
        n = len(positions)
        newPositions = positions.copy()
        newHealths = healths.copy()
        originalIndices = list(range(n))
        
        # Kiểm tra xem robot idx có khả năng va chạm với robot nào không
        def heristics(positions, directions, healths, idx):
            n = len(positions)
            direction = directions[idx]
            position = positions[idx]
            health = healths[idx]
            
            # Robot đã chết
            if health <= 0:
                return False
            
            for i in range(n):
                if i == idx or healths[i] <= 0:
                    continue
                
                checkPosition = positions[i]
                checkDirection = directions[i]
                
                # Chỉ xét va chạm khi:
                # - Robot idx đi sang phải (R) và robot i đi sang trái (L)
                # - Robot idx ở bên trái robot i
                if direction == 'R' and checkDirection == 'L' and position < checkPosition:
                    return True
                
                # Hoặc ngược lại:
                # - Robot idx đi sang trái (L) và robot i đi sang phải (R)
                # - Robot idx ở bên phải robot i
                if direction == 'L' and checkDirection == 'R' and position > checkPosition:
                    return True
            
            return False
        
        # Simulation: mỗi vòng lặp là một bước thời gian
        while True:
            noCross = 0
            
            # Bước 1: Di chuyển các robot
            for i in range(n):
                if newHealths[i] <= 0:
                    noCross += 1
                    continue
                
                # Kiểm tra xem robot có khả năng va chạm không
                prob = heristics(newPositions, directions, newHealths, i)
                if not prob:
                    noCross += 1
                    continue
                
                # Di chuyển robot
                direction = directions[i]
                if direction == 'R':
                    newPositions[i] += 1
                else:
                    newPositions[i] -= 1
            
            # Nếu không còn robot nào có thể va chạm, dừng simulation
            if noCross == n:
                break
            
            # Bước 2: Xử lý va chạm
            collisions = []
            
            # Tìm tất cả các cặp va chạm
            for i in range(n):
                if newHealths[i] <= 0:
                    continue
                
                for j in range(i + 1, n):
                    if newHealths[j] <= 0:
                        continue
                    
                    # Va chạm xảy ra khi:
                    # 1. Cùng vị trí và ngược hướng
                    # 2. Hoặc vượt qua nhau (robot i từ trái sang, robot j từ phải sang)
                    pos_i = newPositions[i]
                    pos_j = newPositions[j]
                    dir_i = directions[i]
                    dir_j = directions[j]
                    
                    # Trường hợp 1: Cùng vị trí
                    if pos_i == pos_j and dir_i != dir_j:
                        collisions.append((i, j))
                    
                    # Trường hợp 2: Vượt qua nhau
                    # Robot i đi sang phải, robot j đi sang trái
                    # Và vị trí hiện tại: i >= j (đã vượt qua)
                    # Và vị trí trước đó: i < j
                    elif dir_i == 'R' and dir_j == 'L':
                        prev_pos_i = pos_i - 1
                        prev_pos_j = pos_j + 1
                        
                        # Kiểm tra xem có vượt qua nhau không
                        if prev_pos_i < prev_pos_j and pos_i >= pos_j:
                            collisions.append((i, j))
            
            # Bước 3: Xử lý các va chạm
            for i, j in collisions:
                # Kiểm tra lại vì có thể robot đã chết trong va chạm trước
                if newHealths[i] <= 0 or newHealths[j] <= 0:
                    continue
                
                if newHealths[i] > newHealths[j]:
                    newHealths[i] -= 1
                    newHealths[j] = 0
                elif newHealths[i] < newHealths[j]:
                    newHealths[j] -= 1
                    newHealths[i] = 0
                else:
                    newHealths[i] = 0
                    newHealths[j] = 0
        
        # Trả về kết quả theo thứ tự ban đầu
        result = []
        for i in range(n):
            if newHealths[i] > 0:
                result.append(newHealths[i])
        
        return result


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        n = len(positions)
        indices = list(range(n))  # Lưu chỉ số ban đầu
        
        # Sắp xếp theo vị trí
        robots = list(zip(positions, healths, directions, indices))
        robots.sort()
        
        stack = []  # Stack để xử lý va chạm
        
        for pos, health, direction, idx in robots:
            if direction == 'R':
                # Robot đi sang phải, thêm vào stack
                stack.append([pos, health, direction, idx])
            else:
                # Robot đi sang trái, xử lý va chạm với robots đi sang phải
                while stack and stack[-1][2] == 'R' and health > 0:
                    # Va chạm xảy ra
                    r_pos, r_health, r_dir, r_idx = stack[-1]
                    
                    if r_health > health:
                        # Robot phải thắng
                        stack[-1][1] = r_health - 1  # Giảm 1 máu
                        health = 0  # Robot trái chết
                    elif r_health < health:
                        # Robot trái thắng
                        stack.pop()  # Robot phải chết
                        health -= 1  # Robot trái giảm 1 máu
                    else:
                        # Hòa nhau, cả 2 chết
                        stack.pop()
                        health = 0
                
                # Nếu robot trái còn sống, thêm vào stack
                if health > 0:
                    stack.append([pos, health, direction, idx])
        
        # Tạo kết quả theo thứ tự ban đầu
        result = [0] * n
        for pos, health, direction, idx in stack:
            result[idx] = health
        
        # Lọc bỏ các robot đã chết (health = 0)
        return [health for health in result if health > 0]