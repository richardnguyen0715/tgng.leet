from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        import heapq
        ListNode.__lt__ = lambda s, other : 1

        pool = [(lst.val, lst) for lst in lists if lst]
        heapq.heapify(pool)

        dummy = temp = ListNode(0)

        while pool:
            _, curr_list = heapq.heappop(pool)
            temp.next = curr_list
            temp = temp.next
            curr_list = curr_list.next
            if curr_list:
                heapq.heappush(pool, (curr_list.val, curr_list))

        return dummy.next
