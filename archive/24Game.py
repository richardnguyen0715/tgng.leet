from typing import List
from collections import combinations


# Beat: 5% time, 17% space
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        # Time: N^(2N)
        # Mỗi bước có O(N^2) cho 2 số lấy ra, sau đó có 4 dấu để chọn -> thêm N bước tất cả để chọn hết
        
        # Space: O(N)

        ops = ['+', '-', '*', '/']

        n = len(cards)
        ans = False

        def equal(a, b):
            if abs(a - b) < 10E-10:
                return True
            return False


        def eval(op, a, b):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return a / b if not equal(b, 0) else float('inf')


        def process(remain_cards):
            nonlocal ans
            if len(remain_cards) == 1:
                if equal(remain_cards[0], 24):
                    ans = True
                return

                
            for (a, b) in combinations(remain_cards, 2):

                remain_cards.remove(a)
                remain_cards.remove(b)
                for op in ops:

                    res_ab = eval(op, a, b)
                    if res_ab < float('inf'):
                        remain_cards.append(res_ab)
                        process(remain_cards)
                        remain_cards.remove(res_ab)
                    
                    res_ba = eval(op, b, a)
                    if res_ba < float('inf'):
                        remain_cards.append(res_ba)
                        process(remain_cards)
                        remain_cards.remove(res_ba)
                    
                remain_cards.append(a)
                remain_cards.append(b)

        
        process(cards)
        return ans

                    

# beat: 90% time, 7% space
class Solution:
    def judgePoint24(self, nums):
        EPS = 1e-6
        
        def dfs(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24) < EPS
            
            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = arr[i], arr[j]
                    
                    next_arr = []
                    for k in range(n):
                        if k != i and k != j:
                            next_arr.append(arr[k])
                    
                    for val in self.compute(a, b):
                        next_arr.append(val)
                        if dfs(next_arr):
                            return True
                        next_arr.pop()
            
            return False
        
        return dfs(list(map(float, nums)))
    
    
    def compute(self, a, b):
        res = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:
            res.append(a / b)
        if abs(a) > 1e-6:
            res.append(b / a)
        return res