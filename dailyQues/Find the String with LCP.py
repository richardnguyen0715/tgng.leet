from typing import List


class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        group = {}
        cur = ord('a')
        res = [''] * n
        
        for i in range(n):
            root = find(i)
            if root not in group:
                if cur > ord('z'):
                    return ""
                group[root] = chr(cur)
                cur += 1
            res[i] = group[root]
        
        word = "".join(res)
        
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i == n-1 or j == n-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i+1][j+1]
        
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word