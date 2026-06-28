from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None

        run = head
        nums = []
        while run:
            nums.append(run.val)
            run = run.next
        
        n = len(nums)
        k = k % n

        # print(k)
        # print(nums)

        run = head
        i = 0
        while i < n and run:
            newPos = i - k
            if newPos < 0:
                newPos += n
            # print(i, newPos)
            run.val = nums[newPos]
            run = run.next
            i += 1
        
        return head
