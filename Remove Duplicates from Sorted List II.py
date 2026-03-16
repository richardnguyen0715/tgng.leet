from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = prev.next

        while curr:
            flag = False
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                flag = True
            curr = curr.next
            if flag:
                prev.next = curr
            else:
                prev = prev.next
        
        return dummy.next

            