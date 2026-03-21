from typing import List, Optional


class ListNode:
    def __int__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prefix_sum = 0
        seen = {0: dummy}

        cur = head

        while cur:
            prefix_sum += cur.val

            if prefix_sum in seen:
                prev = seen[prefix_sum]
                temp = prev.next

                temp_sum = prefix_sum

                while temp != cur:
                    temp_sum += temp.val
                    if temp_sum in seen:
                        del seen[temp_sum]
                    temp = temp.next

                prev.next = cur.next
            else:
                seen[prefix_sum] = cur

            cur = cur.next

        return dummy.next