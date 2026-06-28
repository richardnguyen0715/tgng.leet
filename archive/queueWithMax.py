from collections import deque
from typing import List



# class maxQueue:
    
#     def __init__(self):
#         self.queue = deque()
        
    
#     def enQueue(self, val):
#         self.queue.appendleft(val)
#         return True
    
#     def deQueue(self):
#         return self.queue.pop()
        
    
#     def getMax(self):
#         max = self.queue[0]
#         for i in self.queue:
#             if i > max:
#                 max = i
#         return max


from collections import deque

class maxQueue:
    
    def __init__(self):
        self.entryQueue = deque()
        self.maxQueue = deque()
        
    def enQueue(self, val):
        self.entryQueue.appendleft(val)
        
        while self.maxQueue and self.maxQueue[-1] < val:
            self.maxQueue.pop()
        
        self.maxQueue.append(val)
        return True
    
    def deQueue(self):
        val = self.entryQueue.pop()
        
        if self.maxQueue and val == self.maxQueue[0]:
            self.maxQueue.popleft()
        
        return val
    
    def getMax(self):
        return self.maxQueue[0]

        
        
    
maxQ = maxQueue()
maxQ.enQueue(4)
maxQ.enQueue(2)
maxQ.enQueue(3)
print(maxQ.getMax())
print(maxQ.deQueue())
print(maxQ.getMax())
