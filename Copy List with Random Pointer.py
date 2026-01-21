from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        # Time: O(N)
        # Space: O(N)
        # Problem: Tốn thêm bộ nhớ ngoài
            
        if not head:
            return None

        hash_map = {}

        cur = head
        while cur:
            hash_map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                hash_map[cur].next = hash_map[cur.next]
            if cur.random:
                hash_map[cur].random = hash_map[cur.random]
            
            cur = cur.next
        
        return hash_map[head]
    

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
        # Không dùng thêm bộ nhớ ngoài
        # Time: O(N)
        # Space: O(1)
        
        if not head:
            return None

        # Ghép thêm node mới
        cur = head
        while cur:
            tempNode = Node(cur.val)
            tempNode.next = cur.next
            cur.next = tempNode
            cur = cur.next.next

        # Thêm random node

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        
        # Cắt ra các phần tử mới

        dummy = Node(0)
        tempNode = dummy
        cur = head

        while cur:
            tempNode.next = cur.next
            cur.next = cur.next.next
            tempNode = tempNode.next
            cur = cur.next
        
        return dummy.next

