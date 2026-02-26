from typing import List, Optional
from heapq import heapify, heappop, heappush


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Không cần thực hiện setup hàm so sánh cho ListNode bằng cách sử dụng counter thể hiện xem thằng nào vào trước thì thằng đó lên trước nếu như trùng chỉ số.
        # Ví dụ: (val, counter, Node)
        # Tức là heap so sánh val -> counter -> Node, nhưng do Node ko có operation so sánh -> phải ko cho nó đi quá counter -> counter phải duy nhất khi val bị trùng (counter là một tier breaker)
        
        pool = []
        for i, lst in enumerate(lists):
            if lst:
                pool.append((lst.val, i, lst))
        
        dummy = ListNode(0)
        temp = dummy
        counter = len(lists)
        heapify(pool)
        
        while pool:
            _, _, node = heappop(pool)
            temp.next = node
            temp = temp.next
            node = node.next
            if node:
                heappush(pool, (node.val, counter, node))
                counter +=1
            
        return dummy.next
        