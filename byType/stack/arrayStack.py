class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    
class LinkedListStack:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self._size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val
    
    def peek(self):
        if self.isEmpty():
            return None
        
        return self.head.val
    
    def isEmpty(self):
        return self.head is None or self._size == 0
    
    def size(self):
        return self._size


stack = LinkedListStack()
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
