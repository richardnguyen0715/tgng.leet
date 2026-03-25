import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        while cur.next:
            addNode = ListNode(math.gcd(cur.val, cur.next.val))
            addNode.next = cur.next
            cur.next = addNode
            cur = addNode.next
        
        return head