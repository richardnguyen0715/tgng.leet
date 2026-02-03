from typing import List




# TLE
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # Analysis:
        # Cell nào mà có giá trị bé hơn giá trị từ nó đến biển gần nhất.
        # Ví dụ: (O,O) mà muốn ra biển thì ít nhất cần R - 1 - i hoặc C - 1 - j giá trị.
        # => (0,0) = 1, không thể ra khỏi do 1 < 4


        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j, result, visited):
            height = heights[i][j]
            if i + height > m - 1 or height - i >= 0 or j + height > n - 1 or height - j >= 0:
                if j == n - 1 or i == m - 1 or j == 0 or i == 0:
                    if j == n - 1 or i == m - 1:
                        result[1] = True
                    if j == 0 or i == 0:
                        result[0] = True

                visited.add((i, j))

                for dx, dy in directions:
                    nX, nY = i + dx, j + dy
                    if 0 <= nX < m and 0 <= nY < n and (nX, nY) not in visited and heights[nX][nY] <= heights[i][j]:
                        # print(f"From {i, j} to {nX, nY}")
                        dfs(nX, nY, result, visited)
                
                visited.remove((i, j))

            return result

        ans = []
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                height = heights[i][j]

                if i + height > m - 1 or height - i >= 0 or j + height > n - 1 or height - j >= 0:

                    print("Passed: ", i, j)
                    result = [False, False]       
                    visited = set()
                    result = dfs(i, j, result, visited)
                    print(result)

                    if result[0] and result[1]:
                        ans.append([i, j])
                    
                    print("---=---")

        return ans
    
    
    
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Tạo 2 set để lưu các cell có thể đến được mỗi đại dương
        pacific = set()
        atlantic = set()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j, ocean):
            ocean.add((i, j))
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                # Điều kiện: trong bounds, chưa visit, và có thể flow ngược (cao hơn hoặc bằng)
                if (0 <= ni < m and 0 <= nj < n and 
                    (ni, nj) not in ocean and 
                    heights[ni][nj] >= heights[i][j]):
                    dfs(ni, nj, ocean)
        
        # DFS từ các cell biên Pacific (hàng đầu và cột đầu)
        for i in range(m):
            dfs(i, 0, pacific)  # Cột đầu
        for j in range(n):
            dfs(0, j, pacific)  # Hàng đầu
            
        # DFS từ các cell biên Atlantic (hàng cuối và cột cuối)  
        for i in range(m):
            dfs(i, n-1, atlantic)  # Cột cuối
        for j in range(n):
            dfs(m-1, j, atlantic)  # Hàng cuối
        
        # Tìm giao của 2 tập hợp
        return list(pacific & atlantic)