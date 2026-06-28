from collections import deque

class Topo:
    
    def __init__(self, n , edges):
        self.n = n
        self.degrees = [0] * n
        self.map_edges = {}
        self.visited = [False] * n
        
        for i in range(n):
            self.map_edges[i] = []
            
        for u, v in edges:
            self.map_edges[u].append(v)
            self.degrees[v] += 1
        
    
    def topoSorting(self):
        result = []
        dq = deque()
        
        for i in range(self.n):
            if self.degrees[i] == 0:
                dq.append(i)
                
        while dq:
            node = dq.popleft()
            result.append(node)
            adj_nodes = self.map_edges[node]
            for adj_node in adj_nodes:
                self.degrees[adj_node] -= 1
                if self.degrees[adj_node] == 0:
                    dq.append(adj_node)
        
        return result
    
    
    def topoSortingDFS(self):
        
        result = []
        
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i, result)
        
        result.reverse()
        
        return result
    
    def dfs(self, i , result):
        self.visited[i] = True
        adj_nodes = self.map_edges[i]
        
        for adj_node in adj_nodes:
            if not self.visited[adj_node]:
                self.dfs(adj_node, result)
                
        result.append(i)
        
        
        

topo = Topo(5, [(3, 0), (3, 1), (0, 2), (0, 4), (1, 4)])
print(topo.topoSortingDFS())
                
        
