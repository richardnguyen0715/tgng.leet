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

        if not head:
            return False

        prev, ne = None, None

        def clone_list(head):
            if not head:
                return None
            dummy = ListNode(0)
            cur_new = dummy
            cur_old = head
            while cur_old:
                cur_new.next = ListNode(cur_old.val)
                cur_new = cur_new.next
                cur_old = cur_old.next
            return dummy.next
        
        head2 = clone_list(head)
        while head2:
            ne = prev
            prev = head2
            head2 = head2.next
            prev.next = ne

        while head != None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True

        