class MinStack(object):

    def __init__(self):
        """
            push vào trong stack một cặp gồm val và min hiện tại!!!
            : [(val, min)]
        """
        self.stack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.is_empty():
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def is_empty(self):
        return len(self.stack) == 0
        

    def pop(self):
        """
        :rtype: None
        """
        if self.is_empty():
            raise Exception("Stack is Empty!")

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()