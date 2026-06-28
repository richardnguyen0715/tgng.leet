from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        run = head
        greaterCount = 0
        nums = []

        while run:
            nums.append(run.val)
            if run.val >= x:
                greaterCount += 1
            run = run.next
        
        print(nums)
        print(greaterCount)
        n = len(nums)
        res = [0] * n
        i = n - greaterCount
        j = 0
        for num in nums:
            if num >= x:
                res[i] = num
                i += 1
            else:
                res[j] = num
                j += 1
        
        print(res)
        run = head
        i = 0
        while run:
            run.val = res[i]
            i += 1
            run = run.next
        
        return head


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Tạo 2 dummy nodes cho 2 phần
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # 2 pointers để build 2 lists
        smaller = smaller_dummy
        greater = greater_dummy
        
        # Duyệt 1 lần duy nhất
        current = head
        while current:
            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Nối 2 lists lại
        greater.next = None  # Quan trọng: cắt đuôi
        smaller.next = greater_dummy.next
        
        return smaller_dummy.next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:

            if head.val >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next

            head = head.next
        
        after.next = None
        before.next = after_head.next

        return before_head.next