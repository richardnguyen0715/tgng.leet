# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = list1

        curr = list1
        count = 0
        prevA, nextB = None, None
        while curr:
            if count == a - 1:
                prevA = curr
            if count == b + 1:
                nextB = curr
            count += 1
            curr = curr.next
        
        prevA.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = nextB

        return dummy.next

