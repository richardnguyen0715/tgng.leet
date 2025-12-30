
from collections import deque, defaultdict



deQueue = deque()
visited = set()
paths = []
adj = defaultdict(list)

def BFS(start, dest):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        u = path[-1]

        if u == dest:
            return path

        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(path + [v])

    

adj[1] = [2, 5]
adj[2] = [1, 3, 5]
adj[3] = [2, 4]
adj[4] = [3, 5, 6]
adj[5] = [1, 2, 4]
adj[6] = [4]
deQueue.append(1)

if __name__ == "__main__":
    print(BFS(1, 4))