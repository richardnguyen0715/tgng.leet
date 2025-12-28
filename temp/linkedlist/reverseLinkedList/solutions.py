from typing import List

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
# 1 -> 2 -> 3 -> 4 -> 5
# ne = None, prev = 1, head = 2 -> prev.next = None
# ne = prev, prev = 2, head = 3 -> prev.next = 1
# 5 -> 4 -> 4 -> 2 -> 1 -> Null (None) -> Singly linked list
# Time complexity: O(n)
# Spece complexity: O(1)
        
def reverseLinkedList(head: List[ListNode]) -> List[ListNode]:
    
    prev, ne = None, None
    while head:
        ne = prev
        prev = head
        head = head.next
        prev.next = ne
    
    return prev