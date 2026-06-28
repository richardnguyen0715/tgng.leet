from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)

        current = head
        while current:
            nextNode = current.next

            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            current.next = prev.next
            prev.next = current

            current = nextNode
        
        return dummy.next