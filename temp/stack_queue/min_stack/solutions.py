import numpy as np

class MinStack(object):

    def __init__(self):
        self.min_val = np.inf
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val < self.min_val:
            self.min_val = val

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.stack) > 0:
            self.min_val = min(self.stack)
        else:
            self.min_val = np.inf
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()