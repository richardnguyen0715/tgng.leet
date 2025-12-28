# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = nex = None
        # 1 -> 2 -> None
        # nex: None, prev = 1, slow = 2
        # nex: 1, prev = 2, slow = None
        while slow:
            nex = prev
            prev = slow
            slow = slow.next
            prev.next = nex

        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True