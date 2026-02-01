from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Khi có chu trình thì sẽ thực hiện return về empty
        # Topo sorting sài BFS thì khi ko tìm được cạnh nào có bậc vào bằng 0 thì là có chu trình

        degrees = [0] * numCourses
        mapCourses = {}
        for i in range(numCourses):
            mapCourses[i] = []

        
        for v, u in prerequisites:
            degrees[v] += 1
            mapCourses[u].append(v)

        
        result = []
        dq = deque()

        for i in range(numCourses):
            if degrees[i] == 0:
                dq.append(i)
            
        while dq:
            curr = dq.popleft()
            result.append(curr)

            for j in mapCourses[curr]:
                degrees[j] -= 1
                if degrees[j] == 0:
                    dq.append(j)


        # Tức là có chu trình xảy ra thì ko trả về
        if len(result) != numCourses:
            return []

        return result
    



