from typing import List


class Solution:
    
    # DFS nhanh hơn cách Union Find
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        # Build adjacency list (more efficient than matrix)
        graph = [[] for _ in range(n)]
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = [False] * n
        components = 0
        
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        # Count connected components
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components - 1
    
    
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Need at least n-1 cables to connect n computers
        if len(connections) < n - 1:
            return -1
        
        # Union-Find data structure
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True  # Successfully connected two components
            return False  # Already connected (redundant cable)
        
        # Process all connections
        redundant_cables = 0
        for x, y in connections:
            if not union(x, y):
                redundant_cables += 1
        
        # Count number of connected components
        components = len(set(find(i) for i in range(n)))
        
        # Need (components - 1) operations to connect all components
        return components - 1