from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # Time Limit
    # Time: O(N^2)
    # Space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        run = headA
        while run:
            run2 = headB
            while run2:
                if run2 == run:
                    return run2
                run2 = run2.next
            run = run.next
        
        return None
    

class Solution:
    
    # Pass, beat 95.83% time, 82,17% space
    # Time: O(N)
    # Space: O(M)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodeList = {}
        run = headA
        while run:
            nodeList[run] = 0
            run = run.next
        
        run = headB
        while run:
            if run in nodeList:
                return run
            run = run.next
        
        return None