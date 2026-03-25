# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        stack = []
        n = len(nums)
        nextGreater = [-1] * n
        for i in range(n - 1, -1, -1):

            val = nums[i]

            while stack and nums[stack[-1]] <= val:
                stack.pop()
            
            if stack:
                nextGreater[i] = nums[stack[-1]]
            stack.append(i)

        print(nextGreater)

        dummy = ListNode(0)
        curr = dummy
        for i in range(n):
            if nextGreater[i] == -1:
                curr.next = ListNode(nums[i])
                curr = curr.next
        
        return dummy.next
    
    
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy
        for node in stack:
            curr.next = node
            curr = curr.next
        
        curr.next = None
        return dummy.next
    
    
    
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        head.next = self.removeNodes(head.next)
        
        # If next node exists and has greater value, remove current node
        if head.next and head.val < head.next.val:
            return head.next
        
        return head