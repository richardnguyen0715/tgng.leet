from collections import defaultdict

path = []
visited = set()
adj = defaultdict(list)

def DFS(u, destination):
    if u == destination:
        print(path + [u])
        return
    
    path.append(u)
    visited.add(u)
    
    for i in adj[u]:
        if i not in visited:
            DFS(i, destination)
        
    visited.remove()
    path.pop()
    
    
    
    
    