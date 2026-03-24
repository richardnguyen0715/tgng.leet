from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        slow = head
        fast = slow
        first = head
        count = 1

        # lấy k node đầu tiên
        for i in range(k - 1):
            fast = fast.next
        
        print(slow.val, fast.val)
        
        # Chạy lấy cuối cùng
        while fast.next:
            slow = slow.next
            fast = fast.next

        while first:
            if count == k:
                break
            count += 1
            first = first.next
        
        print(slow.val, fast.val, first.val)
        
        first.val, slow.val = slow.val, first.val

        return head
        
