import random
class Heap:
    def __init__(self):
        self.pool = []
 
    def push(self, val):
        self.pool.append(val) # cần siftup node mới
        self._sift_up()
 
    def _get_parent(self, idx):
        return (idx - 1) // 2  # (idx * 2 + 1) (idx * 2 + 2)
 
    def _get_left(self, idx):
        return idx * 2 + 1
 
    def _get_right(self, idx):
        return idx * 2 + 2
 
    def _swap(self, x, y):
        self.pool[x], self.pool[y] = self.pool[y], self.pool[x]
 
    def _sift_up(self):
        start = len(self.pool) - 1
        while start != 0:
            pa = self._get_parent(start)
            if self.pool[start] < self.pool[pa]:
                self._swap(start, pa)
            start = pa
 
    def _sift_down(self):
        """
        for i in range(len(self.pool) - 1, -1, -1):
            self._sift_down(i)
       
        """
        start = 0
        while True:
            left, right = self._get_left(start), self._get_right(start)
            if left >= len(self.pool) and right >= len(self.pool):
                break
            #index left < right
            pivot = left
            if right < len(self.pool) and self.pool[pivot] > self.pool[right]:
                pivot = right
            if self.pool[pivot] >= self.pool[start]:
                break
            self._swap(pivot, start)
            start = pivot
 
    def pop(self):
        if not self.pool:
            raise Exception("not valid")
        ans = self.pool[0]
        self._swap(0, len(self.pool) - 1)
        self.pool.pop()
        #print(self.pool)
        self._sift_down()
      #  print(self.pool)
        return ans
 
 
"""
            0
        1       2
     5    3  6     7
  10   8 9 4  
"""
 
 
def test():
    hp = Heap()
    xx = list(range(20))
    random.shuffle(xx)
   # print(xx)
    for i in xx:
        hp.push(i)
  #  print(hp.pool)
 
    ans = []
    while True:
        try:
            ans.append(hp.pop())
           # print(hp.pool)
        except:
            break
    print(ans)
 
 
test()