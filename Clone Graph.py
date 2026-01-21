
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



# Beat: 5.27% time, 5.38% space
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Time: O(E+V) -> E là số cạnh, V là số nodes
        # Space: O(V) -> Số nodes
        
        if not node:
            return None

        hash_map = {}
        visited = set()

        def nodeTraversal(curNode, visited, hash_map):
            hash_map[curNode] = Node(curNode.val)
            # print("add ", curNode.val)
            visited.add(curNode)

            for neighbor in curNode.neighbors:
                if neighbor not in visited:
                    nodeTraversal(neighbor, visited, hash_map)

            return hash_map

        hash_map = nodeTraversal(node, visited, hash_map)

        visited = set()
        def getNeighbors(curNode, hash_map):
            
            visited.add(curNode)

            for neighbor in curNode.neighbors:
                hash_map[curNode].neighbors.append(hash_map[neighbor])
            
            for neighbor in curNode.neighbors:
                if neighbor not in visited:
                    getNeighbors(neighbor, hash_map)
            
            return hash_map

        hash_map = getNeighbors(node, hash_map)
            
        return hash_map[node]
    

# Cách trình bày khác của DFS phát triển từ code cũ
# Beat: 22% time, 16% space
# Time: O(E+V), O(V)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}
        
        def dfs(curr_node):
            if curr_node in cloned:
                return
            
            # Tạo clone
            cloned[curr_node] = Node(curr_node.val)
            
            # Recursive clone neighbors
            for neighbor in curr_node.neighbors:
                dfs(neighbor)
            
            # Set up connections
            for neighbor in curr_node.neighbors:
                cloned[curr_node].neighbors.append(cloned[neighbor])
        
        dfs(node)
        return cloned[node]


# Beat: 33% time, 15.89% space
# Sử dụng DFS -> chỉ cần một lần travel
# Time: O(E+V), O(V)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}
        
        def dfs(node):
            if node in cloned:
                return cloned[node]
            
            # Tạo clone node
            clone = Node(node.val)
            cloned[node] = clone
            
            # Clone tất cả neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)


from collections import deque

# Beat: 27% time, 16% space
# Sử dụng queue để implement BFS -> tránh stack overflow
# Time: O(E+V), O(V)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                cloned[curr].neighbors.append(cloned[neighbor])
        
        return cloned[node]