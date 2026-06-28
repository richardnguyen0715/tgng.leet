from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_vals = []
        l2_vals = []
        while l1:
            l1_vals.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_vals.append(str(l2.val))
            l2 = l2.next
        
        # print(l1_vals)
        # print(l2_vals)

        l1_val_reversed = l1_vals[::-1]
        l2_val_reversed = l2_vals[::-1]

        # print(l1_val_reversed)
        # print(l2_val_reversed)

        separator = ""
        l1_int = int(separator.join(l1_val_reversed))
        l2_int = int(separator.join(l2_val_reversed))


        print(l1_int)
        print(l2_int)

        l3_int = l1_int + l2_int

        ans = []

        while l3_int >= 1:
            ans.append(int(l3_int % 10))
            l3_int //= 10

        if len(ans) == 0:
            ans.append(0)

        print(ans)

        head = ListNode(ans[0])
        tail = head

        for i in ans[1:]:
            tail.next = ListNode(i)
            tail = tail.next


        return head



class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + carry
            carry = s // 10
            cur.next = ListNode(s % 10)

            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0

        # walk through the linked list adding nodes on the same idx together
        # track carry, handling cases of double carry and adding a one (99 + 1)        
        while l1 and l2:
            l1_new_val = l1.val + l2.val + carry

            if l1_new_val >= 10:
                carry = 1
            else:
                carry = 0

            l1.val = l1_new_val % 10
            
            # point to the end of either linked list on the last iteration
            if not l1.next or not l2.next:
                break

            l1 = l1.next
            l2 = l2.next
        
        # handle cases of l1 has more digits
        if l2.next:
            l1.next = l2.next

        while l1.next:
            l1 = l1.next
            l1_new_val = l1.val + carry

            if l1_new_val == 10:
                carry = 1
            else:
                carry = 0

            l1.val = l1_new_val % 10

        if carry:
            l1.next = ListNode(1)

        return head