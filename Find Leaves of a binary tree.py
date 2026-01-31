def findLeaves(root):
    ans = []
    
    def dfs(node):
        
        # Time: O(N)
        # Space: O(H)
        
        nonlocal ans
        if not node:
            return -1
    
        height = max(dfs(node.left), dfs(node.right)) + 1
    
        if height < len(ans):
            ans[height].append(node.val)
        else:
            ans.append(node.val)
            
        return height

    dfs(root)
    return ans