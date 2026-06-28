from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return True
        
        numRemainRooms = len(rooms) - 1
        visitedRooms = [False] * len(rooms)
        visitedRooms[0] = True
        keyList = deque()
        for key in rooms[0]:
            keyList.append(key)

        print(keyList)
        
        while keyList:
            # Lấy chìa khóa
            key = keyList.popleft()

            if not visitedRooms[key]:
                visitedRooms[key] = True
                numRemainRooms -= 1

            # Vào phòng
            roomKeys = rooms[key]

            for k in roomKeys:
                if k not in keyList and not visitedRooms[k]:
                    keyList.append(k)
            
        return numRemainRooms == 0
    

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return True
        
        visitedRooms = [False] * len(rooms)
        visitedRooms[0] = True
        
        keyList = deque()
        for key in rooms[0]:
            keyList.append(key)

        print(keyList)
        
        while keyList:
            # Lấy chìa khóa
            key = keyList.popleft()

            if not visitedRooms[key]:
                visitedRooms[key] = True
                numRemainRooms -= 1

            # Vào phòng
            roomKeys = rooms[key]

            for k in roomKeys:
                if k not in keyList and not visitedRooms[k]:
                    keyList.append(k)
            
        return all(visitedRooms)
    
    
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return True
        
        visited = [False] * len(rooms)
        visited[0] = True
        
        queue = deque([0])
        
        while queue:
            current_room = queue.popleft()
            
            for key in rooms[current_room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        
        return all(visited)