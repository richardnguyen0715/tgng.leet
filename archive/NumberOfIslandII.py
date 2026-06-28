# Thay vì maintain một mảng 2 chiều với parentX và parentY thì thực hiện flatten thành mảng một chiều với o(i,j) = i * m + j

# Ý tưởng là cứ thêm một thằng một vào thì check các thằng xung quanh xem nó có liên thông với thằng nào khác ko, nếu có thì gôm lại thành một đảo
# Còn nếu không thì chính là một đảo mới

def numberOfIsland(m , n, positions):
    matrix = [[0] * n for _ in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    k = m * n
    parent = [-1] * k
    
    print("matrix: \n", matrix)
    print("parent: \n", parent)
        
    res = []
    count = 0
    for x, y in positions:
        matrix[x][y] = 1
        
        u = x * m + y
        
        count += 1
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            
            if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == 1:
                v = new_x * m + new_y
                
                rootU = find(u, parent)
                rootV = find(v, parent)
                
                if rootU != rootV:
                    count -= 1
                    union(rootU, rootV, parent)
                    
        res.append(count)
    
    return res
        
    
def find(u, parent):
    temp = u
    while parent[temp] != -1:
        temp = parent[temp]
        parent[u] = temp
    return temp

def union(u, v, parent):
    parent[u] = v


print("res: \n", numberOfIsland(3, 3, [[0,0], [0,1], [1,2], [2,1], [1,1]]))