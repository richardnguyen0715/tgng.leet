from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)
        dummy = ListNode(0, head)
        curr = dummy
        run = dummy.next
        while run:

            while run and run.val in nums:
                run = run.next
            
            if run:
                curr.next = run
                curr = curr.next
                run = run.next
        
        curr.next = None

        return dummy.next


