from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

# Beat: 100% time, 30% Space
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time: O(N)
        # Space: O(1)
        
        if not head:
            return None

        if not head.next:
            return head


        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
        
        return dummy.next
    
    

# Time: O(N)
# Space: O(N) - recursion

# Beat: 100% Time & 30% Space
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        second = head.next
        
        head.next = self.swapPairs(second.next)
        
        second.next = head
        
        return second