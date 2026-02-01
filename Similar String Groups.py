from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)
        parent = [-1] * n

        def find(i , parent):
            u = i

            while parent[u] != -1:
                u = parent[u]
                parent[i] = u
            
            return u

        def union(u, v, parent):
            parent[u] = v
        
        def isSimilar(a , b):

            if a == b:
                return True
            
            if len(a) != len(b):
                return False
            
            n = len(a)

            i = 0
            j = n - 1
            # Vì chỉ cần swap 2 phần tử nên tìm trái qua và phải qua rồi swap
            # Tìm phần tử khác nhau đầu tiên từ trái qua
            while i < n and a[i] == b[i]:
                i += 1
            
            # Tìm phần tử khác nhau đầu tiên từ phải qua
            while j >= 0 and a[j] == b[j]:
                j -= 1
            
            if i == j:
                return False
            
            # Swap characters
            temp = list(a)
            temp_char = temp[i]
            temp[i] = temp[j]
            temp[j] = temp_char

            return "".join(temp) == b

        for i in range(n):
            for j in range(i + 1, n):
                # Nếu 2 thằng giống nhau thì cho thành một liên thông và 1 thằng trong số đó làm gốc
                if isSimilar(strs[i], strs[j]):
                    u = find(i , parent)
                    v = find(j, parent)
                    if u != v:
                        union(u , v, parent)

        res = 0
        # Đếm số node gốc còn lại -> 1 node gốc là 1 thành phần liên thông chứa các từ simi vs nhau
        for i in range(n):
            if parent[i] == -1:
                res += 1
        
        return res
                    
