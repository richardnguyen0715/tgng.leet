from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Case chỉ có 1 node
        if not head.next:
            return None

        dummy = ListNode(0, head)
        parent = dummy

        while parent:
            temp = parent
            cnt = 0

            # đi n bước từ parent
            while cnt < n and temp:
                temp = temp.next
                cnt += 1

            # nếu đi đủ n bước và temp là node cuối
            if cnt == n and temp and temp.next is None:
                parent.next = parent.next.next
                break

            parent = parent.next

        return dummy.next



# 2 pointers
def removeNthFromEnd(self, head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
