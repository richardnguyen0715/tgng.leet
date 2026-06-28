from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        visited = [False] * n
        visited[0] = True

        queue = deque()
        queue.extend(rooms[0][:])

        while queue:
            key = queue.popleft()
            newKeys = rooms[key]
            visited[key] = True
            for newKey in newKeys:
                if not visited[newKey]:
                    queue.append(newKey)
        
        return all(visited)



