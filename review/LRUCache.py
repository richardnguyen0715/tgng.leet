class Node:
    
    def __init__(self, key =0, val = 0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next= self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self._move_to_head(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            node.val = value
            self._move_to_head(node)
        else:
            newNode = Node(key, value)

            if len(self.cache) >= self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = newNode
            self._add_node(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)