from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses # Chứa bậc của các đỉnh
        mapCourses = {} # Chứa các cạnh kề của đỉnh đó

        for i in range(numCourses): # Khởi tạo các cạnh kề rỗng
            mapCourses[i] = []

        
        for u, v in prerequisites:
            degrees[v] += 1
            mapCourses[u].append(v)
        
        dq = deque()
        results = []

        for i in range(numCourses):
            if degrees[i] == 0: # Thêm các node gốc
                dq.append(i)

            
        while dq:
            current = dq.popleft() # Lấy ra các node
            results.append(current)

            # Xét các cạnh kề của current
            for node in mapCourses[current]:
                degrees[node] -= 1

                if degrees[node] == 0:
                    dq.append(node)

        # Khi đồ thị có chu trình thì khi đến một giai đoạn thì sẽ không còn node gốc nữa mà luôn có node cha -> tức là mọi degree trong degrees đều >= 1
        if len(results) != numCourses:
            return False
        return True
    



