class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

        # Analyze: 
        # word in words có thể khác kích thước và tối đa lên tới 3 * 10^4 ký tự
        # chỉ có thể đi lên xuống trái phải -> không đi xéo

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
        print(max_len)

        res = set()

        pos_visited = set()
        len_visited = set()

        candidates = []

        def early_terminate(candidates):

            # Nếu có bất cứ từ ngữ nào sai thì dừng ngay luôn. Ví dụ: Candidates: ['a'] mà không có từ nào bắt đầu bằng 'a' -> loại luôn.
            
            for word in words:
                if "".join(candidates) in word[:len(candidates)]:
                    return False
            
            return True

        def dfs(i, j):

            nonlocal candidates

            # if early_terminate(candidates):
            #     print("early stopping")
            #     return

            if len(candidates) > max_len:
                print("more than max_len")
                return
            
            if "".join(candidates) in words:
                print("Got candidates: ", "".join(candidates.copy()))
                res.add("".join(candidates.copy()))
                return

            candidates.append(board[i][j])
            pos_visited.add((i, j))
            
            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in pos_visited:
                    # print("current candidates: ", candidates)
                    # print("next step: ", new_x, new_y)
                    dfs(new_x, new_y)

            candidates.pop()
            pos_visited.remove((i, j))

        for i in range(m):
            for j in range(n):
                print("start from: ", i, j)
                dfs(i, j)
                print("------------------")
        
        return list(res)