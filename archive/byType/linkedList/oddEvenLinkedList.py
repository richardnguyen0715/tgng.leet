from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        dummyOdd = ListNode(0)
        dummyEven = ListNode(0)
        odd = dummyOdd
        even = dummyEven

        count = 1
        curr = head
        while curr:
            if count % 2 != 0:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            count += 1
            curr = curr.next

        # print(odd)
        # print(even)
        even.next = None
        
        odd.next = dummyEven.next
        return dummyOdd.next

