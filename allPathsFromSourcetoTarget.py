from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        # Step 1: Các bước giải đầu tiên thì luôn là chuyển biểu diễn về adjust matrix

        # Step 2: định nghĩa các biến cần thiết 
        ans = []
        path =[0]
        visited = set()
        visited.add(0)
        n = len(graph) - 1

        # Step 3: Định nghĩa DFS -> Tìm đường luôn là DFS, BFS thường đc dùng để tìm ngắn nhất 
        def dfs(node_u):
            if node_u == n:
                ans.append(path.copy())
                return

            for node_v in graph[node_u]:
                if node_v not in visited:
                    visited.add(node_v)
                    path.append(node_v)
                    dfs(node_v)
                    visited.remove(node_v)
                    path.pop()

        dfs(0)
        return ans