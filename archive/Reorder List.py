from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Đưa tất cả nodes vào stack
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        # Reorder
        curr = head
        n = len(stack)
        
        for i in range(n // 2):
            next_node = curr.next
            tail = stack.pop()
            
            curr.next = tail
            tail.next = next_node
            curr = next_node
        
        # Cắt connection cuối
        curr.next = None