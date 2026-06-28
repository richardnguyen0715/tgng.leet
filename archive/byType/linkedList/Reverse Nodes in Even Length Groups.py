from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        count = 1
        
        while prev.next:
            curr = prev
            actual_count = 0
            for i in range(count):
                if curr.next:
                    curr = curr.next
                    actual_count += 1
                else:
                    break
            
            if actual_count % 2 == 0:
                prev = self.reverseGroup(prev, actual_count)
            else:
                for i in range(actual_count):
                    prev = prev.next
            
            count += 1
        
        return dummy.next
    
    def reverseGroup(self, prev, k):
        group_start = prev.next
        curr = group_start
        
        prev_node = None
        for i in range(k):
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        
        prev.next = prev_node
        group_start.next = curr
        
        return group_start