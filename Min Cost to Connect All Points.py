from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = {i : i for i in range(n)} # khởi tạo nó là parent của chính nó trước 
        self.rank = {i: 1 for i in range(n)} # bậc vào khởi tạo bằng 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        
        if parentX == parentY:
            # Tạo được chu trình
            return False

        # Setup parent cho x và y -> thằng nào lớn hơn thì ưu tiên làm parent
        if parentX < parentY:
            self.parent[parentX] = parentY
        
        else:
            
            self.parent[parentY] = parentX
            
            # Nếu rank bằng nhau thì cộng rank của parent lên 1
            if self.rank[parentX] == self.rank[parentY]:
                self.rank[parentX] += 1
        
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Time Complexity: O(N^2LogN)
        # Space Complexity: O(N^2)
        
        
        # Tạo một ma trận cạnh + weight để sử dụng được kruskal
        
        edges = []
        n = len(points)
        
        def calcMahattan(a, b):
            
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        for i in range(n):
            for j in range(i + 1, n):
                distance = calcMahattan(points[i], points[j])
                edges.append((i, j, distance))
        
        # Sort các cạnh này theo dộ dài bé nhất trước
        edges.sort(key=lambda x: x[2]) # x[2] là distance
        
        uf = UnionFind(n)

        n_edges = 0
        ans = 0
        
        for a, b, w in edges:

            # Thử merge 2 đỉnh A B nếu không tạo chu trình thì lấy
            if uf.union(a, b):
                n_edges += 1
                ans += w
            
            if n_edges == n - 1:
                break
        
        return ans
        
        
        