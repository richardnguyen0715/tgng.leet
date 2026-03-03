from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        valList = []
        run = head
        while run:
            valList.append(run.val)
            run = run.next
        
        doublingList = deque()
        carry = 0
        for i in range(len(valList) - 1, -1, -1):
            val = valList[i]
            multiply = val * 2 + carry
            digit = multiply % 10
            carry = multiply // 10
            doublingList.appendleft(digit)
        
        if carry > 0:
            doublingList.appendleft(carry)
        
        dummy = ListNode(0)
        run = dummy
        for val in doublingList:
            run.next = ListNode(val)
            run = run.next
        
        return dummy.next