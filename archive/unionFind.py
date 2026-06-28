class MyGraph:
    
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        
    
    def add(self, i, j):
        u = self.find(i)
        v = self.find(j)
        
        if u != v:
            self.union(u, v)
        
    # time: O(N)
    def find(self, i):
        while self.parent[i] != -1:
            i = self.parent[i]
        
        return i
    
    def union(self, i, j):
        self.parent[i] = j
    
    def query(self, i, j):
        return self.find(i) == self.find(j)


class MyGraph:
    
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.height = [1] * n
        
    
    def add(self, i, j):
        u = self.find(i)
        v = self.find(j)
        
        if u != v:
            self.union(u, v)
        
    # Optimized: Chỉ cần quan tâm đến nút gốc -> là thành phần liên thông thì chỉ cần chung gốc => lấy gốc nhanh nhất
    def find(self, i):
        u = i
        while self.parent[u] != -1:
            u = self.parent[u]
            self.parent[i] = u
        
        return u
    
    
    # Optimized -: uư tiên cây cao hơn làm cha
    # Time: O(1)
    def union(self, i, j):
        
        if self.height[i] > self.height[j]:
            self.parent[j] = i
        elif self.height[j] > self.height[i]:
            self.parent[i] = j
        else:
            self.height[i] += 1        
            self.parent[i] = j
    
    def query(self, i, j):
        return self.find(i) == self.find(j)
    
    

myG = MyGraph(5)
myG.add(0,1)
myG.add(2,4)
print(myG.query(0,4))
myG.add(1,2)
print(myG.query(0,4))