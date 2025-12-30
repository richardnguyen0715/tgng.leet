from collections import defaultdict

def solutions(edges):
    
    # Ý tưởng: duyệt qua tất cả các đỉnh, và các đường đi có thể có từ các đỉnh đó, nếu còn dư thì ans +1. Tức là 2 thành phần liên thông A,B sẽ không có đường đi tới nhau
    # => Xuất phát tại mọi đỉnh chưa đi qua, tìm đến đích cuối mà từ đỉnh đó có thể đi được sẽ là một thành phần liên thông, sau khi xong thì đỉnh nào chưa visit tức là nằm trong thành phần liên thông khác -> khi đó duyệt lại là +1 thêm.
    adj = defaultdict[list]
    
    
    for i , j in edges:
        adj[i].append(j)
        adj[j].append(i)
        
    
    visited = set()
    
    def dfs(node_u):
        
        visited.add(node_u)
        for node_v in adj[node_u]:
            if node_v not in visited:
                dfs(node_v)
                
    
    ans = 0
    for i in range(len(adj)):
        if i not in visited:
            dfs(i)
            ans += 1
            
        
    return ans
        