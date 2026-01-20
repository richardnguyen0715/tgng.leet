from collections import deque

# Time limit exceeded
class StockSpanner:

    def __init__(self):
        self.entry_queue = deque()
        
    def next(self, price: int) -> int:
        self.entry_queue.append(price)
        n = len(self.entry_queue)

        if n == 1:
            return n

        cnt = 0
        j = n - 1
        while j >= 0 and self.entry_queue[j] <= price:
            j -= 1
            cnt += 1
        
        return cnt





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


from collections import deque


# Time limit exceeded -> Do mỗi lần chạy đều phải build lại stack
class StockSpanner:

    def __init__(self):
        self.entry_list = []
        
        
    def next(self, price: int) -> int:
        self.entry_list.append(price)
        n = len(self.entry_list)

        if n == 1:
            return n

        res = []
        stack = deque()
        # print(self.entry_list)
        for i in range(n):
            while stack and self.entry_list[stack[-1]] <= self.entry_list[i]:
                stack.pop()
            
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)

            stack.append(i)

        # print(res)
        
        return n - 1 - res[-1]



# Lưu lại stack -> hết TLE
from collections import deque

class StockSpanner:
    
    # Time: O(1)
    # Space: O(N)

    def __init__(self):
        self.prices = []
        self.stack = deque()
        
        
    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices) - 1
        
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        
        if self.stack:
            span = i - self.stack[-1]
        else:
            span = i + 1
        
        self.stack.append(i)
        return span
    
    

# Time: O(1), Space: O(N) -> Beat: 40% time
class StockSpanner:

    def __init__(self):
        self.stack = []  # (price, span)
        
    def next(self, price: int) -> int:
        
        # Ý tưởng: mỗi lần mà price lớn hơn đỉnh thì pop ra tới khi nhỏ hơn xong +span lên
        
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[-1] # get the span

        self.stack.append((price, span))
        return span



# Time: O(1), space: O(N) -> beat: 100% time
class StockSpanner:

    
    # Chạy nhanh hơn là do:
    # len(self.prices) rẻ hơn self.stack and ...
    # So sánh xảy ra sau khi đã vào vòng -> self.prices[-1][0] > price, còn cách trên thì lần nào cũng so sánh.
    # -1 phải thực hiện thêm phép tính len(tuple) - 1.
    def __init__(self):
        self.prices = []        

    def next(self, price: int) -> int:
        span = 1
        while len(self.prices):
            if self.prices[-1][0] > price:
                break
            
            span += self.prices.pop()[1]
        
        self.prices.append((price, span))
        return span
