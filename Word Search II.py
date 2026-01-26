from typing import List


# Time Limit Exceeded
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        if not board or not words:
            return []
        
        m = len(board)
        n = len(board[0])

        if n == 1 and m == 1:
            if board[0][0] in words:
                return [board[0][0]]
            else:
                return []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_len = max([len(word) for word in words])
        res = set()

        def early_terminate(candidates):
            candidate_str = "".join(candidates)
            for word in words:
                if word.startswith(candidate_str):
                    return False
            return True

        def dfs(i, j, candidates, pos_visited):
            # THÊM ký tự hiện tại vào candidates và visited TRƯỚC
            candidates.append(board[i][j])
            pos_visited.add((i, j))
            
            # SAU ĐÓ mới kiểm tra
            if early_terminate(candidates):
                candidates.pop()
                pos_visited.remove((i, j))
                return

            if len(candidates) > max_len:
                candidates.pop()
                pos_visited.remove((i, j))
                return
            
            # Kiểm tra xem có tìm được từ hoàn chỉnh không
            candidate_str = "".join(candidates)
            if candidate_str in words:
                res.add(candidate_str)
            
            # Duyệt các ô kề cận
            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in pos_visited:
                    dfs(new_x, new_y, candidates, pos_visited)

            # Backtrack
            candidates.pop()
            pos_visited.remove((i, j))

        # Bắt đầu DFS từ mỗi ô
        for i in range(m):
            for j in range(n):
                if board[i][j] not in [k[0] for k in words]:
                    continue
                dfs(i, j, [], set())
        
        return list(res)
    
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = set()
        
        # Tạo Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True
        
        def dfs(i, j, node, path, visited):
            # Kiểm tra bounds và visited trước
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
                return
                
            char = board[i][j]
            if char not in node:
                return
            
            # Thêm ký tự hiện tại vào path và visited
            visited.add((i, j))
            path += char
            node = node[char]  # Di chuyển đến node tiếp theo trong trie
            
            # Kiểm tra xem có phải là từ hoàn chỉnh không
            if '#' in node:
                res.add(path)
            
            # Tiếp tục DFS với các ô kề cận
            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                dfs(new_x, new_y, node, path, visited)
            
            # Backtrack
            visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "", set())
        
        return list(res)
    

# ----------------------------------------------

def insert(transitions: dict, word: str) -> None:
    current = transitions
    for ch in word:
        if ch not in current:
            current[ch] = {}
        current = current[ch]
    current['$'] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        transitions = {}
        res = []
        m, n = len(board), len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        for word in words:
            insert(transitions, word)
        
        def dfs(x, y, node):
            ch = board[x][y]
            if ch not in node:
                return
            nxt = node[ch]

            if '$' in nxt:
                res.append(nxt['$'])
                del nxt['$']

            visited[x][y] = 1

            if x > 0 and visited[x-1][y] == 0:
                dfs(x-1, y, nxt)
            if x < m-1 and visited[x+1][y] == 0:
                dfs(x+1, y, nxt)
            if y > 0 and visited[x][y-1] == 0:
                dfs(x, y-1, nxt)
            if y < n-1 and visited[x][y+1] == 0:
                dfs(x, y+1, nxt)

            visited[x][y] = 0
            if not nxt:
                del node[ch]

        for i in range(m):
            for j in range(n):
                dfs(i, j, transitions)
                
        return res
