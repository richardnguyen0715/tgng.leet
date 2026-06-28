from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        if count == 1:
            return None

        mid = count // 2
        curr = head
        for i in range(mid - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head