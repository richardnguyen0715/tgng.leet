from collections import deque



# Beat: 100% Space, 5% time
class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.max_cap = capacity
        self.least_recent_key = deque()
        self.current_cap = 0
        

    def get(self, key: int) -> int:
        # print(f"Find {key} in {self.cache}")
        val = self.cache.get(key, None)
        if key in self.least_recent_key:
            self.least_recent_key.remove(key) # O(N)
            self.least_recent_key.append(key)
            # print("Get methods -> Least Recent Queue Status: ", self.least_recent_key)
        # print(f"Found {val}")
        if val is not None:
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key đã tồn tại: cập nhật value và di chuyển lên đầu
            self.cache[key] = value
            self.least_recent_key.remove(key) # O(N)
            self.least_recent_key.append(key)
        else:
            # Key mới: kiểm tra capacity trước khi thêm
            if self.current_cap >= self.max_cap:
                # Xóa least recent key
                remove_key = self.least_recent_key.popleft()
                self.delete_least(remove_key)
                self.current_cap -= 1
            
            # Thêm key mới
            self.cache[key] = value
            self.least_recent_key.append(key)
            self.current_cap += 1
        
    def delete_least(self, remove_key):
        # print("Before removing")
        # print(self.cache)
        if remove_key in self.cache:
            del self.cache[remove_key]
        # print("After removing")
        # print(self.cache)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Sử dụng Hashmap + Doubly linkedlist để tối ưu thời gian
# Beat: 95% time, 67% space
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Dummy head và tail để dễ thao tác
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Thêm node ngay sau head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Xóa node khỏi linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Di chuyển node lên đầu (most recent)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Xóa node cuối cùng (least recent)"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            # Di chuyển lên đầu
            self._move_to_head(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if node:
            # Update existing key
            node.val = value
            self._move_to_head(node)
        else:
            # Add new key
            new_node = Node(key, value)
            
            if len(self.cache) >= self.capacity:
                # Remove least recent
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = new_node
            self._add_node(new_node)