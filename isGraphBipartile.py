from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n # Color tượng trưng cho chẵn lẻ đường từ gốc đến hiện tại. # -1: chưa đi qua, 0: đã đi qua rồi, đỉnh lẻ, 1: đã đi qua rồi nhưng đỉnh chẳn (đi chẵn bước để từ gốc đến đỉnh hiện tại)
        has_odd_cycle = False
        
        def dfs(node_u, current_color):
            nonlocal has_odd_cycle
            color[node_u] = current_color

            # Xét các cạnh kề của node U -> đi tiếp
            for node_v in graph[node_u]:
                if color[node_u] >= 0 and color[node_v] == color[node_u]:
                    # 2 đỉnh cùng chẵn hoặc cùng lẽ kề nhau. (lẻ + lẻ) = chẵn , (chẵn + chẵn) = chẵn , +1 (đường đi từ u -> v) -> lẻ và luôn có chu trình.
                    has_odd_cycle = True
                    return
                elif color[node_v] == -1:
                    dfs(node_v, 1 - current_color) # Kề với đỉnh hiện tại chưa đi qua thì sẽ đổi màu cho nốt sắp tới (xen kẽ) -> từ đỉnh chẵn thì tiếp theo sẽ thành đỉnh lẻ, đỉnh lẻ thành đỉnh chẵn.

        # Xét tất cả các đỉnh góc có thể có (tìm all chu trình)
        for i in range(n):
            if color[i] == -1:
                dfs(i, 0)

        return not has_odd_cycle
        


