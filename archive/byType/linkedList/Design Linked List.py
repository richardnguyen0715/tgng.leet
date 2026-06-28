
class ListNode:
    def __init__(self, val = 0, prevNode = None, nextNode = None):
        self.val = val
        self.prev = prevNode
        self.next = nextNode

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def _getNode(self, index: int) -> ListNode:
        if not self.head or self.size == 0 or index >= self.size:
            return None
        
        if index < self.size // 2:
            runNode = self.head
            for _ in range(index):
                runNode = runNode.next
        else:
            runNode = self.tail
            for _ in range(self.size - 1, index, -1):
                runNode = runNode.prev
        return runNode
        

    def get(self, index: int) -> int:
        node = self._getNode(index)
        return node.val if node else -1        

    def addAtHead(self, val: int) -> None:
        if not self.head or self.size == 0:
            self.head = self.tail = ListNode(val)
        else:
            newNode = ListNode(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail or self.size == 0:
            self.head = self.tail = ListNode(val)
        else:
            newNode = ListNode(val)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if self.size < index or index < 0:
            return
    
        if index == self.size:
            self.addAtTail(val)
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        nextNode = self._getNode(index)
        prevNode = nextNode.prev
        
        newNode = ListNode(val)
        
        prevNode.next = newNode
        newNode.prev = prevNode
        nextNode.prev = newNode
        newNode.next = nextNode
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        
        node = self._getNode(index)
        if not node:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        self.size -= 1
    

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)